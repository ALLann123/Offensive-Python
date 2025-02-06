#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def fetch_vulnerabilities(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP issues
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Adjust the selector based on the actual NVD structure
        vulnerabilities = soup.find_all('tr', class_='srrowns')  # Example based on the NVD layout
        
        for vuln in vulnerabilities:
            title = vuln.find('a')  # Find the vulnerability title link
            if title:
                print(title.text.strip(), '-', title['href'])  # Print title and link

    except requests.exceptions.RequestException as e:
        print(f"Error fetching vulnerabilities: {e}")

# Example usage
vulnerability_feed = 'https://nvd.nist.gov/general/nvd-dashboard'
fetch_vulnerabilities(vulnerability_feed)
