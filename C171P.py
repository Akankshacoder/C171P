from tkinter import *
from PIL import ImageTk, Image
import pytz
from datetime import datetime
root = Tk()
root.title("World Time")
root.geometry("1000x1000")

class India:
    def __init__(self, master):
        self.master = master
        self.india_image = ImageTk.PhotoImage(Image.open("india.jpg"))
        self.india_map = Label(self.master, image=self.india_image)
        self.india_map.place(relx=0.05, rely=0.1)
        self.india_label = Label(self.master, text="India")
        self.india_label.place(relx=0.05, rely=0.7)
        self.india_time = Label(self.master, text="")
        self.india_time.place(relx=0.05, rely=0.8)

class USA:
    def __init__(self, master):
        self.master = master
        self.usa_image = ImageTk.PhotoImage(Image.open("usa.jpg"))
        self.usa_map = Label(self.master, image=self.usa_image)
        self.usa_map.place(relx=0.35, rely=0.1)
        self.usa_label = Label(self.master, text="USA")
        self.usa_label.place(relx=0.35, rely=0.7)
        self.usa_time = Label(self.master, text="")
        self.usa_time.place(relx=0.35, rely=0.8)

class Australia:
    def __init__(self, master):
        self.master = master
        self.australia_image = ImageTk.PhotoImage(Image.open("australia.jpg"))
        self.australia_label = Label(self.master, text="Australia")
        self.australia_label.place(relx=0.05, rely=0.7)
        self.australia_map = Label(self.master, image=self.australia_image)
        self.australia_map.place(relx=0.05, rely=0.1)
        self.australia_time = Label(self.master, text="")
        self.australia_time.place(relx=0.05, rely=0.8)

    def times(self):
        australia_timezone = pytz.timezone('Australia/ACT')
        australia_time = datetime.now(australia_timezone).strftime('%Y-%m-%d %H:%M:%S')
        self.australia_time.config(text="Time: " + australia_time)

class Japan:
    def __init__(self, master):
        self.master = master
        self.japan_image = ImageTk.PhotoImage(Image.open("japan.jpg"))
        self.japan_label = Label(self.master, text="Japan")
        self.japan_label.place(relx=0.35, rely=0.7)
        self.japan_map = Label(self.master, image=self.japan_image)
        self.japan_map.place(relx=0.35, rely=0.1)
        self.japan_time = Label(self.master, text="")
        self.japan_time.place(relx=0.35, rely=0.8)

    def times(self):
        japan_timezone = pytz.timezone('Japan')
        japan_time = datetime.now(japan_timezone).strftime('%Y-%m-%d %H:%M:%S')
        self.japan_time.config(text="Time: " + japan_time)



india_clock = India(root)
usa_clock = USA(root)
australia_clock = Australia(root)
japan_clock = Japan(root)

australia_button = Button(root, text="Show Time", command=australia_clock.times)
australia_button.place(relx=0.05, rely=0.9)

japan_button = Button(root, text="Show Time", command=japan_clock.times)
japan_button.place(relx=0.35, rely=0.9)

root.mainloop()
