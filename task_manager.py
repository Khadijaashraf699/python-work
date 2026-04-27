"""
Design and develop a command-line Task Manager app where users can create, update ,
complete, view, delete, and filter their daily tasks. The app will store tasks in memory and
optionally save them to a file for persistence.
Task Creation:
• Prompt the user to enter a task name.
• Ask for task priority (Low, Medium, High).
• Automatically mark it as "Incomplete".
• Store it in a list of dictionaries.
Example:
task = {"title": "Buy milk", "priority": "High", "completed": False}
Python Code File:
task_manager.py
Data File: 
tasks.txt
Menu
The application must present a menu that keeps running until the user exits: 
===== Task Manager =====
1. Add a task
2. View all tasks 
3. Update a task 
4. Mark a task as complete
5. Delete a task
6. Filter tasks
7. Exit
======================== 
Enter your choice:




"""


class TaskManager:
    def __init__(self):
        self.all_task = {}

    def add_task(self, task, type_task):
        task_data = {
            'title': task,
            'priority': type_task,
            'completed': False
        }
        task_id = len(self.all_task) + 1
        self.all_task[task_id] = task_data
        print('--- Successfully Added ---')
  
    def view_task(self):
        for key, value in self.all_task.items():
            print(f'Task_Num   All_Task\n{key}    :     {value}')
        if not self.all_task:
            print('Empty List')  

    def mark_complete(self, task_num):
        if task_num in self.all_task:
            self.all_task[task_num]['completed'] = True
            print('Successfully completed')
        else:
            print('Task not found')

    def update_task(self, task_num, exist_task, update_value):
        if task_num in self.all_task:
            if exist_task in self.all_task[task_num]:
                self.all_task[task_num][exist_task] = update_value
            else:
                print('Incorrect Task Name')
        else:
            print('invalid Task')

    def filter_task(self, task_name):
        found = False
        for key, value in self.all_task.items():
            if task_name in value.values():
                print(key, ': ', value)
                found = True
        if found == False:
            print('Invalid Search')

    def delete_task(self, task_id):
        if task_id in self.all_task:
            del self.all_task[task_id]
            print('succesfully remove')
        else:
            print('Invalid Task')




def main():
    obj = TaskManager()
    while True:
        print('---- Welcome Task Manager App ----')
        option = int(input('Add    Task Press 1:\nView   Task Press 2:\nUpdate Task Press 3:\nDelete Task Press 4:\nFilter Task Press 5:\nComplete Task Press 6:\nExit Programme Press 7: '))
        if option == 1:
            title = input('Enter Task Name: ')
            priority = input('Enter type of Task\nLow, Mediem, High : ').lower()
            obj.add_task(title, priority)
        elif option == 2:
            obj.view_task()
        elif option == 3:
            task_num = int(input('Enter task Number: '))
            value = input('Enter Name For updation: ')
            update = input('Enter Updated Value: ')
            obj.update_task(task_num, value, update)
        elif option == 4:
            tsk = int(input('Enter Task Number: '))
            obj.delete_task(tsk)
        elif option == 5:
            name = input('Search here.... ')
            obj.filter_task(name)
        elif option == 6:
            comp_task = int(input('Enter Task Number: '))
            obj.mark_complete(comp_task)
        elif option == 7:
            print('Thanks For Using APP')
            break
        else:
            print('Invalid Number')


obj_1 = main()
