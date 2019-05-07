import tkinter as tk
from tkinter import font
import requests
# from apiclient.discovery import build

HEIGHT = 500
WIDTH = 500

def test_function(name):
    print(name)

# key: 338f8bdeee24d0ba10baedee961a78f7
# url: api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

# youtube key: AIzaSyDhRwBBZ79ZdRFOegIVCsWxK2a2KwStKuY

def get_weather(city):
    weather_key = '338f8bdeee24d0ba10baedee961a78f7'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    report = response.json()

    label['text'] = format_response(report)

def format_response(report):
    try:
        name = report['city']['name']
        desc = report['list'][0]['weather'][0]['description']
        temp = report['list'][0]['main']['temp']

        result = f'City: {str(name)}\nConditions: {str(desc)}\nTemperature(°F): {str(temp)} '
    except:
        result = 'There was a problem with looking for your location'
    return result


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='hello3.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='gray', bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry = tk.Entry(frame, font=("Courier", 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", font=("Courier", 12), command=lambda:get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='grey', bd=3)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.4, anchor='n')


label = tk.Label(lower_frame, font=("Courier", 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()