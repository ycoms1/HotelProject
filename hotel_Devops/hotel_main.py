from hotel_Devops.hotel_func import *
from hotel_Devops.functions import menu

print("Welcome to NET4U Hotel:")


menu()

while True:
    boolean = input("You want to finish or go back to menu? - 1-finish/2-menu")
    if boolean == "1":
        break
    elif boolean == "2":
        menu()
    else:
        print("Enter only 1-2!!!")


