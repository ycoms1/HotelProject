from hotel_Devops.hotel_func import *

def menu():
    boolean = 0
    while boolean == 0:
        choise = input(
            "Menu:\n1.search for avilable rooms\n2.search for specific date\n3.invitation\n"
            "4.cancel order\n5.add days/rooms\n6.search for invitation\n")
        if choise == "1":
            hotels.find_free_rooms()
            boolean = 1
        elif choise == "2":
            hotels.invitation()
            boolean = 1
        elif choise == "3":
            print("3")
            boolean = 1
        elif choise == "4":
            print("4")
            boolean = 1
        elif choise == "5":
            print("5")
            boolean = 1
        elif choise == "6":
            print("6")
            boolean = 1
        else:
            print("Enter 1-6 only!")






