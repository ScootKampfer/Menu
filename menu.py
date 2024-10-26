def reading():
    
    PreviousMenu = eval(open('menu.txt', 'r').read())
    return PreviousMenu

def writemenu():

        FutureMenu = open('menu.txt', 'wt') 
        FutureMenu.write(str(menu)) 
        FutureMenu.close() 

def security():
     
     attempt = input("Please input your password to gain access to admin privileges: ")
     if attempt != password:

          print('Your password was incorrect')
          exit()

def switch(ToDo):

    if ToDo == "view menu":

        return menu
    
    elif ToDo == "add item":

        security()
        NewMenuItem = input("What is the name of the new menu item? ")
        NewMenuPrice = "$" + format(float(input(f"And what is the price of a {NewMenuItem} in dollars? ")), ".2f")
        menu[NewMenuItem] = NewMenuPrice
        writemenu()
        return menu
    
    elif ToDo == "remove item":

        security()
        Removal = input("What is the name of the menu item you wish to be removed? ")
        del menu[Removal]
        writemenu()
        return menu
    
    elif ToDo == "Change password":
         
         security()
         
         global password
         password = input("Please enter the new password")
         message = "Your password has now been changed"
         return message
    
    elif ToDo == "quit":

        writemenu()
        print("Thank you for using our software.")
        exit()
        return menu

password = "6942"

while True:
    
    menu = reading()
    action = input("Enter action to do here: ")
    print(switch(action))

