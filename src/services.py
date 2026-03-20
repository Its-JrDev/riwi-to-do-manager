tasks = []

def get_status_tasks(select, tasks):
    if select == 1:
        pendings_tasks = []
        for task in tasks:
            if task["status"] == "pending":
                pendings_tasks.append(task)
        return pendings_tasks
    
    elif select == 2:
        completed_tasks = []
        for task in tasks:
            if task["status"] == "completed":
                completed_tasks.append(task)
        return completed_tasks

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

def create_task():  
    title=input("ingrese un titulo: ")
    description=input("ingrese la descripcion: ")
    priority=input("ingrese la prioridad: ")
    status="por hacer"
        
    tasks.append({"title":title,"description":description,"priority":priority,"status":status})    
    print(f"task {tasks["title"]} it was crated correctly")    
def show_task():
    if tasks==None:
        print('tasks are empty, please crate one')
    else:    
        print("\n---tasks---")
        for i,t in enumerate(tasks):
            print(f"{i+1}. {t['title']}\nthe description are : {t['description']}\nwith priority: {t['priority']} and status: {t['status']}")
