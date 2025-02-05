#!/usr/bin/python3
from reverse_lookup import get_websites_on_server

ip = input("Enter the server IP: ")
websites = get_websites_on_server(ip)

if websites:
    print("\n[+] Websites hosted on the same server:")
    for site in websites:
        print(f" - {site}")
else:
    print("[-] No other websites found on the same server.")
