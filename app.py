from tkinter import *
from functools import partial
import ttkbootstrap as tb
import json
import os.path
from person import PeopleMatrix
import random
from time import time

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Multipages")
        self.master.geometry("500x350")
        if os.path.exists('./people.json'):
            self.people = self.load_people()
        else:
            self.people = PeopleMatrix([])
        self.home()

    def home(self):
        self.clearscr()
        page = self.create_page()
        title = tb.Label(page, text="Partner Combinator", font=("Calibri", 14), bootstyle="Default")
        title.grid(row=0, column=0, pady=5, sticky='ew')
        btn1 = tb.Button(page, text="Add People", command=self.add_people_pg)
        btn1.grid(row=1, column=0, pady=5, sticky='ew')
        btn2 = tb.Button(page, text="Delete People")
        btn2.grid(row=2, column=0, pady=5, sticky='ew')
        btn3 = tb.Button(page, text="Edit Partners")
        btn3.grid(row=3, column=0, pady=5, sticky='ew')
        btn4 = tb.Button(page, text="Create Prayer Partners")
        btn4.grid(row=4, column=0, pady=5, sticky='ew')
        btn5 = tb.Button(page, text="View Matrix")
        btn5.grid(row=5, column=0, pady=5, sticky='ew')
        btn6 = tb.Button(page, text="Exit", command=self.exit_app)
        btn6.grid(row=6, column=0, pady=5, sticky='ew')

    def add_people_pg(self):
        self.clearscr()
        page = self.create_page()
        title = tb.Label(page, text="Add People", font=("Calibri", 18), bootstyle="Default")
        title.grid(row=0, column=0, pady=5)

        name = tb.Entry(page, bootstyle="Dark")
        name.grid(row=1, column=0, pady=5)

        enterbtn = tb.Button(page, text="Enter Person", command=partial(self.add_person, name))
        enterbtn.grid(row=2, column=0, pady=5, sticky='ew')

        returnbtn = tb.Button(page, text="Return", command=self.home)
        returnbtn.grid(row=3, column=0, pady=5, sticky='ew')
    
    def add_person(self, name):
        self.people.add_person(name.get())
        name.delete(0, END)

    
    def clearscr(self):
        for i in self.master.winfo_children():
            i.destroy()
    def create_page(self):
        page = Frame(self.master, width=500, height=350)
        page.pack()
        return page
    
    def load_people(self):
        with open('people.json', 'r') as json_file:
            json_data = json.load(json_file)
        people = PeopleMatrix(json_data[0], json_data[1])
        return people

    def save_people(self):
        json_data = [self.people.get_names(), self.people.get_matrix()]
        json_object = json.dumps(json_data, indent=4)
        with open("people.json", 'w') as json_file:
            json_file.write(json_object)

    def exit_app(self):
        self.master.destroy()
