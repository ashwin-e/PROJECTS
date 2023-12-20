from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("weather app")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="current weather")
        #weather

        api= "https://api.openweathermap.org/data/2.5/weather?lat=" + str(location.latitude) + "&lon=" + str(location.longitude) + "&appid=9ce6d89f83a1bdcfd84e504ef777187e"

        json_data=requests.get(api).json()
        condition=json_data["weather"][0]["main"]
        description=json_data["weather"][0]["description"]
        temp=int(json_data["main"]["temp"]-273.15)
        pressure=(json_data["main"]["pressure"])
        humidity=json_data["main"]["humidity"]
        wind=json_data['wind']["speed"]

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","feels","like",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        c.config(text=description)
        m.config(text=pressure)
    except Exception as e:
        messagebox.showerror()("weather app", "invalid Entry!!")









#search box
Search_image=PhotoImage(file="ser.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()
 
Search_icon=PhotoImage(file="sericon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="lo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#bottom box
frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)



#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)
#label

label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

# Label 2
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=225, y=400)

# Label 3
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

# Label 4
label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
c=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
c.place(x=450,y=430)
m=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
m.place(x=670,y=430)



root.mainloop()