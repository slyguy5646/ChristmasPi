import requests

r = requests.get('http://192.168.1.214:5000/lightdata').json();

print(r)