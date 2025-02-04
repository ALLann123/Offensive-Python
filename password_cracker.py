#!/usr/bin/python3
import hashlib

def try_passwords(hash_to_crack, path_to_directory):
	with open(path_to_directory, 'r')as file:
		for password in file.readlines():
			hashed_pw=hashlib.sha256(password.strip().encode()).hexdigest()
			if hashed_pw==hash_to_crack:
				return password.strip()
	return "Password not found"


hash_to_crack=input("Enter the hash>> ")

path_dictionary=input("Enter path and name to dictionary>> ")

cracked_password=try_passwords(hash_to_crack,path_dictionary)
print(f"Password {cracked_password}")
