import requests


def ip_public():
    """
    Affiche l'adresse IP public de l'utilisateur
    :return: IP public
    :rtype: str
    """

    r = requests.get("https://api.ipify.org/?format=json")
    ip_non_formate = str(r.text)

    ip_formate = ip_non_formate[7:21]
    return f'Voici votre IP public : {ip_formate}'


print(ip_public())
