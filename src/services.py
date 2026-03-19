
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