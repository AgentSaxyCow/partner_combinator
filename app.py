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
        self.master.geometry("800x800")
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
        btn4 = tb.Button(page, text="Create Prayer Partners", command=self.create_partners_pg)
        btn4.grid(row=4, column=0, pady=5, sticky='ew')
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
        page = Frame(self.master, width=300, height=300)
        page.pack(fill='y', expand=True)
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
        page = Frame(self.master, width=300, height=300)
        page.pack(fill='both', expand=True)
        title = tb.Label(page, text="Delete_People", font=("Calibri", 18), bootstyle="Default")
        title.pack(pady=5)

        people_frame = ScrolledFrame(page, autohide=False, bootstyle="default, rounded")
        people_frame.pack(pady=15, padx=15, fill=BOTH, expand=True)

        btn_list = []
        for i in range(len(self.people.get_names())):
            tb.Label(people_frame, text=self.people.get_names()[i], bootstyle="default").grid(row=0, column=i+1, pady=5, padx=5)
            tb.Label(people_frame, text=self.people.get_names()[i], bootstyle="default").grid(row=i+1, column=0, pady=5, padx=5)
            btn_list.append([])
            for j in range(len(self.people.get_names())):
                tmpvar = IntVar()
                tmpbtn = Checkbutton(people_frame, variable=tmpvar, onvalue=1, offvalue=0)
                btn_list[i].append([tmpbtn, tmpvar])
                tmpbtn.grid(row=i+1, column=j+1, pady=5, padx=5)

        names = self.people.get_names()
        matrix = self.people.get_matrix()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    btn_list[i][j][0].select()

        for i in range(len(btn_list)):
            for j in range(len(btn_list)):
                if i==j:
                    btn_list[i][j][0].destroy()
                else:
                    btn_list[i][j][0].config(command=partial(self.update_partners, btn_list[j][i][0], btn_list[i][j][1], names[i], names[j]))
        
        clearbtn = tb.Button(page, text="Clear", command=partial(self.clearbtns, btn_list))
        clearbtn.pack(pady=5, side='bottom', fill='x')

        returnbtn = tb.Button(page, text="Return", command=self.savereturn)
        returnbtn.pack(pady=5, side='top', fill='x')
    def clearbtns(self, btn_list):
        for i in range(len(btn_list)):
            for j in range(len(btn_list)):
                if i != j:
                    btn_list[i][j][0].deselect()
                    self.people.remove_all_partners()
    def savereturn(self):
        self.save_people()
        self.home()
    
    def update_partners(self, btn, btn_var, n1, n2):
        btn.toggle()
        if btn_var.get() == 0:
            self.people.remove_partners(n1, n2)
        else:
            self.people.add_partners(n1, n2)
    
    def create_partners_pg(self):
        self.clearscr()
        page = self.create_page()
        self.create_partners(page)
        returnbtn = tb.Button(page, text="Return", command=self.home)
        returnbtn.pack(pady=10)
    
    def create_partners(self, page):
        available_partners = []
        for name in self.people.get_names():
            available_partners.append(name)
        random.seed(time())

        while len(available_partners) > 3 or len(available_partners) == 2:
            person = available_partners[0]

            for x in available_partners:
                if self.people.get_partners_count(x) > self.people.get_partners_count(person):
                    person = x
            
            available_partners.remove(person)

            not_partners = self.people.get_not_partners(person)
            tmp = []
            for name in available_partners:
                if name in not_partners:
                    tmp.append(name)
            if len(tmp) == 0:
                partner = random.choice(available_partners)
            else:
                partner = random.choice(tmp)

            available_partners.remove(partner)
            tb.Label(page, text=f"{person} <-> {partner}", font=("Calibri", 14), bootstyle="default").pack(pady=10)

            self.people.add_partners(person, partner)
        
        if len(available_partners) == 3:
            tb.Label(page, text=f"{available_partners[0]} <-> {available_partners[1]} <-> {available_partners[2]}", font=("Calibri", 14), bootstyle="default").pack(pady=10)
            self.people.add_partners(available_partners[0], available_partners[1])
            self.people.add_partners(available_partners[0], available_partners[2])
            self.people.add_partners(available_partners[1], available_partners[2])
    
    def clearscr(self):
        for i in self.master.winfo_children():
            i.destroy()
    def create_page(self):
        page = Frame(self.master, width=300, height=300)
        page.pack(expand=False)
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
        self.save_people()
        self.master.destroy()
