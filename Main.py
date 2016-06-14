import Task
import MainMenu

TaskStuff = Task.Tasks()
TaskStuff.notify()

Session = MainMenu.MainMenu(TaskStuff)
Session.show_menu()
