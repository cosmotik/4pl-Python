last_id = 0


class Task:
    def __init__(self, task_name, complete=""):
        self.task_name = task_name
        self.complete = "N"
        global last_id
        last_id += 1
        self.id = last_id


class ToDoList:
    def __init__(self):
        self.tasks = []

    def new_task(self, task_name, complete):
        self.tasks.append(Task(task_name, complete))

    def find_task(self, task_id):
        for task_name in self.tasks:
            if str(task_name.id) == str(task_name.id):
                return task_name
        return None

    def modify_task(self, task_id, task_name):
        task_name = self.find_task(task_id)
        if task_name:
            task_name.task_name = task_name
            return True
        else:
            return False

    def delete_task(self, task_id, complete):
        task = self.find_task(task_id)
        if task:
            task.complete = "Y"
            return self.tasks.remove(task_id - 1)
        else:
            return False
