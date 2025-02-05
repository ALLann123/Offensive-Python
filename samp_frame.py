#!/usr/bin/python3
import sys
#display menu
print("-----------STORY TELLING-----------------")
print("*****************************************")

while True:
	print("*****************************************")
	print("1.Password Attacks")
	print("2.Hash Identify")
	print("3.Reccon Whois")
	print("4.Network Scan")
	print("5.Identify websites on server")
	print()
	print("99.To exit")
	value=input("Choose attack(select the number)>> ")

	if value == "1":
		print()
		print("1.Dictionary Attack")
		print("2.Hash Identifier")
		print("3.Bruteforce")
		attack=input("Selected>> ")
		if attack=="1":
			print("Starting Dictonary Attack")
			hashed_pass=input("Enter the hash to be cracked>> ")
			path=input("Enter Path for wordlist>> ")
			print("Starting Dictionary attack")
		elif attack=="2":
			hash_pass=input("Enter the hash>>")
			print(f"Identifying the hash {hash_pass}")
	elif value == "99":
		print("Good bye")
		sys.exit()
