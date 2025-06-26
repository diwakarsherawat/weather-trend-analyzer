import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

API_KEY = "820e5eabae3f4baaae595740252606"  # 🔑 Replace with your key
BASE_URL = "http://api.weatherapi.com/v1/history.json"

def fetch_weather(city, date):
    params = {
        "key": API_KEY,
        "q": city,
        "dt": date
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
     


    if "forecast" in data:
        forecast = data["forecast"]["forecastday"][0]["day"]
        return {
            "date": date,
            "avg_temp": forecast["avgtemp_c"],
            "max_temp": forecast["maxtemp_c"],
            "min_temp": forecast["mintemp_c"],
            "humidity": forecast["avghumidity"],
            "condition": forecast["condition"]["text"]
        }
    else:
        return None

# Streamlit UI
st.set_page_config(layout="centered", page_title="Weather Trend Analyzer 🌦️")
st.title("📊 Weather Trend Analyzer")

city = st.text_input("Enter City Name", value="Delhi")
days = 7

if st.button("Analyze Weather"):
    with st.spinner("Fetching weather data..."):
        today = datetime.today()
        weather_data = []

        for i in range(days):
            date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
            data = fetch_weather(city, date)
            if data:
                weather_data.append(data)

        if not weather_data:
            st.error("Failed to fetch data.")
        else:
            df = pd.DataFrame(weather_data)
            df = df.sort_values("date")
            st.subheader(f"Weather Data for {city.title()}")
            st.dataframe(df)

            fig, axes = plt.subplots(1, 2, figsize=(14, 5))

            axes[0].plot(df["date"], df["avg_temp"], label="Avg Temp (°C)", marker='o', color='blue')
            axes[0].plot(df["date"], df["max_temp"], label="Max Temp (°C)", linestyle='--', color='red')
            axes[0].plot(df["date"], df["min_temp"], label="Min Temp (°C)", linestyle='--', color='green')
            axes[0].set_title("🌡️ Temperature")
            axes[0].set_xlabel("Date")
            axes[0].set_ylabel("°C")
            axes[0].tick_params(axis='x', rotation=45)
            axes[0].grid(True)
            axes[0].legend()

            axes[1].plot(df["date"], df["humidity"], label="Humidity (%)", marker='x', color='purple')
            axes[1].set_title("💧 Humidity")
            axes[1].set_xlabel("Date")
            axes[1].set_ylabel("%")
            axes[1].tick_params(axis='x', rotation=45)
            axes[1].grid(True)
            axes[1].legend()

            plt.tight_layout()
            st.pyplot(fig)
