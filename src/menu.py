from services import create_task, show_tasks, update_task, delete_task
from validations import validate_int

def menu():
    while True:    
        print('** To Do Manager - Pro-Edition **')
        print('1. Add a task')
        print('2. View tasks')
        print('3. Update task')
        print('4. Delete task')
        print('5. Exit')

        option = validate_int('\nSelect an option (1-5): ', min_value=1, max_value=5)

        match option:
            case 1:
                create_task()
            case 2:
                show_tasks()
            case 3:
                update_task()
            case 4:
                delete_task()
            case 5:
                print('\nExiting the program.')
                break