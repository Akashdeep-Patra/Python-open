import requests
import json

def wiki():
    response=requests.get("https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Craig%20Noone&format=json")
    out= response.json()
    return out
print(wiki())
