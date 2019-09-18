import datetime

class hotels():

    # option-1
    def find_free_rooms():
        room1 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room1.txt", "r")
        room2 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room2.txt", "r")
        room3 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room3.txt", "r")
        room4 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room4.txt", "r")
        print("\nfor room1 with 2 adults:\n" + str(room1.read()))
        print("\nfor room2 with 2 adults:\n" + str(room2.read()))
        print("\nfor room3 with 3 adults:\n" + str(room3.read()))
        print("\nfor room4 with 3 adults:\n" + str(room4.read()))
        room1.close()
        room2.close()
        room3.close()
        room4.close()

    # option-2

    def searchdate():
        date_array = input("enter date: (year-day-month)").split("-")
        if len(date_array) == 3:
            date = str(datetime.date(int(date_array[0]), int(date_array[1]), int(date_array[2])))
            print(date)
        days = input("enter how many days: ")
        boolean = 0
        while boolean == 0:
            adults = int(input("enter number of adults: (2/3)"))
            if adults == 2:
                room1 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room1.txt", "r")
                room2 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room2.txt", "r")
                room1_list = list(room1.read().splitlines())
                room2_list = list(room2.read().splitlines())

                if date in room1_list:
                    print("you can invite " + str(days) + " days from " + str(date) + " for " + str(
                        adults) + " adults in room 1")
                else:
                    print("This date is full for room1")
                if date in room2_list:
                    print("you can invite " + str(days) + " days from " + str(date) + " for " + str(
                        adults) + " adults in room2")
                else:
                    print("This date is full for room2")

                boolean = 1
            elif adults == 3:
                room3 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room1.txt", "r")
                room4 = open("C:/Users/LapTop/PycharmProjects/HotelMenu/Files/room2.txt", "r")

                room3_list = list(room3.read().splitlines())
                room4_list = list(room4.read().splitlines())
                if date in room3_list:
                    print("you can invite " + str(days) + " days from " + str(date) + " for " + str(
                        adults) + " adults in room3")
                else:
                    print("This date is full for room3")

                if date in room4_list:
                    print("you can invite " + str(days) + " days from " + str(date) + " for " + str(
                        adults) + " adults in room4")
                else:
                    print("This date is full for room4")

                boolean = 1

            else:
                print("Invalid input!, try again.")







    # print('''
           #  welcome to Net4U Hotel!
           #
           #  Menu:
           #
           #  1) חיפוש תאריכים פנויים לפי מס מבוגרים ותאריך
           #  2) מכניס את כמות האנשים ותאריך ומקבל תשובה מה פנוי
           #  3) ביצוע הזמנה,לעשות קנייה חישוב עלות הכנסת פרטים אישיים
           #  4) בוטול הזמנה קיימת ומחייב בכנס של 10%
           #  5) הוספת חדרים או ימים להזמנה קיימת
           #  6) חיפוש הזמנה קיימת
           #  ''')
           #


