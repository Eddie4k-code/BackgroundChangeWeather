import requests
import ctypes
import json
import tkinter as tk
import customtkinter
from customtkinter import *







def main():
    def change_wall(image): #Setting Paths to images we want to use.
        img_cloud = r"" #Path to Cloud image goes here
        img_sun = r""   #Path to Sun image goes here
        img_rain = r""  #Path to Rain image goes here

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)

    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={entry.get()}&appid={API KEY HERE }')

    weather_data = response.json()

    weather_status = weather_data['weather'][0]['main'].lower()
    weather_label['text'] = weather_status


    #Just a few cases here, many could be added because of all of the different types of weather
    #Another way to do this instead of doing (e.g - clouds, sun, rain) one could do temperatures instead.
    if 'cloud' in weather_status:
        change_wall(img_cloud)
    elif 'sun' or 'clear' in weather_status:
        change_wall(img_sun)
    elif 'rain' or 'mist' in weather_status:
        change_wall(img_rain)





### GUI ####
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
root = tk.Tk()
root.title('Change Background Via Weather')
root.geometry('500x500')

label = customtkinter.CTkLabel(text='City')
label.pack()

entry = customtkinter.CTkEntry()
entry.pack()

button = customtkinter.CTkButton(text='Change Background', command=main)
button.pack()

weather_label = customtkinter.CTkLabel(text='')
weather_label.pack()




root.mainloop()
