# PYTHON Basics
# In support of completing the Google Cybersecurity Certificate

# Import a library NumPy that assist with computing
import numpy as np

# Create an array
numbers = np.array([1,2,3,4,5])
print(numbers)

# Display a string.
print("Enter User Password:")

# Calculate numbers using print().
# Returns: 4
print(2 + 2)

# Evaluate a comparison.
# Returns: False
print(12 < 2)

# Create and display a list containing different data types.
print([12, 32, "time"])

# Map keys to values using a dictionary.
device_status = {
    "A": "On",
    "B": "Off"
}

# Store a device ID in a variable.
device_id = "23rHH"

# Display the value stored in the variable.
print(device_id)

# Display the variable's data type.
# Returns: <class 'str'>
print(type(device_id))

# Create a variable and list
computer_id = "3245"
print(computer_id)
computer_list = ["basement", "finance", "hr"]
print(computer_list)

# Create variables with comparisons
max_users = 99
type(max_users)
assigned_users = 90
print(max_users)
print(max_users <= assigned_users)

# Create conditional statement
if max_users > 100:
    print("Too many users")
if max_users == 100:
    print("Maximum users reached. No more users allowed")
else:
    print("Proceed to enter user")

# Using loops
for topics in [11,12,13,14]:
    print(topics)

for classes in (range(0,3)):
    print("Class full.")

student = 1
while student <= 5:
    print("Class is open")
    student = student + 1
else:
    print("Class is full")

# Type of datra
var1 = 9.5
var1_type = type(var1)
print(var1_type)

# Create a function and call it
def warning_alert ():
    print("Too many attempts.")
warning_alert()

# Using parameters
def close_file(time, location):
    print("File has been open too long.", time, location)
close_file("1215 hours", "USA")

# Using return
def calculate_enrolled(student_spots, student_enroll):
    spots_left = student_spots - student_enroll
    return spots_left

print(calculate_enrolled(20,14))
