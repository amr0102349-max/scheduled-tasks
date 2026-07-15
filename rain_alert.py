import os 
import requests
from twilio.rest import Client
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid =os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
from_number = os.environ.get("FROM_NUMBER")
to_number = os.environ.get("TO_NUMBER")
weather_params ={
    "lat" :  18.840603 ,
    "lon" :  95.257996 ,
    "appid" : api_key ,
    "cnt" :4

}
response = requests.get(OWM_Endpoint, params =weather_params )
response.raise_for_status()
weather_data = response.json()


list_weather =[]
will_rain  = False
for per_id in weather_data["list"] :
    twelve_hour = per_id["weather"][0]["id"]
    if twelve_hour <700 :
        will_rain = True


if True :
    client = Client(account_sid , auth_token)
    message  =client.messages \
        .create(
        body="ي عجل",
        from_="from_number",
        to= "to_number"
    )

    print (message.status)
