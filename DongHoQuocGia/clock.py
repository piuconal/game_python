from datetime import datetime
from tkinter import *
import tkinter as ui
import tkinter.ttk as combo
import requests
import time
import math
import pytz

window = ui.Tk()
window.geometry("1250x650")
window.title("Clock And Weather App")
canvas = ui.Canvas(window, width=1250, height=650, bg="black")
canvas.create_text(422,25, text= "CHỌN QUỐC GIA", font=('Helvetica','15','bold'), fill='white')

#tital
def update_clock0():
    #nation
    tz_nation0 = pytz.timezone(combo.get())
    now0 = datetime.now(tz_nation0)
    #time
    time_text0 = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now0.hour, now0.minute, now0.second)
    digital_clock_lbl0.config(text=time_text0)
    digital_clock_lbl0.after(1000, update_clock0)

#4 clock
def update_clock1():
    #nation
    tz_nation1 = pytz.timezone('America/Chicago')
    now1 = datetime.now(tz_nation1)

    #time
    hours1 = now1.hour
    minutes1 = now1.minute
    seconds1 = now1.second
    time_text1 = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now1.hour, now1.minute, now1.second)
    digital_clock_lbl1.config(text=time_text1)
    digital_clock_lbl1.after(1000, update_clock1)

    # updating seconds1 hand
    seconds_x1 = seconds_hand_len1 * math.sin(math.radians(seconds1 * 6)) + center_x1
    seconds_y1 = -1 * seconds_hand_len1 * math.cos(math.radians(seconds1 * 6)) + center_y1
    canvas.coords(seconds_hand1, center_x1, center_y1, seconds_x1, seconds_y1)
    # updating minutes1 hand
    minutes_x1 = minutes_hand_len1 * math.sin(math.radians(minutes1 * 6)) + center_x1
    minutes_y1 = -1 * minutes_hand_len1 * math.cos(math.radians(minutes1 * 6)) + center_y1
    canvas.coords(minutes_hand1, center_x1, center_y1, minutes_x1, minutes_y1)
    # updating hours1 hand
    hours_x1 = hours_hand_len1 * math.sin(math.radians(hours1 * 30 + 0.5 * minutes1 + 0.008 * seconds1)) + center_x1
    hours_y1 = -1 * hours_hand_len1 * math.cos(math.radians(hours1 * 30 + 0.5 * minutes1 + 0.008 * seconds1)) + center_y1
    canvas.coords(hours_hand1, center_x1, center_y1, hours_x1, hours_y1)

    window.after(1000, update_clock1)

def update_clock2():
    #nation
    tz_nation2 = pytz.timezone('Asia/Bangkok')
    now2 = datetime.now(tz_nation2)

    #time
    hours2 = now2.hour
    minutes2 = now2.minute
    seconds2 = now2.second
    time_text2 = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now2.hour, now2.minute, now2.second)
    digital_clock_lbl2.config(text=time_text2)
    digital_clock_lbl2.after(1000, update_clock2)

    # updating seconds hand
    seconds_x2 = seconds_hand_len1 * math.sin(math.radians(seconds2 * 6)) + center_x2
    seconds_y2 = -1 * seconds_hand_len1 * math.cos(math.radians(seconds2 * 6)) + center_y2
    canvas.coords(seconds_hand2, center_x2, center_y2, seconds_x2, seconds_y2)
    # updating minutes hand
    minutes_x2 = minutes_hand_len1 * math.sin(math.radians(minutes2 * 6)) + center_x2
    minutes_y2 = -1 * minutes_hand_len1 * math.cos(math.radians(minutes2 * 6)) + center_y2
    canvas.coords(minutes_hand2, center_x2, center_y2, minutes_x2, minutes_y2)
    # updating hours hand
    hours_x2 = hours_hand_len1 * math.sin(math.radians(hours2 * 30 + 0.5 * minutes2 + 0.008 * seconds2)) + center_x2
    hours_y2 = -1 * hours_hand_len1 * math.cos(math.radians(hours2 * 30 + 0.5 * minutes2 + 0.008 * seconds2)) + center_y2
    canvas.coords(hours_hand2, center_x2, center_y2, hours_x2, hours_y2)

    window.after(1000, update_clock2)

