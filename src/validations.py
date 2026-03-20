def validate_int(prompt, min_value=None, max_value=None):
    """
    Validate that the input is an integer and optionally within a min and max range.
    """
    while True:
        value = input(prompt).strip()
        
        if not value.isdigit():
            print("\nInvalid input. Please enter a valid number.\n")
            continue
        
        value = int(value)
        
        if min_value is not None and value < min_value:
            print(f"\nNumber must be at least {min_value}.\n")
            continue
        
        if max_value is not None and value > max_value:
            print(f"\nNumber must be at most {max_value}.\n")
            continue
        
        return value


def validate_non_empty_string(prompt):
    """
    Ensure the input string is not empty.
    """
    while True:
        value = input(prompt).strip()
        
        if not value:
            print("\nThis field cannot be empty.\n")
            continue
        
        return value


def validate_priority(prompt):
    """
    Validate that the input is a valid priority: high, medium, or low.
    """
    valid_priorities = ["high", "medium", "low"]
    
    while True:
        value = input(prompt).strip().lower()
        
        if value not in valid_priorities:
            print(f"\nInvalid priority. Choose from: {', '.join(valid_priorities)}.\n")
            continue
        
        return value


def validate_status(prompt):
    """
    Validate that the input is a valid status: pending or completed.
    """
    valid_status = ["pending", "completed"]
    
    while True:
        value = input(prompt).strip().lower()
        
        if value not in valid_status:
            print(f"\nInvalid status. Choose from: {', '.join(valid_status)}.\n")
            continue
        
        return value