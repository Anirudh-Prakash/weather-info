# Fetch Weather info from https://openweathermap.org
import requests
import json
API_KEY='[YOUR API KEY]'
city = input('Enter City Name:')
url='http://api.openweathermap.org/data/2.5/weather?appid=%s&units=metric&q=%s,IN' %(API_KEY,city)
data = requests.get(url)
data = json.loads(data.text)
print('Temperatures in degree Celsius')
weather={'Latitude':data['coord']['lat'],
'Lonngitude':data['coord']['lon'],
'Weather_details':data['weather'][0]['description'],
'Temp':data['main']['temp'],
'Temp (min)':data['main']['temp_min'],
'Temp (max)':data['main']['temp_max'],
'Humidity':data['main']['humidity']}

for key in weather:
    print(key+' : '+str(weather[key]))