def update_clock3():
    #nation
    tz_nation3 = pytz.timezone('Canada/Mountain')
    now3 = datetime.now(tz_nation3)

    #time
    hours3 = now3.hour
    minutes3 = now3.minute
    seconds3 = now3.second
    time_text3 = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now3.hour, now3.minute, now3.second)
    digital_clock_lbl3.config(text=time_text3)
    digital_clock_lbl3.after(1000, update_clock3)

    # updating seconds hand
    seconds_x3= seconds_hand_len1 * math.sin(math.radians(seconds3 * 6)) + center_x3
    seconds_y3 = -1 * seconds_hand_len1 * math.cos(math.radians(seconds3 * 6)) + center_y3
    canvas.coords(seconds_hand3, center_x3, center_y3, seconds_x3, seconds_y3)
    # updating minutes hand
    minutes_x3 = minutes_hand_len1 * math.sin(math.radians(minutes3 * 6)) + center_x3
    minutes_y3 = -1 * minutes_hand_len1 * math.cos(math.radians(minutes3 * 6)) + center_y3
    canvas.coords(minutes_hand3, center_x3, center_y3, minutes_x3, minutes_y3)
    # updating hours hand
    hours_x3 = hours_hand_len1 * math.sin(math.radians(hours3 * 30 + 0.5 * minutes3 + 0.008 * seconds3)) + center_x3
    hours_y3 = -1 * hours_hand_len1 * math.cos(math.radians(hours3 * 30 + 0.5 * minutes3 + 0.008 * seconds3)) + center_y3
    canvas.coords(hours_hand3, center_x3, center_y3, hours_x3, hours_y3)

    window.after(1000, update_clock3)

def update_clock4():
    #nation
    tz_nation4 = pytz.timezone('Australia/West')
    now4 = datetime.now(tz_nation4)

    #time
    hours4 = now4.hour
    minutes4 = now4.minute
    seconds4 = now4.second
    time_text4 = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now4.hour, now4.minute, now4.second)
    digital_clock_lbl4.config(text=time_text4)
    digital_clock_lbl4.after(1000, update_clock4)

    # updating seconds hand
    seconds_x4= seconds_hand_len1 * math.sin(math.radians(seconds4 * 6)) + center_x4
    seconds_y4 = -1 * seconds_hand_len1 * math.cos(math.radians(seconds4 * 6)) + center_y4
    canvas.coords(seconds_hand4, center_x4, center_y4, seconds_x4, seconds_y4)
    # updating minutes hand
    minutes_x4 = minutes_hand_len1 * math.sin(math.radians(minutes4 * 6)) + center_x4
    minutes_y4 = -1 * minutes_hand_len1 * math.cos(math.radians(minutes4 * 6)) + center_y4
    canvas.coords(minutes_hand4, center_x4, center_y4, minutes_x4, minutes_y4)
    # updating hours hand
    hours_x4 = hours_hand_len1 * math.sin(math.radians(hours4 * 30 + 0.5 * minutes4 + 0.008 * seconds4)) + center_x4
    hours_y4 = -1 * hours_hand_len1 * math.cos(math.radians(hours4 * 30 + 0.5 * minutes4 + 0.008 * seconds4)) + center_y4
    canvas.coords(hours_hand4, center_x4, center_y4, hours_x4, hours_y4)

    window.after(1000, update_clock4)

def getWeather(window):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Nhiệt độ thấp nhất: " + str(min_temp) + "°C" + "\n" + "Nhiệt độ cao nhất: " + str(max_temp) + "°C" +"\n" + "Áp suất: " + str(pressure) + "\n" +"Độ ẩm: " + str(humidity) + "\n" +"Tốc độ gió: " + str(wind) + "\n" + "Bình minh: " + sunrise + "\n" + "Hoàng hôn: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)
#weather
f = ("poppins", 10, "bold")
t = ("poppins", 13, "bold")

textField = ui.Entry(window, width = 10, font = t)
textField.place(x=980, y=150)
textField.bind('<Return>', getWeather)

label2 = ui.Label(canvas, font=f)
label2.place(x=1050, y=160)
label1 = ui.Label(canvas, font=t)
label1.place(x=930, y=200)

def btcancelclick():
    exit()
    return()

