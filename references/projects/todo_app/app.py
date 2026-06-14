# To-do list Application
# v0.1 Pre-Alpha CLI Version
tasks = []
flag = True

def show_options():
    """Shows option on screen"""
    print("\n--- To-do List App v0.1 ---")
    print("Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    """Adds Task in tasks list"""
    task = input("Please Enter Your Task: ")
    tasks.append({"task": task, "completed":False})
    print(f"Task: {task} added!")


def view_task():
    """View Tasks"""
    print("\nHere is List of Tasks:  ")
    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{index}. {task['task']} {status}")


def complete_task():
    """Mark a Task a Completed."""
    if tasks:
        view_task()
        user_choice = input("Please Enter Your Task Number:  ")
        try:
            user_choice = int(user_choice)
            tasks[user_choice-1]["completed"] = True
            print(f"Task: {tasks[user_choice-1]['task']} marked as Completed [X]")
        except:
            print("Please Enter a Valid choice!")
    else:
        print("Please add task to mark as complete!")


def delete_task():
    """Delete a Task."""
    if tasks:
        view_task()
        user_choice = input("Please Enter Your Task Number:  ")
        try:
            user_choice = int(user_choice)
            print(f"Task: {tasks[user_choice-1]['task']} successfully deleted!")
            del tasks[user_choice-1]
        except:
            print("Please Enter a Valid choice!")
    else:
        print("There is no task to remove it!")
    
# Logic
while flag:
    show_options()
    user_choice = input("Enter Your choice:  ")
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
            print("Please Enter a Valid choice!")       
    except:
        print("Please Enter a Valid choice!")