import requests

api_key = "1d90dd2bb4c3c3de302ac008bd13a079"
city = "Stockholm"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + \
    city+"&appid=f56175550dda9e8326a6989d1ada6657"

request = requests.get(url)

json = request.json()

print(json)
