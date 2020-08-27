from mylib.menus import *
import os
while True:
    os.system("cls")
    x=main_menu()
    if x=='1':
        os.system("cls")
        registration()
        input("Press any key to continue....")
    elif x=='2':
        os.system("cls")
        search_stu()
        input("Press any key to continue....")
    elif x=='3':
        os.system("cls")
        issue_tc()
        input("Press any key to continue....")
    elif x=='4':
        os.system("cls")
        disp_tc()
        input("Press any key to continue....")
    elif x=='5':
        os.system("cls")
        display()
        input("Press any key to continue....")
    elif x=='6':
        print("THANK YOU !!")
        break

