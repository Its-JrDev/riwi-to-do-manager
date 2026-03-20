from validations import validate_non_empty_string, validate_priority, validate_status, validate_int

tasks = []

def get_status_tasks(select, tasks):
    """
    Display tasks filtered by status.
    select: 1 -> pending tasks, 2 -> completed tasks
    """
    if select == 1:
        # Filter pending tasks
        pendings_tasks = [task for task in tasks if task["status"] == "pending"]
        
        # Inform user if there are no pending tasks
        if not pendings_tasks:
            print('\nThere are no pending tasks.\n')
            return
        
        print('\n--Pending Tasks--')
        for i, task in enumerate(pendings_tasks):
            print(f"\n{i+1}. {task['title']}.")
            print(f"Description: {task['description']}")
            print(f"With priority: {task['priority']} and status: {task['status']}")
        print()  # final line for spacing
        return 
    
    elif select == 2:
        # Filter completed tasks
        completed_tasks = [task for task in tasks if task["status"] == "completed"]
        
        # Inform user if there are no completed tasks
        if not completed_tasks:
            print('\nThere are no completed tasks.\n')
            return
        
        print('\n--Completed Tasks--')
        for i, task in enumerate(completed_tasks):
            print(f"\n{i+1}. {task['title']}.")
            print(f"Description: {task['description']}")
            print(f"With priority: {task['priority']} and status: {task['status']}")
        print()  # final line for spacing
        return 

def create_task():
    """Create a new task and append it to the global tasks list."""
    print("\n--- Create Task ---")
    title = validate_non_empty_string("Enter the title: ")
    description = validate_non_empty_string("Enter the description: ")
    priority = validate_priority("Enter the priority (high, medium, low): ")
    
    # Importing the model here allows separation of service logic and data structure
    from models import create_task_model
    task = create_task_model(title, description, priority)
    tasks.append(task)
    
    print(f"\nTask '{title}' created correctly.\n")

def show_tasks():
    """Display tasks based on user filter selection: pending, completed, or all."""
    if not tasks:
        print('\nThere are no tasks, please create one.\n')
        return
    
    print("\nFilter tasks? | 1. Pending | 2. Completed | 3. All |")
    filter_option = validate_int("Select an option: ", min_value=1, max_value=3)
    
    if filter_option in [1, 2]:
        get_status_tasks(filter_option, tasks)
    else:
        print("\n--- All Tasks ---")
        for i, t in enumerate(tasks):
            print(f"\n{i+1}. {t['title']}.")
            print(f"The description is: {t['description']}")
            print(f"With priority: {t['priority']} and status: {t['status']}")
        print()  # final spacing

def update_task():
    """Update the status of an existing task by title."""
    if not tasks:
        print('\nThere are no tasks.\n')
        return
    
    new_value = input('\nInsert the title of the task to be modified: ').strip()
    for value in tasks:
        if value['title'] == new_value:
            print(f"\nCurrent status: {value['status']}")
            new_status = validate_status('Enter the new status (pending, completed): ')
            value['status'] = new_status
            print(f"\nTask '{value['title']}' updated to status '{value['status']}'.\n")
            return
    
    print('\nTask not found.\n')

def delete_task():
    """Delete an existing task after user confirmation."""
    if not tasks:
        print('\nThere are no tasks.\n')
        return

    delete_task_title = input('\nEnter the name of the task to delete: ').strip()
    ej = validate_int(f"Are you sure you want to delete '{delete_task_title}'? 1. (YES) 2. (NO): ", min_value=1, max_value=2)
    if ej == 2:
        print("\nDeletion cancelled.\n")
        return
    
    for key in tasks:
        if key['title'] == delete_task_title:
            tasks.remove(key)
            print(f"\nTask '{delete_task_title}' deleted successfully.\n")
            return
    print('\nTask not found.\n')