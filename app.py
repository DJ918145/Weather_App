tefrom streamlit import *
import requests

def weather(state, country):
    api_key = "API_KEY" # Enter your api key by login weather api
    base_url = "http://api.weatherapi.com/v1/current.json"
    url = f"{base_url}?key={api_key}&q={state},{country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c'] 
        # write("Temprature is  : ", temp,"°C")
        condition = data['current']['condition']['text']
        markdown(f"<h1 style='font-size: 21px;'>Temprature is : {temp} °C</h1>", unsafe_allow_html=True)
        markdown(f"<h1 style='font-size: 21px;'>Condition is : {condition}</h1>", unsafe_allow_html=True)
        markdown(f"<h1 style='font-size: 21px;'>Wind speed is : {data['current']['wind_mph']}in MPH</h1>", unsafe_allow_html=True)
        markdown(f"<h1 style='font-size: 21px;'>Wind speed is : {data['current']['wind_kph']} in KPH</h1>", unsafe_allow_html=True)
        markdown(f"<h1 style='font-size: 21px;'>Wind direction is : {data['current']['wind_dir']}</h1>", unsafe_allow_html=True)
        # write("Wind speed is  : ", data['current']['wind_mph']," in MPH")
        # write("Wind speed is  : ", data['current']['wind_kph']," in KPH")
        # write("Wind direction is  : ", data['current']['wind_dir'])
        
        # print(f"The current temperature in {state} is {temp}°C with {weather_description}.")
    else:
        print(f"Failed to retrieve weather data: {response.json().get('message', 'Unknown error')}")

    
markdown(f"<h1 style='font-size: 50px; text-align: center '> Weather </h1>", unsafe_allow_html=True)
state = text_input("Enter the State Name")
country = text_input("Enter the Country Name")
if(button("Submit")):
    state = state.title().lower()
    weather(state, country)
