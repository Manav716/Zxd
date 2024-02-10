# Variables
name = "Nora"
age = 56
is_student = False

# List
grades = [67, 100, 87, 56]

# Dictionary
student = {
    "name": "Nora",
    "age": 56,
    "is_student": False,
    "grades": [67, 100, 87, 56]
}

# Function
def get_average_grade(grades):
    """
    Calculate the average grade of a student.
    """
    total = sum(grades)
    average = total / len(grades)
    return average

# String
message = f"Hi, I'm {name}. I'm {age} years old. "
message += f"My average grade is {get_average_grade(grades)}."

# String methods
message = message.capitalize()
message = message.strip()

# Print
print(message)