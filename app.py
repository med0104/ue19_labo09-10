import requests

r = requests.get("https://api.ipify.org/?format=json")

ip_non_formate = str(r.text)

ip_formate = ip_non_formate[7:21]
print(f' Voici votre IP public : {ip_formate}')