def getweather1():
    city = 'Chicago'
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_data = 'America/Chicago\n' + condition + "\n" + str(temp) + "°C" + "\n"+ "Nhiệt độ thấp nhất: " + str(min_temp) + "°C" + "\n" + "Nhiệt độ cao nhất: " + str(max_temp) + "°C" +"\n" + "Áp suất: " + str(pressure) + "\n" +"Độ ẩm: " + str(humidity) + "\n" +"Tốc độ gió: " + str(wind) + "\n" + "Bình minh: " + sunrise + "\n" + "Hoàng hôn: " + sunset
    #weather
    f = ("poppins", 10, "bold")
    t = ("poppins", 13, "bold")

    label2 = ui.Label(canvas, font=f, height=10, width=19)
    label2.place(x=340, y=200)
    label2.config(text = final_data)
def getweather2():
    city = 'Bangkok'
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_data = 'Asia/Bangkok\n' + condition + "\n" + str(temp) + "°C" + "\n"+ "Nhiệt độ thấp nhất: " + str(min_temp) + "°C" + "\n" + "Nhiệt độ cao nhất: " + str(max_temp) + "°C" +"\n" + "Áp suất: " + str(pressure) + "\n" +"Độ ẩm: " + str(humidity) + "\n" +"Tốc độ gió: " + str(wind) + "\n" + "Bình minh: " + sunrise + "\n" + "Hoàng hôn: " + sunset
    #weather
    f = ("poppins", 10, "bold")
    t = ("poppins", 13, "bold")

    label2 = ui.Label(canvas, font=f, height=10, width=19)
    label2.place(x=340, y=200)
    label2.config(text = final_data)
def getweather3():
    city = 'Canada'
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_data = 'Canada/Mountain\n' + condition + "\n" + str(temp) + "°C" + "\n"+ "Nhiệt độ thấp nhất: " + str(min_temp) + "°C" + "\n" + "Nhiệt độ cao nhất: " + str(max_temp) + "°C" +"\n" + "Áp suất: " + str(pressure) + "\n" +"Độ ẩm: " + str(humidity) + "\n" +"Tốc độ gió: " + str(wind) + "\n" + "Bình minh: " + sunrise + "\n" + "Hoàng hôn: " + sunset
    #weather
    f = ("poppins", 10, "bold")
    t = ("poppins", 13, "bold")

    label2 = ui.Label(canvas, font=f, height=10, width=19)
    label2.place(x=340, y=200)
    label2.config(text = final_data)
def getweather4():
    city = 'Australia'
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_data = 'Australia/West\n' + condition + "\n" + str(temp) + "°C" + "\n"+ "Nhiệt độ thấp nhất: " + str(min_temp) + "°C" + "\n" + "Nhiệt độ cao nhất: " + str(max_temp) + "°C" +"\n" + "Áp suất: " + str(pressure) + "\n" +"Độ ẩm: " + str(humidity) + "\n" +"Tốc độ gió: " + str(wind) + "\n" + "Bình minh: " + sunrise + "\n" + "Hoàng hôn: " + sunset
    #weather
    f = ("poppins", 10, "bold")
    t = ("poppins", 13, "bold")

    label2 = ui.Label(canvas, font=f, height=10, width=19)
    label2.place(x=340, y=200)
    label2.config(text = final_data)

def btcancelclick():
    exit()
    return()

bgtrang = ui.PhotoImage(file='trang.png')
canvas.create_image(1035, 210, image=bgtrang)
bgpika = ui.PhotoImage(file='pika.png')
canvas.create_image(900, 290, image=bgpika)
canvas.create_text(1027,127, text= "THỜI TIẾT\nQUỐC GIA", font=('Helvetica','10','bold'), fill='black')

seconds_hand_len1, minutes_hand_len1, hours_hand_len1 = 47.5, 40, 30
center_x1, center_x2, center_x3, center_x4 = 200, 630, 200, 630
center_y1, center_y2, center_y3, center_y4 = 160, 160, 430, 430

bg1 = ui.PhotoImage(file='dial_400.png')
canvas.create_image(200, 160, image=bg1)
canvas.create_image(630, 160, image=bg1)
canvas.create_image(200, 430, image=bg1)
canvas.create_image(630, 430, image=bg1)
#clock 0
digital_clock_lbl0 = ui.Label(window, text="00:00:00", font=('Helvetica','15','bold'))
digital_clock_lbl0.place(x=380, y=37)
#clock 1
digital_clock_lbl1 = Button(window, text="00:00:00", font=('', 10, 'bold'), command = getweather1)
digital_clock_lbl1.place(x=170, y=250)

