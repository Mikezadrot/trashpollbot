# -*- coding: utf-8 -*-
import json


def create_element():
    elem = {"Id_elements": int(input("Input you Id question\n")),
               "Chat_ID": input("Input you Chat ID\n"),
               "Question": input("Input you question\n"),
               "Answer": input("Input you  answers\n").split('.'),
               "Hour": int(input("Input hour\n")),
               "Minutes": int(input("Input minutes\n"))}
    return elem


def writing_in_file(our_mass):
    with open("data.json", "w") as outfile:
        json.dump(our_mass, outfile)
        outfile.write("\n")


def adding_in_file():
    open_date = []
    with open("data.json", "r") as infile:
        data = json.load(infile)

        for elm in data:
            open_date.append(elm)
        print(open_date)
    elem = create_element()
    elem["Answer"].pop(len(elem["Answer"]) - 1)
    if any(d["Id_elements"] == elem["Id_elements"] for d in open_date):
        print("Try create new or input add")
    else:
        open_date.append(elem)
    writing_in_file(open_date)
    return open_date


def reading_file():
    with open("data.json", "r") as infile:
        data = json.load(infile)
    i = 1
    for chat in data:
        print(i)
        print(chat)
        i += 1


# adding_in_file()
mass = []
Main_mass = []
lis = []

while True:
    nu21 = input("Input number 1 for writing or 2 for reading or ex to exit (help)  \n")
    if nu21 == '1':
        element = create_element()
        element["Answer"].pop(len(element["Answer"])-1)
        print(element)
        if any(d["Id_elements"] == element["Id_elements"] for d in mass):
            print("Try create new or input add")
        else:
            mass.append(element)
        # print(mass)
        writing_in_file(mass)
    if nu21 == "2":
        reading_file()
    if nu21 == "3":
        adding_in_file()
    if nu21 == "help":
        print("Input 1-writing file\n","Input 2-reading file\n","Input 3-adding file\n","Input ex-stop prog\n","Input help-reading info\n")
    if nu21 == 'ex':
        break
