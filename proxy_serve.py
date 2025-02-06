import requests
import certifi

response = requests.get("https://www.ku.ac.ke/", verify=certifi.where())
print(response)
