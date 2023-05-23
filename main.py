import requests
import json
import sqlite3

import schedule
import win10toast
import requests


#
key = '20eaa45d6a8810567a41b6c0472bea18'
city_name="Tbilisi"
country_code="ISO 3166-2:GE"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={key}'
re = requests.get(url)

print(re)
print(re.status_code)
print(re.headers)
print(re.text)

toJson=re.text

file=open('json.txt','w')
file.write(toJson)
file.close()

# file = open('json.txt', 'r')
# toLoad = json.load(file)
# file.close()

toDict=json.loads(toJson)

re_structured = json.dumps(toDict, indent=6)
print(re_structured)

main = toDict["main"]
wind=toDict["wind"]
weather=toDict["weather"]
weather_num=weather[0]

temp_far = main["temp"]
humidity = main["humidity"]
pressure=main["pressure"]
wind_speed=wind["speed"]
main_weather=weather_num["main"]




print('ტემპერატურა: ', temp_far, 'ცელსიუსი')
print('ტენიანობა: ', humidity, '%')
print('წნევა: ', pressure, "პას")
print('ქარის სიჩქარე: ', wind_speed, 'კმ/სთ')
print('ამინდი: ', main_weather)



conn = sqlite3.connect("Weather_API_Data")
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Weather
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ქალაქი VARCHAR(50),
#         ტემპერატურა FLOAT,
#         ტენიანობა FLOAT,
#         წნევა FLOAT,
#         ქარის_სიჩქარე FLOAT,
#         ზოგადი_ამინდი VARCHAR(50));''')


# cursor.execute('INSERT INTO Weather (ქალაქი, ტემპერატურა, ტენიანობა,წნევა,ქარის_სიჩქარე,ზოგადი_ამინდი) VALUES (?, ?, ?, ?, ?, ?)', (city_name, temp_far, humidity,pressure,wind_speed,main_weather))
# conn.commit()
#
# conn.close()


#Windows Notification
def weather_notification():
    toast = win10toast.ToastNotifier()

    toast.show_toast(title=f'{city_name}-ის ამინდი', msg=f'{main_weather}       ტემპერატურა: {temp_far} ფრნ\nტენიანობა: {humidity}%\nწნევა: {pressure} პასკ\nქარის სიჩქრე: {wind_speed}კმ/სთ', duration=20,icon_path=None)

# schedule.every(10).seconds.do(weather)
# while True:
#     schedule.run_pending()
weather_notification()
