import requests

url = "https://randomuser.me/api/"
users = []
data = requests.get(url).json()
a = 0
while a < 10:
    response = requests.get(url)
    s = response.json()
    first_name = s["results"][0]["name"]["first"]
    last_name = s["results"][0]["name"]["last"]
    if s["results"][0]["gender"] == "male":
        users.append(first_name+" "+last_name)
        a += 1
print(users)

def gender_user(data):
    return data.get("gender")

print(gender_user(data))

def fullname_user(data):
    t = data.get("name")
    return f"{t.get("first")} {t.get("last")}"

print(fullname_user(data))

def email_user(data):
    return data.get("email")

print(email_user(data))

def phone_user(data):
    return data.get("phone")

print(phone_user(data))

def address_user(data):
    return data.get("location")["city"]

print(address_user(data))

def username(data):
    return data.get("login")["username"]

print(username(data))