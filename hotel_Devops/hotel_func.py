class hotels():

    # option-1
    def find_free_rooms():
        room1 = open("C:/Users/LapTop/Desktop/hotel/room1.txt", "r")
        room2 = open("C:/Users/LapTop/Desktop/hotel/room1.txt", "r")
        room3 = open("C:/Users/LapTop/Desktop/hotel/room1.txt", "r")
        room4 = open("C:/Users/LapTop/Desktop/hotel/room1.txt", "r")
        print("\nfor room1 with 2 adults:\n" + str(room1.read()))
        print("\nfor room2 with 2 adults:\n" + str(room2.read()))
        print("\nfor room3 with 3 adults:\n" + str(room3.read()))
        print("\nfor room4 with 3 adults:\n" + str(room4.read()))
        room1.close()
        room2.close()
        room3.close()
        room4.close()

    # option-2

    def invitation():
        date = input("enter date: ")
        days = input("enter how many days: ")
        boolean = 0
        while boolean == 0:
            adults = int(input("enter number of adults: "))
            if adults == 2:
                ##################
                boolean = 1
            elif adults == 3:
                ####################
                boolean = 1
            else:
                print("Enter how many adults (2-3)")







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


