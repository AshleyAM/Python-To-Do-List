import cPickle
import datetime
import smtplib

class Task:
    '''The task class is used to create individual task objects. Every object in the list
       is an instance of the Task class. '''
    
    def __init__(self, title, duedate):
        '''Set variables required for tasks. '''
        self.__t = title
        self.__dd = duedate

    # getter and setter methods for private variables
    
    def get_title(self):
        return self.__t

    def get_duedate(self):
        return self.__dd
    
    def set_title(self, newTitle):
        if newTitle == "":
            print "A task requires a title."
        else:
            self.__t = newTitle

    def set_duedate(self, newDuedate):
        if newDueDate == "":
            print "A task requires a due date."
        else:
            self.__dd = newDueDate 

    def __str__(self):
        return str(self.__t) + " // Due on " + str(self.__dd) + "\n"

class Tasks:
    ''' The Tasks class handles Task objects by organizing and manipulating them in a list
        and writing said list to a pickle file. '''
    
    def __init__(self):
        ''' Creates empty list for Task objects to be held in. ''' 
        self.__tasks = []

    def read_file(self):
        ''' Reads list from file into local list. ''' 
        try:
            filein = open("tasks.dat","r")
            self.__tasks = cPickle.load(filein)
            filein.close()

        except EOFError:
            pass

        except IOError:
            filein = open("tasks.dat", "w+") # create file if one does not exist in the directory
            filein.close() 
            
        return self.__tasks

    def write_file(self):
        ''' Writes local list to file. '''
        fileout = open("tasks.dat", "w+")
        cPickle.dump(self.__tasks, fileout)
        fileout.close()

    def updated_list(self):
        print "*" * 30 
        print "\nUpdated task list: \n"
        self.view_tasks()

    def add_task(self, task):
        ''' Adds task to local list, then uses write_file() method to update the file. '''
        self.__tasks = self.read_file()
        self.__tasks.append(task)
        self.write_file()
        print "\nTask successfuly added."
        self.updated_list()

    def view_tasks(self):
        ''' Reads list in from file using read_file method, then prints them out a formatted list. '''
        self.__tasks = self.read_file()
        
        if len(self.__tasks) == 0:
            print "No active tasks. \n"

        else:
            for x in range (0, len(self.__tasks)):
                print x+1, ">" , str(self.__tasks[x])

        print "*"*30 , "\n"

    def delete_task(self, taskToDelete):
        ''' Reads list in from file, deletes item in local list, writes updated local list back into file. '''
        self.__tasks = self.read_file() 

        try:
            del self.__tasks[taskToDelete-1] 

        except IndexError, ValueError:
            print "This task does not exist."
            pass
        
        self.write_file()
        self.updated_list()
        
    def edit_task(self, taskToEdit, newTask):
        ''' Reads list on from file, overwrites selected Task object in list, writes updated list back to file '''
        self.__tasks = self.read_file()
        try: 
            self.__tasks[taskToEdit-1] = newTask
        except IndexError, ValueError:
            print "\nThis task you wish to edit does not exist."
            pass 
        self.write_file()
        self.updated_list()

    def sort_tasks(self):
        ''' Sorts task objects by date. '''
        self.__tasks = self.read_file()
        self.__tasks = sorted(self.__tasks, key = lambda Task: Task.get_duedate())
        self.write_file()
        self.updated_list()

    def move_task(self, positionToMove, itemToMove):
        '''Moves selected task to selected place in list '''
        self.__tasks = self.read_file()
        
        try: 
            self.__tasks.insert(positionToMove -1, self.__tasks.pop(itemToMove - 1))
            self.write_file()
            self.updated_list() 
            
        except ValueError , IndexError:
            print "The task or position you have selected does not exist."
            pass

    def notify(self):
        '''Sends an email notification if task due date matches today's date. '''
        self.__tasks = self.read_file() 
        
        for d in range (0, len(self.__tasks)):
            if self.__tasks[d].get_duedate() == datetime.date.today(): 
                try:
                    sender = "ashleytaskmanger@gmail.com"  
                    recipient  = "ashleytaskmanager@gmail.com"  
                    notification = "The following task is due to be completed today: " + str(self.__tasks[d])  
                      
                    __username = "ashleytaskmanager@gmail.com"  
                    __password = "helloworld123"  
                      
                     
                    server = smtplib.SMTP("smtp.gmail.com:587")  
                    server.starttls()  
                    server.login(__username,__password)  
                    server.sendmail(sender, recipient, notification)  
                    server.quit()

                    dateout = open("today.dat", "w+")
                    cPickle.dump(datetime.date.today())
                    dateout.close()
                    
                except:
                    print "Unable to contact e-mail server. Please ensure this user account has admistrator privealages. \n"
                    pass 
            else:
                pass
# Test code.                
if __name__ == "__main__":
    newTask = Task("Test Task", datetime.date(2012,05,31))
    testSession = Tasks()
    testSession.add_task(newTask)
    testSession.notify() 
    
         
