import json
import os.path
from person import PeopleMatrix
import random
from time import time

from tkinter import *
import ttkbootstrap as tb
from app import App


def main():
    root = tb.Window(themename="superhero")
    App(root)
    root.mainloop()
    # main menu
    #while True:
    #    print("person_combinator:")
    #    print("1. Add People")
    #    print("2. Delete Person")
    #    print("3. Fill Previous Partners")
    #    print("4. Create Prayer Partners")
    #    print("5. Clear all partners")
    #    print("6. Print people")
    #    print("7. Exit")
    #    choice = input("Please select one of the above [1-6]: ")
    #    if choice == '1':
    #        create_matrix(people)
    #    elif choice == '2':
    #        delete_person(people)
    #    elif choice == '3':
    #        fill_partners(people)
    #    elif choice == '4':
    #        create_partners(people)
    #    elif choice == '5':
    #        people.remove_all_partners()
    #    elif choice == '6':
    #        people.print_matrix()
    #    elif choice == '7':
    #        break
    #save_people(people)


def create_matrix(p):
    name = input("Name: ")
    while name not in ['q', '']:
        p.add_person(name)
        name = input("Name: ")

def delete_person(p):
    i = 0
    for person in p.get_names():
        print(f"{i+1}. {person}")
        i += 1
    num = int(input("Which do you want to delete?: "))
    while (num != -1) and (num > i and i < 0):
        num = int(input("Wrong input, try again: "))
    if num != -1:
        p.remove_person(p.get_names()[num-1])

def fill_partners(p):
    names = p.get_names()
    matrix = p.get_matrix()
    for i in range(len(names)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0 and i != j and matrix[i][j] != -1:
                ans = input(f"Did {names[i]} partner with {names[j]}?(y/n): ")
                ans = ans.lower()
                if ans == 'y':
                    p.add_partners(names[i], names[j])
                else:
                    p.not_partners(names[i], names[j])
    p.clean_matrix()
            
def create_partners(people):
    available_partners = []
    for name in people.get_names():
        available_partners.append(name)
    random.seed(time())

    while len(available_partners) > 3 or len(available_partners) == 2:
        person = available_partners[0]

        for x in available_partners:
            if people.get_partners_count(x) > people.get_partners_count(person):
                person = x
        
        available_partners.remove(person)

        not_partners = people.get_not_partners(person)
        tmp = []
        for name in available_partners:
            if name in not_partners:
                tmp.append(name)
        print(not_partners)
        print(available_partners)    
        print(tmp)
        partner = random.choice(tmp)

        #print(partner)
        #print(available_partners)
        #print(tmp)
        available_partners.remove(partner)
        
        print(f"{person} <-> {partner}")

        people.add_partners(person, partner)
    
    if len(available_partners) == 3:
        print(f"{available_partners[0]} <-> {available_partners[1]} <-> {available_partners[2]}")
        people.add_partners(available_partners[0], available_partners[1])
        people.add_partners(available_partners[0], available_partners[2])
        people.add_partners(available_partners[1], available_partners[2])

if __name__=="__main__":
    main()