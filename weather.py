import tkinter as tk
import requests

#uses api to call for weather data by city from openweather

def get_weather(city):
    weather_key = 'ef248c4221ff37829e6e2eed13b3b167'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APIkey': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params = params)
    weather = response.json()

    weather_output['text'] = format_response(weather)

#formats output to display weather to user

def format_response(weather):
    try:
        location = weather['name']
        descrip = weather['weather'][0]['description']
        loc_temp = weather['main']['temp']

        return 'Location: ' + location + '\n' + 'Current Conditions: ' + descrip + '\n' + 'Temperature: ' + str(loc_temp)
    except:
        return 'Location not found'

#GUI setup

width = 800
height = 800

root = tk.Tk(className= 'Weather App')
root.geometry("500x500")
root.resizable(0, 0)

background_image = tk.PhotoImage(file='./bg.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

city_bg = tk.Frame(root, bg = '#cfeaff', bd = 5)
city_bg.place(relx = 0.5, rely = 0.05, relwidth = 0.9, relheight = 0.1, anchor = 'n')

city_enter = tk.Entry(city_bg)
city_enter.place(relx = 0.01, rely = 0.1, relwidth = 0.65, relheight = 0.8)

city_button = tk.Button(city_bg, text = "Get Weather", command = lambda: get_weather(city_enter.get()))
city_button.place(relx = 0.67, rely = 0.1, relwidth = 0.31, relheight = 0.8)

weather_frame = tk.Frame(root, bg = '#cfeaff', bd = 5)
weather_frame.place(relx = 0.5, rely = 0.2, relwidth = 0.9, relheight = 0.7, anchor = 'n')

weather_output = tk.Label(weather_frame)
weather_output.place(relwidth = 1, relheight = 1)

root.mainloop()
