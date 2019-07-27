# Auto
import json, requests
user = input("Search by username:").capitalize()
r = requests.get ("https://jsonplaceholder.typicode.com/users", params={"username" : user})
print(r.json())

# Manual
# import json
# user = input("Search by username:").capitalize()
# json.loads("https://jsonplaceholder.typicode.com/users")
