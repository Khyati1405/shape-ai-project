import requests

responce=requests.get('https://api.openweathermap.org/data/2.5/weather?q=surat&appid=f4ce2400dfc2205c408737bc1a86e913')
with open('weather.txt','wb') as fd:
    for chunk in responce.iter_content(chunk_size=100):
        fd.write(chunk)

api_key='f4ce2400dfc2205c408737bc1a86e913'
location = input("enter the city name: ")
complete_api_link= "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']


print("---------")
print("weather shows for -{}".format(location.upper()))
print("---------")

print("current temperatur is: {:.2f} deg C".format(temp_city))
print("current weather desc: ",weather_desc)
print("current humidity: ",hmdt,'%')
print("current wind speed: ",wind_spd,'kmph')