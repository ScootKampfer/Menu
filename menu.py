def switch(ToDo):

    if ToDo == "view menu":

        return menu
    
    elif ToDo == "add item":

        NewMenuItem = input("What is the name of the new menu item? ")
        NewMenuPrice = format(float(input(f"And what is the price of a {NewMenuItem} in dollars? ")), ".2f") + "$"
        menu[NewMenuItem] = NewMenuPrice
        return menu
    
    elif ToDo == "remove item":

        Removal = input("What is the name of the menu item you wish to be removed? ")
        del menu[Removal]
        return menu
    
    elif ToDo == "save and quit":

        f = open("menu.txt", "w")
        f.write(str(menu))
        print("Your menu has been saved")
        f.close()
        exit()
        return menu
    

menu = {}

while True:

    action = input("Enter action to do here: ")
    print(switch(action))