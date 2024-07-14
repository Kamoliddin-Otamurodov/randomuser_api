import requests
a = int(input())
gender = input()
inc = input()
payload = {"result" : a , "gender" : gender , "inc" : inc}
url = f"https://randomuser.me/api/"
response = requests.get(url , params=payload)
s = response.json()
print(s)