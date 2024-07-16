# Define available departments
departments = {
    "1": "HR",
    "2": "Finance",
    "3": "IT",
    "4": "Marketing"
}

# Display department options
print("Select a department:")
for key, value in departments.items():
    print(f"{key}. {value}")

# Get user input
user_input = input("Enter the department number: ")

# Check user input and perform action
if user_input in departments:
    selected_department = departments[user_input]
    print(f"You've selected the {selected_department} department.")
    # Perform further actions based on the selected department
    # For example, you can add conditional blocks for each department to perform specific tasks
else:
    print("Invalid department number. Please select a valid department.")
