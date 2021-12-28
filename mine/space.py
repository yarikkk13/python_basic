# current location of ISS
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
obj = response.json()
print(response.status_code)
print(obj['iss_position'])

# create post in pastebin
dev_key = 'mOVA76wa34rCszzR_BKmSzsKRWFxuoF_'
user_name = 'yarik13'
password = 'jn4y6Lpsu@E34Js'

my_title = 'It`s title of my post'
paste_code = "Hello! This is my first post!"
login_data = {
    'api_dev_key': dev_key,
    'api_user_name': user_name,
    'api_user_password': password
}

login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")

print("User token: ", login.text)
my_user_key = login.text

data = {
    'api_option': 'paste',
    'api_dev_key': dev_key,
    'api_paste_code': paste_code
}

req = requests.post("https://pastebin.com/api/api_post.php", data=data)
print("Paste send: ", req.status_code if req.status_code != 200 else "OK/200")
print("Paste URL: ", req.text)
