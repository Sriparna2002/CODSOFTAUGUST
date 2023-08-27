import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox 

import requests
import os
from datetime import datetime

def weather():
    try:
        weather_api = os.environ['weather_api']
        location = location_entry.get()
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+weather_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data['cod'] == 404:
            print("Invalid City : {} Please, check your city name".format(location))
        else:
            api_city = ((api_data['main']['temp'])-273.15)
            api_desc = api_data['weather'][0]['description']
            api_humidity = api_data['main']['humidity']
            api_wind = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            result_label.config(text="Weather Stats for - {}  || {}".format(location.upper(), date_time))
            temp_label.config(text="Current temperature is: {:.2f} deg C".format(api_city))
            desc_label.config(text="Current weather desc: " + api_desc)
            humidity_label.config(text="Current Humidity: {} %".format(api_humidity))
            wind_label.config(text="Current wind speed: {} kmph".format(api_wind))

    except KeyError:
        result_label.config(text="API Key not found in environment variables")
    except Exception as e:
        result_label.config(text="An error occurred: {}".format(str(e)))


root = tk.Tk()
font_name = "Lobster"
font_size = 30
font = (font_name, font_size)

font2_name = "LilitaOne-Regular.ttf"
font2_size = 15
font2_style = "bold"
font2 = (font2_name, font2_size,font2_style)

font3_name = "Consolas"
font3_size = 12
font3 = (font3_name, font3_size)

background_color = "#ECECEC"
header_background = "light blue"
header_foreground = "Dark blue"
label_foreground = "Dark blue"
button_background = "#0074E4"  
button_foreground = "#FFFFFF"  

root.geometry("600x500")
root.title("Weather Forecast")
root.resizable(0,0)
root.configure(bg="light blue")


header_frame = tk.Frame(root, bg= header_background)
functions_frame = tk.Frame(root, bg = header_background )


header_frame.pack(fill="both")
functions_frame.pack(side = "left",expand = True, fill = "both")  

header_label = ttk.Label(
    header_frame,
    text="Weather Forecast",
    font=font,
    background=header_background,
    foreground=header_foreground
)
header_label.pack(padx = 20, pady = 5)



location_label = ttk.Label(   
    functions_frame,  
    text = "Enter the Location Name",  
    font = font2,  
    background = header_background,  
    foreground = label_foreground   
)  
location_label.pack(padx=50)

location_entry = ttk.Entry(  
    functions_frame,  
    font = font3,
    width = 25,  
    background = "#FFF8DC",  
    foreground = "#A52A2A"  
)  

location_entry.pack(padx=50, pady=20) 

get_weather_button = ttk.Button(  
        functions_frame,  
        text = "Search",  
        width = 24,  
        command = weather,
        style="TButton"
)  
get_weather_button.pack(padx=50)  

result_label = tk.Label(
    functions_frame,  
    text="", 
    font=("Helvetica", 12, "bold"),
    background = header_background,  
    foreground = label_foreground
)
result_label.pack(padx=50, pady=10,  anchor="center")  

temp_label = tk.Label(
    functions_frame, 
    text="", 
    font=("Helvetica", 12),
    background = header_background,  
    foreground = label_foreground
)
temp_label.pack(padx=50, anchor="center")  

desc_label = tk.Label(
    functions_frame,  
    text="", 
    font=("Helvetica", 12),
    background = header_background,  
    foreground = label_foreground
)
desc_label.pack(padx=50,  anchor="center")  

humidity_label = tk.Label(
    functions_frame,  
    text="", 
    font=("Helvetica", 12),
    background = header_background,  
    foreground = label_foreground
)
humidity_label.pack(padx=50,  anchor="center") 

wind_label = tk.Label(
    functions_frame,  
    text="", 
    font=("Helvetica", 12),
    background = header_background,  
    foreground = label_foreground
)
wind_label.pack(padx=50,anchor="center")  

s = ttk.Style()
s.configure("Custom.TButton", background=button_background, foreground=button_foreground)
root.mainloop()