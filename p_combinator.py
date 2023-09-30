import json
import os.path
from person import PeopleMatrix
import random
from time import time
# person: name, previous_partners

def main():
    if os.path.exists('./people.json'):
        people = load_people()
    else:
        people = []
    # main menu
    while True:
        print("person_combinator:")
        print("1. create new person")
        print("2. delete person")
        print("3. Create Prayer Partners")
        print("4. Exit")
        print("5. Print people")
        print("6. Clear all partners")
        choice = input("Please select one of the above [1-4]: ")
        if choice == '1':
            create_person(people)
        elif choice == '2':
            delete_person(people)
        elif choice == '3':
            create_partners(people)
        elif choice == '4':
            break
        elif choice == '5':
            for p in people:
                print(p.get_name())
        elif choice == '6':
            for p in people:
                p.clear_partners()
    save_people(people)

def load_people():
    with open('people.json', 'r') as json_file:
        json_data = json.load(json_file)
    people = PeopleMatrix(json_data[0], json_data[1])
    return people

def save_people(p):
    json_data = [p.get_names(), p.get_matrix()]
    json_object = json.dumps(json_data, indent=4)
    with open("people.json", 'w') as json_file:
        json_file.write(json_object)

def create_person(p):
    name = input("Name: ")
    partners = []
    i = 1
    part = input(f"Partner {i}: ")
    while part not in ['', 'q']:
        partners.append(part)
        i += 1
        part = input(f"Partner {i}: ")
    p.append(PersonNode(name, partners)) 

def delete_person(p):
    i = 0
    for person in p:
        print(f"{i+1}. {person.get_name()}")
        i += 1
    num = int(input("Which do you want to delete?: "))
    p.pop(num-1)
            
def create_partners(people):
    available_partners = []
    for p in people:
        available_partners.append(p)
    random.seed(time())

    while len(available_partners) > 3 or len(available_partners) == 2:
        person = available_partners[0]

        for x in available_partners:
            if len(person.get_partners()) < len(x.get_partners()):
                person = x
        
        available_partners.remove(person)

        tmp = fill_tmp(available_partners, person)

        partner = random.choice(tmp)
        available_partners.remove(partner)
        
        print(f"{person.get_name()} <-> {partner.get_name()}")

        person.add_partner(partner.get_name())
        partner.add_partner(person.get_name())
    
    if len(available_partners) == 3:
        print(f"{available_partners[0].get_name()} <-> {available_partners[1].get_name()} <-> {available_partners[2].get_name()}")
        available_partners[0].add_partner(available_partners[1].get_name())
        available_partners[0].add_partner(available_partners[2].get_name())

        available_partners[1].add_partner(available_partners[0].get_name())
        available_partners[1].add_partner(available_partners[2].get_name())

        available_partners[2].add_partner(available_partners[0].get_name())
        available_partners[2].add_partner(available_partners[1].get_name())

def fill_tmp(available_partners, person):
    tmp = []
    for p in available_partners:
        if p.get_name() not in person.get_partners():
            tmp.append(p)
    if len(tmp) == 0:
        person.clear_partners()
        tmp = fill_tmp(available_partners, person)
    return tmp

if __name__=="__main__":
    main()