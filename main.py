from tkinter import*
from  tkinter import ttk
import requests

def data_get():
    city=city_name.get()



    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=54d795ce90c53603273691e29a95f7cd").json()
    w1_label.config(text=data["weather"][0]["main"])
    wb1_label.config(text=data["weather"][0]["description"])
    temp1_label.config(text= str(int(data["main"]["temp"]-273.15)))
    pr1_label.config(text=data["main"]["pressure"])


win=Tk()
win.title("Weather")
win.config(bg= "blue" )
win.geometry('500x570')
name_label=Label(win,text=" My Weather App",
                 font=("Time New Roman",40,"bold"))
name_label.place(x=25 , y=50, height=50,width=450)
city_name= StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


com=ttk.Combobox(win,text=" My Weather App",values=list_name,
                 font=("Time New Roman",30,"bold"),textvariable=city_name)
com.place(x=25 , y=140, height=50,width=450)

w_label=Label(win,text=" Weather climate",
                 font=("Time New Roman",17))
w_label.place(x=25 , y=270, height=50,width=160)

w1_label=Label(win,text=" ",
                 font=("Time New Roman",17))
w1_label.place(x=240 , y=270, height=50,width=160)

wb_label=Label(win,text=" Weather Description",
                 font=("Time New Roman",17))
wb_label.place(x=25 , y=335, height=50,width=160)

wb1_label=Label(win,text="",
                 font=("Time New Roman",17))
wb1_label.place(x=240 , y=335, height=50,width=160)

temp_label=Label(win,text=" Temperature",
                 font=("Time New Roman",17))
temp_label.place(x=25 , y=400, height=50,width=160)

temp1_label=Label(win,text="",
                 font=("Time New Roman",17))
temp1_label.place(x=240, y=400, height=50,width=160)

pr_label=Label(win,text=" Pressure",
                 font=("Time New Roman",17))
pr_label.place(x=25 , y=470, height=50,width=160)

pr1_label=Label(win,text="",
                 font=("Time New Roman",17))
pr1_label.place(x=240 , y=470, height=50,width=160)

done_button=Button(win,text="Done",
                 font=("Time New Roman",30,"bold"),command=data_get)
done_button.place(x=200 , y=210, height=50,width=100 )

win.mainloop()
