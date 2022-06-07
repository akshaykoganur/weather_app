# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
import requests
from PIL import Image, ImageTk

# Open WeatherMap API Key : 59c465747fc12f3b377de08210cf11c3
# API url : https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

root = tk.Tk()

def response(weat):
    try:
        name = weat['name']
        temp = weat['main']['temp']
        hum = weat['main']['humidity']
        desc = weat['weather'][0]['description']
        final = ('City : %s\nTemparature : %s\nHumidity : %s\nDescription : %s' % (name, temp, hum, desc))
    except:
        final = "Couldn't find record"
    finally:
        return final


def weather(city):
    weather_key = '59c465747fc12f3b377de08210cf11c3'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {'appid': weather_key, 'q': city, 'units': 'metric'}
    res = requests.get(weather_url, param)
    weat = res.json()       # we get the weather info in json format
    result['text'] = response(weat)    # text to be written in result box


# creating window and giving size
root.title("Weather App")
root.geometry("600x500")

# considering image
img = Image.open("weather.jpg")
img = img.resize((600, 500))
img_photo = ImageTk.PhotoImage(img)

# setting the image at background
bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

# creating introduction label
intro = tk.Label(bg_lbl, bg="#00FF00", text="Welcome to Weather App", font=('times new roman', 20))
intro.place(x=150, y=30, width=300, height=50)

# creating label Enter city
title = tk.Label(bg_lbl, bg="#FFFF00", text="Enter City", font=('times new roman', 18))
title.place(x=50, y=100)

# making frame
frame1 = tk.Frame(bg_lbl, bg="pink", bd=5)
frame1.place(x=50, y=150, width=500, height=44)

# creating two columns in frame and assigning first column to input
txt_box = tk.Entry(frame1, width=30, font=('times new roman', 18))
txt_box.grid(row=0, column=0, sticky='w')

# assigning second column to search button
btn = tk.Button(frame1, text="Search", font=('times new roman', 13), command=lambda: weather(txt_box.get()))
btn.grid(row=0, column=1, padx=50)

# creating the frame for result
frame2 = tk.Frame(bg_lbl, bg="#AED6F1", bd=10)
frame2.place(x=100, y=250, height=200, width=400)

# creating the result
result = tk.Label(frame2, bg="white", font=('times new roman', 18), justify='left')
result.place(relwidth=1, relheight=1)

root.mainloop()   # ending of the code lines written after it will not get executed

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
