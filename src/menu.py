def menu():
    while True:    
        print('** To Do Manager - Pro-Edition **')
        print('1. Add a task')
        print('2. View tasks')
        print('3. Update task')
        print('4. Delete task')
        print('5. Exit')

        option = int(input('\nSelect an option (1-5): '))

        match option:
            case 1:
                from services import add_task
                add_task()
            case 2:
                from services import view_tasks
                view_tasks()
            case 3:
                #Waiting for the implementation of the update_task function
                pass
            case 4:
                #Waiting for the implementation of the delete_task function
                pass
            case 5:
                print('\nExiting the program.')
                break
            case _:
                print('\nInvalid option. Please select a number between 1 and 5.')