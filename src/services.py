tasks = []

def update_task():
    if not tasks:
        print('there is no homework')
        return
    new_value = input('Insert the title of the task to be modified.').strip()
    for value in tasks:
        if value['título'] == new_value:
            print (value['estado'])
            new_status = input('enter the new state: ')
            value['estado'] = new_status
            print(tasks)
            return
        
    print ('task not found')

def delete_task():
    if not tasks:
        print('here is no homework')
        return
    print(tasks)
    delete_task = input('Enter the name of the task to delete ').strip()
    ej = int(input('Are you sure you want to delete list 1? (YES) 2. (NO)'))
    if ej == 2:
        return
    for key in tasks:
        if key['título'] == delete_task:
            tasks.remove(key)
            print(tasks)
            return
    print ('task not found')
    

delete_task()