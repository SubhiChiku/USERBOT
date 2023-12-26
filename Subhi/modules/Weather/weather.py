from pyrogram import Client, filters
import requests
from config import HANDLER as hl
from Subhi.userbot import RBX

api_key = "fadd97c7821d568d82f1cceaa06c7def"

@RBX.on_message(filters.command("weather", hl) & filters.me)
async def get_weather_info(client, message):
    city = "Mumbai"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        await message.edit(f"Weather in {city}:\n\nDescription: {weather_desc}\n\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
    else:
        await message.edit("Unable to fetch weather information..!!")
