import requests
from os import environ,path
from twilio.rest import Client
from dotenv import load_dotenv

basedir=path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))

apikey=environ.get('APIKEY')
account_sid=environ.get('ACCOUNT_SID')
auth_token=environ.get('AUTH_TOKEN')


url='https://api.openweathermap.org/data/2.5/forecast'

params={
    "lat":17.385044,
    "lon":78.486671,
    "appid":apikey
}
will_rain=False
response=requests.get(url=url,params=params)
print(response.raise_for_status)
weather_data=response.json()
weather_slice=weather_data['list'][:8]
for hour_data in weather_slice:
    weather_code=hour_data['weather'][0]['id']
    print(weather_code)
    if int(weather_code)<700:
        will_rain=True
if will_rain==True:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Bring your umbrella",
                        from_='+19045076643',
                        to='+917288856612'
                    )

