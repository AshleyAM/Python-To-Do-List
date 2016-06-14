import Task
import datetime
import sys

class MainMenu:
    def __init__(self, task):
        self.t = task 
     
    def show_menu(self):
        ''' Main menu method provides user with easy access to all of the methods within the Tasks class. '''
        
        print "Welcome to Ashley's task manager. Please select an option from below.\n"
        print "1. View Tasks"
        print "2. Add Tasks"
        print "3. Delete Tasks"
        print "4. Edit Tasks"
        print "5. Prioritize tasks"
        print "Enter 'q' to quit\n" 

        choice = raw_input("Option number: ")
        print " "

        if choice == "1":
            self.t.view_tasks()
            self.show_menu()

        elif choice == "2":       
            self.t.add_task(Task.Task(raw_input("Enter the task: "), self.date_setter())) 
            self.show_menu() 

        elif choice == "3":
            self.t.view_tasks() 
            self.t.delete_task(int(raw_input("Enter the number of the task you wish to delete: ")))
            self.show_menu()
            
        elif choice == "4":
            self.t.view_tasks() 
            self.t.edit_task(int(raw_input("Enter the number of the task you wish to edit: ")),
                           Task.Task(raw_input("Enter the new task: "), self.date_setter()))
            self.show_menu()
            
        elif choice == "5":
            self.t.view_tasks() 
            choice2 = raw_input("Enter 'd' if you would like to prioritize tasks by date, or 'm' if you want to manually alter the position of a task in the list: ")
            print " " 
            
            if choice2 == "d":
                self.t.sort_tasks()
                self.show_menu()

            elif choice2 == "m":
                itemToMove = int(raw_input("Enter the number of the task you wish to move: "))
                positionToMove = int(raw_input("Enter the position you wish to move the task to: "))

                self.t.move_task(positionToMove, itemToMove)
                self.show_menu() 

            else:
                print "Invalid selection. Return to main menu and try again."
                self.show_menu()

        elif choice == "q":
            sys.exit() 
                      
        else:
            print "This is not a valid option, try again."
            self.show_menu(self.t) 
            
    def date_setter(self):
        '''Sets values for datetime.date instances. Catches errors if invalid values are entered. '''
        
        try:
            year = int(raw_input("Please enter the year due (YYYY): "))
        
        except ValueError:
            print "This is not a valid date value, please begin entering the date again."
            self.show_menu()

        try:
            month = int(raw_input("Please enter the month due (MM): "))
        
        except ValueError:
            print "This is not a valid date value, please begin entering the date again."
            self.show_menu() 

        try:
            day = int(raw_input("Please enter the day due (DD): "))
        
        except ValueError:
            print "This is not a valid date value, please begin entering the date again."
            self.show_menu()

        try:
            due = datetime.date(year, month, day)
            return due 
        
        except ValueError:
            print "\nInvalid date values, return to main menu and try again.\n"
            self.show_menu()  

# Test code.                
if __name__ == "__main__": 

    TaskStuff = Task.Tasks()
    TaskStuff.notify()

    Session = MainMenu(TaskStuff)
    Session.show_menu()
    
