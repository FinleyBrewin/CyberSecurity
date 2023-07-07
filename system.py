import sys, time
import random
import os
import datetime

import bcrypt

#A function which creates a centered menu
#where args0 is the header, and the rest menu options
def menuCreator(*args):
    menu = ["~" * 48]

    #Add each args to menu
    for x in args:
        menu.append(x)

    #For each menu item, center them
    for x in range(len(menu)):
        menu[x] = menu[x].center(48, ' ')

    #Displaying menus
    os.system(clr)
    #Sets up headers and ~
    print('', menu[0], "\n",
          menu[1], "\n",
          menu[0], "\n")

    #Sets up menu selection
    for x in range(len(args)-1):
        print(menu[x+2])
        print("\n")

    return menu
          
def mainMenu(check):
    #This changes the terminal size (W, L)
    os.system('mode 50,20')

    #Checks if user needs to login or set-up login
    if check == True:
        menu = menuCreator("Password Manager", "1. Login", "2. Exit")
    else:
        menu = menuCreator("Password Manager", "1. Set-Up Password", "2. Exit")

    #Try except to only allow the correct menu selection
    try:
        menuInput = int(input(" Menu Selection: "))
    except ValueError:
        print(" Error, please try again...")
        time.sleep(2)
        mainMenu(check)
    else:
        #Directs user to the selected menu's function
        if menuInput == 1:
            if check == True:
                login()
            else:
                setUp()
        elif menuInput ==2:
            print("\n Shutting down...")
            time.sleep(2)
            exit()
        else:
            print(" Error, please try again...")
            time.sleep(2)
            mainMenu(check)

def login():

    def passwordManager():

        def addPass():
            menuCreator("Add Password")

        def viewPass():
            menuCreator("View Passwords")

        def delPass():
            menuCreator("Remove a Password")

        menuCreator("Password Manager", "1. Add Password",
                    "2. View Passwords", "3. Remove Passwords",
                    "4. Exit")

        try:
            menuInput = int(input(" Menu Selection: "))
        except ValueError:
            print(" Error, please try again...")
            time.sleep(2)
            passwordManager()
        else:
            if menuInput == 1:
                addPass()
            elif menuInput == 2:
                viewPass()
            elif menuInput == 3:
                delPass()
            elif menuInput == 4:
                print("\n Shutting down...")
                time.sleep(2)
                exit()
            else:
                print(" Error, please try again...")
                time.sleep(2)
                passwordManager()
                
            time.sleep(5)

    menuCreator("Login")
    password = input(" Please enter your master password: ").encode()

    f = open("login.txt", "rb")
    
    #bcrypt salt is first in a hash (needed to hash entered password)
    salt = f.read(29)
    f.read(1) #Skip \n
    #salt + hashed password
    hashed = f.read(61)

    hashVal = bcrypt.hashpw(password, salt)
    
    if hashVal == hashed:
        print("\n Success! Logging in...")
        time.sleep(2)
        passwordManager()
        
    else:
        print("\n Incorrect... Try again!")
        time.sleep(2)
        os.system(clr)
        login()
              
def setUp():

    menuCreator("Password Set-Up")
    password = input(" Please enter a secure master password\n Don't forget it!\n\n Password: ").encode()

    print("\n Hashing your password...")

    #salt randomly generated, rounds can be changed (saved in salt)
    salt = bcrypt.gensalt(rounds=16)
    hashVal = bcrypt.hashpw(password, salt)

    f = open("login.txt", "wb")
    f.write(salt)
    f.write("\n".encode())
    f.write(hashVal)

    f.close()

    print("\n Done! Returning to menu...")
    time.sleep(2)

    os.system(clr)
    mainMenu(True)   

#--Start of program--
    
#Terminal settings for each OS
if sys.platform == "win32":
    clr = "cls"
else:
    clr = "clear"

#If the path exists, check if it follows byte format
if os.path.exists("login.txt"):
    
    f = open("login.txt", "rb")
    checkFile = f.read(1)
    checkFile = str(checkFile)

    try:
        if checkFile == "b'$'":
            check = True
        else:
            check = False
    except IndexError:
        check = False
        
#Else, create the text file.
else:
    f = open("login.txt", "w")
    check = False

f.close()

#Starting main program.
mainMenu(check)




