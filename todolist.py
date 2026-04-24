import json
import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """
    Load tasks from the file if it exists.
    Returns a list of task dictionaries.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            try:
                tasks = json.load(file)
                return tasks
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """
    Save the tasks list to the file.
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """
    Add a new task to the list.
    """
    task_desc = input("Enter the task description: ").strip()
    if task_desc:
        tasks.append({'task': task_desc, 'status': 'Pending'})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    """
    Display all tasks with their status.
    """
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status_symbol = "✅" if task['status'] == 'Completed' else "❌"
        print(f"{i}. {status_symbol} {task['task']} - {task['status']}")
    print()

def complete_task(tasks):
    """
    Mark a task as completed.
    """
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['status'] = 'Completed'
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """
    Delete a specific task.
    """
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_all_tasks(tasks):
    """
    Clear all tasks after confirmation.
    """
    if not tasks:
        print("No tasks to clear.")
        return
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
    if confirm in ['y', 'yes']:
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared!")
    else:
        print("Operation cancelled.")

def main():
    """
    Main function to run the To-Do List application.
    """
    tasks = load_tasks()
    print("Welcome to the To-Do List Application!")

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Clear all tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            clear_all_tasks(tasks)
        elif choice == '6':
            print("Thank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

# Run the main function
if __name__ == "__main__":
    main()