seconds_hand1 = canvas.create_line(200, 160, 200 + seconds_hand_len1, 160 + seconds_hand_len1, width=0.75, fill='red')
minutes_hand1 = canvas.create_line(200, 160, 200 + minutes_hand_len1, 160 + minutes_hand_len1, width=1, fill='white')
hours_hand1 = canvas.create_line(200, 160, 200 + hours_hand_len1, 160 + hours_hand_len1, width=2, fill='white')
#clock2
digital_clock_lbl2 = Button(window, text="00:00:00", font=('', 10, 'bold'), command = getweather2)
digital_clock_lbl2.place(x=600, y=250)

seconds_hand2 = canvas.create_line(630, 160, 630 + seconds_hand_len1, 160 + seconds_hand_len1, width=0.75, fill='red')
minutes_hand2 = canvas.create_line(630, 160, 630 + minutes_hand_len1, 160 + minutes_hand_len1, width=1, fill='white')
hours_hand2 = canvas.create_line(630, 160, 630 + hours_hand_len1, 160 + hours_hand_len1, width=2, fill='white')
#clock3
digital_clock_lbl3 = Button(window, text="00:00:00", font=('', 10, 'bold'), command = getweather3)
digital_clock_lbl3.place(x=170, y=525)

seconds_hand3 = canvas.create_line(200, 430, 200 + seconds_hand_len1, 430 + seconds_hand_len1, width=0.75, fill='red')
minutes_hand3 = canvas.create_line(200, 430, 200 + minutes_hand_len1, 430 + minutes_hand_len1, width=1, fill='white')
hours_hand3 = canvas.create_line(200, 430, 200 + hours_hand_len1, 430 + hours_hand_len1, width=2, fill='white')
#clock4
digital_clock_lbl4 = Button(window, text="00:00:00", font=('', 10, 'bold'), command = getweather4)
digital_clock_lbl4.place(x=600, y=525)

seconds_hand4 = canvas.create_line(630, 430, 630 + seconds_hand_len1, 430 + seconds_hand_len1, width=0.75, fill='red')
minutes_hand4 = canvas.create_line(630, 430, 630 + minutes_hand_len1, 430 + minutes_hand_len1, width=1, fill='white')
hours_hand4 = canvas.create_line(630, 430, 630 + hours_hand_len1, 430 + hours_hand_len1, width=2, fill='white')

#solve_decor:
bgtitalpika1 = ui.PhotoImage(file='tital_pikachu.png')
canvas.create_image(0, 13, image=bgtitalpika1)
canvas.create_image(0, 633, image=bgtitalpika1)
canvas.create_image(1250, 633, image=bgtitalpika1)
canvas.create_image(1250, 13, image=bgtitalpika1)

bgcanh = ui.PhotoImage(file='canhtrai.png')
canvas.create_image(71, 150, image=bgcanh)
canvas.create_image(71, 420, image=bgcanh)
canvas.create_image(501, 150, image=bgcanh)
canvas.create_image(501, 420, image=bgcanh)
bgcanh2 = ui.PhotoImage(file='canhphai.png')
canvas.create_image(330, 150, image=bgcanh2)
canvas.create_image(330, 420, image=bgcanh2)
canvas.create_image(760, 150, image=bgcanh2)
canvas.create_image(760, 420, image=bgcanh2)

bgearth = ui.PhotoImage(file='traidat.png')
canvas.create_image(1030, 470, image=bgearth)

#solve_flag():
bg11 = ui.PhotoImage(file='america.png')
canvas.create_image(200, 300, image=bg11)
bg22 = ui.PhotoImage(file='thailan.png')
canvas.create_image(630, 300, image=bg22)
bg33 = ui.PhotoImage(file='canada.png')
canvas.create_image(200, 570, image=bg33)
bg44 = ui.PhotoImage(file='australia.png')
canvas.create_image(630, 570, image=bg44)

#Combobox
combo = combo.Combobox(window, font = ('Times New Roman',14), width=16)
combo['value'] = (
'Antarctica/Casey',
'Atlantic/Stanley',
'Australia/Yancowinna',
'Brazil/Acre',
'Canada/Atlantic',
'Europe/Zagreb',)
combo.current(0)
combo.place(x = 340, y = 70)

#time solve
update_clock0()
update_clock1()
update_clock2()
update_clock3()
update_clock4()

#Button Cancel
bt = Button(window, text='Thoát', command=btcancelclick, width=10)
bt.place(x=1050, y=600)

#create
canvas.pack()
window.mainloop()