import psutil
import platform
import requests
import json


hostname = psutil.users()[0].host
user = psutil.users()[0].name
os =  platform.system()

memory = psutil.virtual_memory()
percentRam = memory.percent
usedRam = memory.used

url = "http://127.0.0.1:5000/informations"
data = {"host" : hostname, "os" : os, "user" : user,"percentRam" : percentRam, "usedRam" : usedRam }
print data
headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

r = requests.post(url, data = json.dumps(data), headers=headers)
print r.text
print r.status_code