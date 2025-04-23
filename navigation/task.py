# Task Management System
# This program allows users to manage their tasks, including adding, viewing, 
# marking as complete, filtering, saving, loading, and deleting tasks.

import json
import os

# CPT REQUIREMENT: Use of at least one list (or other collection type)
# This list stores all tasks and is used throughout the program
tasks = []

# CPT REQUIREMENT: At least one procedure with defined name, return type, and parameters
def add_task(description, priority):
    if not description or not priority:
        return False
    
    if priority.lower() not in ["high", "medium", "low"]:
        return False
    
    new_task = {
        "description": description,
        "priority": priority.lower(),
        "completed": False
    }
    
    tasks.append(new_task)
    return True

def mark_task_as_complete(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        return True
    return False

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        return True
    return False

# CPT REQUIREMENT: An algorithm that includes sequencing, selection, and iteration
def filter_tasks_by_priority(priority):
    # SEQUENCING: Initialize an empty list to store results
    filtered_tasks = []
    
    # ITERATION: Loop through all tasks
    for task in tasks:
        # SELECTION: Check if the task priority matches the specified priority
        if task["priority"] == priority.lower():
            # Add matching tasks to the filtered list
            filtered_tasks.append(task)
    
    # SEQUENCING: Return the filtered list after the loop is complete
    return filtered_tasks

# CPT REQUIREMENT: Instructions for input from a file
def save_tasks_to_file(filename):
    try:
        with open(filename, 'w') as file:
            json.dump(tasks, file)
        return True
    except:
        return False

# CPT REQUIREMENT: Instructions for input from a file
def load_tasks_from_file(filename):
    global tasks
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                tasks = json.load(file)
            return True
        return False
    except:
        return False

# CPT REQUIREMENT: Instructions for output (textual) based on input and program functionality
def display_tasks(task_list=None):
    if task_list is None:
        task_list = tasks
    
    if not task_list:
        print("No tasks to display.")
        return
    
    print("\n" + "-" * 60)
    print("| {:3} | {:30} | {:8} | {:10} |".format("No.", "Description", "Priority", "Status"))
    print("-" * 60)
    
    for i, task in enumerate(task_list):
        status = "Completed" if task["completed"] else "Pending"
        priority = task["priority"].capitalize()
        print("| {:3} | {:30} | {:8} | {:10} |".format(
            i + 1,
            task["description"] if len(task["description"]) <= 30 else task["description"][:27] + "...",
            priority,
            status
        ))
    print("-" * 60)

def main():
    filename = "tasks.json"
    
    load_tasks_from_file(filename)
    
    while True:
        print("\n===== Task Management System =====")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Filter tasks by priority")
        print("5. Delete a task")  
        print("6. Save tasks")
        print("7. Exit")
        
        # CPT REQUIREMENT: Instructions for input from the user
        choice = input("\nEnter your choice (1-7): ")  
        
        if choice == "1":
            # CPT REQUIREMENT: Instructions for input from the user
            description = input("Enter task description: ")
            print("Priority levels: High, Medium, Low")
            priority = input("Enter task priority: ")
            
            # CPT REQUIREMENT: Calls to your student-developed procedure
            if add_task(description, priority):
                print("Task added successfully!")
            else:
                print("Failed to add task. Please provide valid description and priority.")
                
        elif choice == "2":
            display_tasks()
            
        elif choice == "3":
            display_tasks()
            try:
                # CPT REQUIREMENT: Instructions for input from the user
                task_index = int(input("Enter the task number to mark as complete: ")) - 1
                if mark_task_as_complete(task_index):
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "4":
            print("Priority levels: High, Medium, Low")
            # CPT REQUIREMENT: Instructions for input from the user
            priority = input("Enter priority to filter by: ")
            
            if priority.lower() in ["high", "medium", "low"]:
                # CPT REQUIREMENT: Calls to your student-developed procedure
                filtered = filter_tasks_by_priority(priority)
                display_tasks(filtered)
            else:
                print("Invalid priority level.")
                
        elif choice == "5":
            display_tasks()
            try:
                # CPT REQUIREMENT: Instructions for input from the user
                task_index = int(input("Enter the task number to delete: ")) - 1
                if delete_task(task_index):
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "6":
            if save_tasks_to_file(filename):
                print(f"Tasks saved to {filename}!")
            else:
                print("Failed to save tasks.")
                
        elif choice == "7":  
            print("Thank you for using the Task Management System!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 7.") 

if __name__ == "__main__":
    main()





