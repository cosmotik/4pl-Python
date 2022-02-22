import sys
from to_do import ToDoList


class Menu:

    def __init__(self):
        self.toDoList = ToDoList()
        self.choices = {
            "1": self.show_tasks,
            "2": self.add_tasks,
            "3": self.delete_tasks,
            "4": self.quit,
        }

    def display_menu(self):
        print(
            """
            To Do List menu:

            1. Show all Tasks 
            2. Add Tasks
            3. Delete Tasks
            4. Quit

            """
        )

    def run(self):

        while True:
            self.display_menu()
            choice = input("Enter an option")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_tasks(self, tasks=None):
        if not tasks:
            tasks = self.toDoList.tasks
        for task in tasks:
            print("{0}: {1}".format(task.id, task))

    def add_tasks(self):
        task_name = input("Enter a task:")
        self.toDoList.new_task(task_name, complete="N")
        print("Your task has been added:")

    def delete_tasks(self):
        id = input("Enter a task id:")
        task = input("Enter task name:")
        if task:
            self.toDoList.delete_task(id, task)

    def quit(self):
        print("Thank you for using ToDoList today")
        sys.exit(0)


Menu().run()
