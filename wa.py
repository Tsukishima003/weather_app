import streamlit as st
import requests
from dotenv import load_dotenv
import os 

load_dotenv()

os.environ["API_KEY"] = st.secrets["API_KEY"]

API_KEY = os.getenv("API_KEY1")
st.set_page_config(
    page_title = "weatherapp"
)

st.title("weather app")
city = st.text_input("enter the city name ")


API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
if st.button ("weather data"):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        st.success("Data fetched successfully")

        name = data["name"]
        country = data["sys"]["country"]
        st.subheader(f"weather data for {name} , {country}")

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_Speed = data["wind"]["speed"]
        weather = data["weather"][0]["main"]
                                            
        col1 ,col2 , col3 , col4 = st.columns(4)

        col1.metric("🌡️temp" , f"{temp}°C")
        col2.metric("☔humidity" , f"{humidity}")
        col3.metric("💨wind_speed" , f"{wind_Speed}")
        col4.metric("🌤️weather" , f"{weather}")
    else:
        st.error("not a valid place")
        