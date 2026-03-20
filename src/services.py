tasks=[]
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
