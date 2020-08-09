import tkinter as tk
import requests


HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("THis is the entry")
    
# PUT YOUR  OPENWEATHERMAP LINK ADDRESS HERE! (sign in to OpenWeatherMap, see the description for more info)
# PUT YOUR OPENWEATHERMAP KEY HERE

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem finding the location you where looking for'

    return final_str
 

def get_weather(city):
    weather_key = 'PUT YOUR API WEATHER KEY HERE AGAIN'
    url = 'PUT YOUR HTTPS LINK HERE AGAIN'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'} 
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", font=('Gotham Book', 10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
                       

label = tk.Label(lower_frame, font=('arial', 14), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
