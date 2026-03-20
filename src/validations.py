def validate_int(prompt, min_value= None, max_value = None):
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("incorrect number")
            continue
        value = int(value)
        if min_value is not None and  value < min_value:
                print(f"Number must be at least {min_value}.")
                continue
        if max_value is not None and value < min_value:
                print(f"Number must be at most {max_value}.")
                continue
        return value
        
def validate_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("This field cannot be empty.")
            continue
        return value
        
def validate_priority(prompt):
    valid_priorities = ["high", "mediun", "low"]
    while True:
        value = input(prompt).strip().lower()
        if value not in  valid_priorities:
            print(f"Invalid pririty. chooose from : {','.join(valid_priorities)}.")
            continue
        return value  