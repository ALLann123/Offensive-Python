#!/usr/bin/python3
import hashlib

password=input("Enter the Word to hash>> ")

hashed_pw=hashlib.sha256(password.strip().encode()).hexdigest()

print(f"Hashed Pass: {hashed_pw}")

