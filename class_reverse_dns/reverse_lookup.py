#!/usr/bin/python3
import ipaddress
import socket
import requests

# Define API Key
api_key = '691956333b6ca21eccd538b5864949893966d0ff'

def is_valid_ip(ip):
    """
    Check if an IP address is valid.

    :param ip: str, IP address
    :return: bool, True if valid, False otherwise
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def reverse_lookup(ip):
    """
    Perform a reverse lookup to find the domain of an IP address.

    :param ip: str, IP address
    :return: str or None, Domain name if found, otherwise None
    """
    try:
        domain = socket.gethostbyaddr(ip)[0]
        return domain
    except socket.herror:
        return None

def get_websites_on_server(ip):
    """
    Retrieve all websites hosted on the same server as the given IP.

    :param ip: str, IP address
    :return: list, List of domain names hosted on the server
    """
    url = f"https://api.viewdns.info/reverseip/?host={ip}&apikey={api_key}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "response" in data and "domains" in data["response"]:
                return data["response"]["domains"]
        else:
            print(f"[-] API Request Failed: {response.status_code}")
    except requests.RequestException as e:
        print(f"[-] Network Error: {e}")
    return []
