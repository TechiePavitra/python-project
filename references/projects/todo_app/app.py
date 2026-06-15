# To-do list Application
# v0.3 Pre-Alpha CLI Version
tasks = []
flag = True

def show_options():
    """Shows option on screen"""
    print("\n--- To-do List App v0.3 ---")
    print("Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    """Adds Task in tasks list"""
    task = input("Enter a Task: ").strip()
    if task:
        tasks.append({"task": task, "completed":False})
        print(f"Task '{task}' added successfully!")
    else:
        print("Please enter a valid task!")


def view_task():
    """View Tasks"""
    if not tasks:
        print("\nNo Tasks found.")
        return
    else:    
        print("\nTask List:  ")
        for index, task in enumerate(tasks, start=1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{index}. {task['task']} {status}")


def complete_task():
    """Mark a task as completed."""
    if tasks:
        view_task()
        user_choice = input("Enter the task number:  ")
        try:
            user_choice = int(user_choice)
            tasks[user_choice-1]["completed"] = True
            print(f"Task '{tasks[user_choice-1]['task']}' marked as completed [X].")
        except:
            print("Please enter a valid choice.")    
    else:
        print("There are no tasks to mark as completed.")


def delete_task():
    """Delete a Task."""
    if tasks:
        view_task()
        user_choice = input("Enter the task number::  ")
        try:
            user_choice = int(user_choice)
            print(f"Task '{tasks[user_choice-1]['task']}' deleted successfully!")
            del tasks[user_choice-1]
        except:
            print("Please enter a valid choice.")    
    else:
        print("There are no tasks to delete.")    

        
# Logic
while flag:
    show_options()
    user_choice = input("Enter your choice:  ")
    try:
        user_choice = int(user_choice)
        if user_choice in range(1,6):
            if user_choice == 1:
                add_task()
            elif user_choice == 2:
                view_task()
            elif user_choice == 3:
                complete_task()
            elif user_choice == 4:
                delete_task()
            elif user_choice == 5:
                flag = False
        else:
            print("Please enter a valid choice.")         
    except:
        print("Please enter a valid choice.")  