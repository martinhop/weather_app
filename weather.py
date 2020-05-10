import tkinter as tk

width = 800
height = 800

root = tk.Tk(className= 'Weather App')
root.geometry("500x500")
root.resizable(0, 0)

city_bg = tk.Frame(root, bg = '#cfeaff', bd = 5)
city_bg.place(relx = 0.5, rely = 0.05, relwidth = 0.9, relheight = 0.1, anchor = 'n')

city_enter = tk.Entry(city_bg)
city_enter.place(relx = 0.01, rely = 0.1, relwidth = 0.65, relheight = 0.8)

city_button = tk.Button(city_bg, text = "Get Weather")
city_button.place(relx = 0.67, rely = 0.1, relwidth = 0.31, relheight = 0.8)

weather_frame = tk.Frame(root, bg = '#cfeaff', bd = 5)
weather_frame.place(relx = 0.5, rely = 0.2, relwidth = 0.9, relheight = 0.7, anchor = 'n')

weather_output = tk.Label(weather_frame)
weather_output.place(relwidth = 1, relheight = 1)

root.mainloop()
