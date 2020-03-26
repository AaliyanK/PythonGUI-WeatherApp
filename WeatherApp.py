import tkinter as tk
# can use .place/.grid/.pack to place items on ur GUI
from tkinter import font
import requests


def test_function(entry):
    print('this is the entry:', entry)

# e8cfcc42688907b56bd0dfefaa347b48
# api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        finalstr = f'City: {str(name)} \n Conditions: {str(desc)} \n  Temperature: {str(temp)}'
    except:
        finalstr = 'A problem!'

    return finalstr


def get_weather(city):
    weather_key = 'e8cfcc42688907b56bd0dfefaa347b48'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()  # API INFO

    label['text'] = format_response(weather)
    # connecting with tkinter


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=800)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Dimensions of our screen
frame = tk.Frame(root, bg='#057BF6', bd=5)  # bd=border
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# 0.8 x 0.8

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get Weather', font=40,
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#057BF6', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18),
                 anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()
