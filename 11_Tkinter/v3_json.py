import requests
from pprint import pprint
import json

def get_json():
    username = "VisualStudioCode"
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    return user_data
print(get_json())

