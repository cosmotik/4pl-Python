from prettytable import PrettyTable

options = "\n1: Enter A to add a new ToDo object.\n2: Enter D to delete object.\n3: Enter U to update ToDo list." \
          "\n4: Enter E to exit the program.\n5: Enter L to show full ToDo List."
print(options)

todo_list = []

x = PrettyTable()


def my_list():
    x.field_names = ["Item Names:"]
    for i in todo_list:
        x.add_row([i])
    print(x.get_string(title=" To Do List"))
    x.clear_rows()


running = True
while running:
    UserInput = input("\nWhat do you want to do? A, D, U, L, E").lower()
    if UserInput == "a":
        new_todo = input("\nPlease enter your new ToDo object: ").lower()
        print(f"Your current todo is {new_todo}.")
        todo_list.append(new_todo)
    elif UserInput == "d":
        while True:
            ObjName = input("\nPlease enter a name of an object, that you want delete.").lower()
            if ObjName in todo_list:
                todo_list.remove(ObjName)
                print(f"You deleted: {ObjName}")
                my_list()
                break
            else:
                print("Item not found.")
    elif UserInput == "u":
        while True:
            ObjName = input("\n Please enter a name of object you want to update: ").lower()
            if ObjName in todo_list:
                update = input(f"Please enter the object you want to update {ObjName} with.")
                index = todo_list.index(ObjName)
                todo_list[index] = update
                print("Your updated List.")
                my_list()
                break
            else:
                print("Item not found")
    elif UserInput == "e":
        Exit = input("Are you sure you want to exit? Y/N").lower()
        if Exit == "y":
            running = False
    elif UserInput == "l":
        my_list()
    else:
        print("Enter a valid value.")
