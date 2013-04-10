import requests
payload = {"name": "harada"}
r = requests.post("http://localhost:5001/users/harada")
print r.url

print r.text
