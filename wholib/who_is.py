#!/usr/bin/python3
import whois

def get_whois_info(target):
		#target=input("Enter the Domain>>")
		dm_info=whois.whois(target)
		#print(dm_info)

		print("Registar:", dm_info.registrar) #Get Registar

		print("Creation Date:", dm_info.creation_date) # Get Creation Date

		print("Expiration Date:", dm_info.expiration_date) #Expiration Date

		print("Country:", dm_info.country) #Get Country
		print("Country:", dm_info.emails)
