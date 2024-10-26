def reading():
    
    PreviousMenu = eval(open('menu.txt', 'r').read())
    return PreviousMenu

def writemenu():

    try: 
        geeky_file= open('menu.txt', 'wt') 
        geeky_file.write(str(menu)) 
        geeky_file.close() 
  
    except: 
        print("Unable to write to file")


def switch(ToDo):

    if ToDo == "view menu":

        return menu
    
    elif ToDo == "add item":

        NewMenuItem = input("What is the name of the new menu item? ")
        NewMenuPrice = "$" + format(float(input(f"And what is the price of a {NewMenuItem} in dollars? ")), ".2f")
        menu[NewMenuItem] = NewMenuPrice
        writemenu()
        return menu
    
    elif ToDo == "remove item":

        Removal = input("What is the name of the menu item you wish to be removed? ")
        del menu[Removal]
        writemenu(menu)
        return menu
    
    elif ToDo == "save and quit":

        writemenu()
        print("Your menu has been saved")
        exit()
        return menu

while True:
    
    menu = reading()
    action = input("Enter action to do here: ")
    print(switch(action))