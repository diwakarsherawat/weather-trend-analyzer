# 🌦️ Weather Trend Analyzer

A simple and interactive weather dashboard built with **Streamlit**, powered by the **WeatherAPI**.  
This project fetches and visualizes live weather data (temperature, humidity, conditions) for any city.

---

## 🧠 Purpose

> I built this project to get hands-on experience with APIs, secure key management, and deployment using Streamlit.  
> It helped me understand the real-world workflow of API consumption, data parsing, charting, and hosting.

---

## 🚀 Live App

👉 [Click here to try the app](weather-trend-analyzer-eraxlswrxxopjwyeam35tf
.streamlit.app)  
(Replace this link with your actual Streamlit app URL)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – For building the web app interface
- **WeatherAPI** – For accessing weather data
- **Matplotlib / Pandas** – For data handling and visualization
- **GitHub** – Version control and hosting
- **Streamlit Cloud** – Free deployment platform

---

## 📸 Features

- 🌍 Input any city name
- 📅 Fetch today’s weather (or last 7 days if you have a paid key)
- 📊 Line charts for temperature and humidity
- 📋 Tabular summary of weather stats

---

## 🔐 Security Notes

API key is securely managed using:
- `.streamlit/secrets.toml` (local testing)
- `st.secrets` on **Streamlit Cloud**
- `.gitignore` to prevent key exposure on GitHub

---

## 🧪 How to Run Locally

1. Clone this repo  
```bash
git clone https://github.com/diwakarsherawat/weather-trend-analyzer.git
cd weather-trend-analyzer
