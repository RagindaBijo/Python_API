import requests
import json
import sqlite3
import win10toast
import requests
import schedule


#1
key = '3b430798bddf0914db3b9793b234d3b0'
city_name="Tbilisi"
cnt=1
country_code="ISO 3166-2:GE"
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&cnt={cnt}&appid={key}'
re = requests.get(url)

print(re)
print(re.status_code)
print(re.headers)
print(re.text)

toJson=re.text


#2
toDict=json.loads(toJson)
re_structured = json.dumps(toDict, indent=6)

# file=open('json.json','w')
# file.write(toJson)
# file.close()
#
# file=open('json_dump.json','w')
# file.write(re_structured)
# file.close()
#
# file = open('json.json', 'r')
# toLoad = json.load(file)
# file.close()
#
# file = open('json_dump.json', 'r')
# toLoad = json.load(file)
# file.close()



re_structured = json.dumps(toDict, indent=6)
print(re_structured)


#3
list_of_main=toDict["list"]
num_of_list=list_of_main[cnt-1]
main = num_of_list["main"]
wind=num_of_list["wind"]
weather=num_of_list["weather"]
weather_num=weather[0]

date=num_of_list["dt_txt"]
temp_far = main["temp"]
humidity = main["humidity"]
pressure=main["pressure"]
wind_speed=wind["speed"]
main_weather=weather_num["main"]



print('თარიღი: ',date)
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
#         თარიღი VARCHAR(50),
#         ტემპერატურა FLOAT,
#         ტენიანობა FLOAT,
#         წნევა FLOAT,
#         ქარის_სიჩქარე FLOAT,
#         ზოგადი_ამინდი VARCHAR(50));''')


cursor.execute('INSERT INTO Weather (ქალაქი,თარიღი, ტემპერატურა, ტენიანობა,წნევა,ქარის_სიჩქარე,ზოგადი_ამინდი) VALUES (?, ?, ?, ?, ?, ?, ?)', (city_name, date, temp_far, humidity,pressure,wind_speed,main_weather))
conn.commit()

conn.close()


#Windows Notification
def weather_notification():
    toast = win10toast.ToastNotifier()

    toast.show_toast(title=f'{city_name}    თარიღი: {date}', msg=f'{main_weather}       ტემპერატურა: {temp_far} ფრნ\nტენიანობა: {humidity}%\nწნევა: {pressure} პასკ\nქარის სიჩქრე: {wind_speed}კმ/სთ', duration=5,icon_path=None)

# schedule.every(10).seconds.do(weather)
# while True:
#     schedule.run_pending()
weather_notification()