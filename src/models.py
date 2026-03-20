def create_task_model(title, description, priority):
    return {
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending"
        }
