class ToDoList():
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append(task)
    def delete_task(self,task):
        self.tasks.remove(task)
    def display_task(self):
        for task in self.tasks:
            print(task)
    def input_task(self):
        task = input('Enter a task: ')
        self.add_task(task)
    def remove_task(self):
        task=input('Enter the task to remove: ')
        self.delete_task(task)
'''
The ToDoList class handles multiple responsibilities:
    -   Managing tasks
    -   Handling user input
    -   displaying tasks.
'''

class TaskManager:
    def __init__(self):
        self.task=[]
    def add_task(self,task):
        self.task.append(task)
    def delete_task(self,task):
        self.task.remove(task)
class TaskPresenter:
    @staticmethod
    def display_tasks(taks):
        for task in taks:
            print(task)
class TaskInput:
    @staticmethod
    def input_task():
        return input('Enter a task:')
    
    @staticmethod
    def remove_task():
        return input('Enter the task to remove: ')
    


"""
    TaskManager   -> handle the storage and management of taks
    TaskPresenter -> Display tasks 
    TaskInput     -> Handles user input for adding or removing tasks
"""