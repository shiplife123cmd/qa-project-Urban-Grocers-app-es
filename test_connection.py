import requests

url = "https://cnt-4d79eb57-3441-4b4b-9a79-b389d311b686.containerhub.tripleten-services.com"

try:
    response = requests.get(url)
    print(response.status_code)
except Exception as e:
    print(e)