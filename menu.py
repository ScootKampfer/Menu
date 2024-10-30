import time
login = 0

def menureading():
    
    PreviousMenu = eval(open('C:\\Users\\gaben\\OneDrive\\Documents\\menu.txt', 'r').read())
    return PreviousMenu

def writemenu():

        FutureMenu = open('menu.txt', 'wt') 
        FutureMenu.write(str(menu)) 
        FutureMenu.close() 

def security():
     
     password = open("C:\\Users\\gaben\\OneDrive\\Documents\\very fun number sequences.txt", 'r').read()
     attempt = input("\nPlease input your password to gain access to admin privileges: \n\n")
     if attempt != password:

          print('\nYour password was incorrect.')
          print("\nAccess terminated!")
          time.sleep(1)
          exit()

     global login 
     login = 1

def lock():

     if login != 1:

          print("\nAccess denied!\n")
          time.sleep(1)
          exit()

def switch(ToDo):

    if ToDo == "view menu":

     
        tabbedmenu = "\n" + str(menu)
        return tabbedmenu
    
    elif ToDo == "help":
         
         message = "\nThe available commands are as follows: \n \n - view menu \n - quit \n\nIf you need to access admin controls, you need to login with the login command."
         return message

    elif ToDo == "admin help":
         
         lock()
         message = "\n The available commands are as follows: \n \n - view menu \n - add item \n - clear \n - remove item \n - change password \n - quit"
         return message

    elif ToDo == "clear":
         
         lock()
         areyousure = input("\nAre you sure you want to clear the entire menu? Type CLEAR if you are sure you want to clear: \n\n")
         
         if areyousure == "CLEAR":
              
              menu.clear()
              writemenu()
              message = "\nThe menu has been cleared."
              return message
         
         else:
              
              message = "\nAction canceled."
              return message

    elif ToDo == "add item":

        lock()
        NewMenuItem = input("\nWhat is the name of the new menu item?\n\n")
        NewMenuPrice = "$" + format(float(input(f"\nAnd what is the price of a {NewMenuItem} in dollars?\n\n")), ".2f")
        menu[NewMenuItem] = NewMenuPrice
        writemenu()
        tabbedmenu = "\n" + str(menu)
        return tabbedmenu
    
    elif ToDo == "remove item":

        lock()
        Removal = input("\nWhat is the name of the menu item you wish to be removed?\n\n")
        
        try:

          del menu[Removal]
          writemenu()
          tabbedmenu = "\n" + str(menu)
          return tabbedmenu

        except:

          message = "\nThis menu item does not exist!"
          return message

    
    elif ToDo == "change password":
         
         lock()
         
         global password
         password = input("\nPlease enter the new password:\n\n")
         Changes = open("C:\\Users\\gaben\\OneDrive\\Documents\\very fun number sequences.txt", "wt")
         Changes.write(str(password))
         Changes.close()
         message = "\nYour password has now been changed."
         return message

    elif ToDo == "quit":
     
        lock()
        writemenu()
        print("\nThank you for using our software. Your menu has been saved.\n")
        global login
        login = 0
        time.sleep(1)
        exit()
        return menu
        
    elif ToDo == "login":

          security()
          message = "\nYou have been successfully logged in"
          return message

print("\nType help for all available commands.")

while True:
    
    menu = menureading()
    action = input("\nEnter action to do here: \n\n")
    print(switch(action))