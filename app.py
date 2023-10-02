from tkinter import *
from functools import partial
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
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
        btn2 = tb.Button(page, text="Delete People", command=self.delete_people_pg)
        btn2.grid(row=2, column=0, pady=5, sticky='ew')
        btn3 = tb.Button(page, text="Edit Partners", command=self.edit_partners_pg)
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

        entertext = tb.Label(page, font=("Calibri", 16), bootstyle="success")
        entertext.grid(row=1, column=1, pady=5, padx=10)

        enterbtn = tb.Button(page, text="Enter Person", command=partial(self.add_person, name, entertext))
        enterbtn.grid(row=2, column=0, pady=5, sticky='ew')

        returnbtn = tb.Button(page, text="Return", command=self.home)
        returnbtn.grid(row=3, column=0, pady=5, sticky='ew')
    
    def add_person(self, name, text):
        self.people.add_person(name.get())
        text.config(text=f"Added {name.get()}")
        name.delete(0, END)

    def delete_people_pg(self):
        self.clearscr()
        page = self.create_page()
        title = tb.Label(page, text="Delete_People", font=("Calibri", 18), bootstyle="Default")
        title.pack(pady=5)

        people_frame = ScrolledFrame(page, autohide=False, bootstyle="default, rounded")
        people_frame.pack(pady=15, padx=15, fill=BOTH, expand=YES)

        i=0
        for person in self.people.get_names():
            tmp_label = tb.Label(people_frame, text=person, font=("Calibri", 14), bootstyle="Default")
            tmp_label.grid(row=i, column=0, pady=5, padx=10, sticky='ew')
            tmp_button = tb.Button(people_frame, text="Delete", bootstyle="Danger, outline")
            tmp_button.grid(row=i, column=1, pady=5, padx=10, sticky='ew')
            tmp_button.config(command=partial(self.delete_person, person, tmp_label, tmp_button))
            i += 1

        returnbtn = tb.Button(page, text="Return", command=self.home)
        returnbtn.pack(pady=10)

    def delete_person(self, name, l, btn):
        self.people.remove_person(name)
        l.destroy()
        btn.destroy()
    
    def edit_partners_pg(self):
        self.clearscr()
        page = self.create_page()
        title = tb.Label(page, text="Delete_People", font=("Calibri", 18), bootstyle="Default")
        title.pack(pady=5)

        people_frame = ScrolledFrame(page, autohide=False, bootstyle="default, rounded")
        people_frame.pack(pady=15, padx=15, fill=BOTH, expand=YES)

        i=0
        for person in self.people.get_names():
            j=0
            tmp_label = tb.Label(people_frame, text=person, font=("Calibri", 14), bootstyle="Default")
            tmp_label.grid(row=i, column=0, pady=5, padx=10, sticky='ew')
            for partner in self.people.get_names():
                if person != partner:
                    tmp_button = tb.Button(people_frame, text=partner, bootstyle="info, outline")
                    tmp_button.grid(row=i, column=j, pady=5, padx=5, sticky='ew')
                    tmp_button.config(command=partial(self.delete_person, person, tmp_label, tmp_button))
                j += 1
            i += 1

        returnbtn = tb.Button(page, text="Return", command=self.home)
        returnbtn.pack(pady=10)
    
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
