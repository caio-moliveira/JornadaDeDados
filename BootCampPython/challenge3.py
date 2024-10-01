import argparse
import json
import os

# File where the employees dictionary will be stored
EMPLOYEES_FILE = "employees.json"

# Function to load the employees dictionary from a JSON file
def load_employees():
    if os.path.exists(EMPLOYEES_FILE):
        with open(EMPLOYEES_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save the employees dictionary to a JSON file
def save_employees(employees):
    with open(EMPLOYEES_FILE, "w") as file:
        json.dump(employees, file, indent=4)

# Load the current state of the employees dictionary
employees = load_employees()

# Function to add information to the employees dictionary
def add_info_to_dict(name: str, salary: float, bonus: float):
    # Calculate the final bonus
    final_bonus = 1000 + salary * bonus
    
    # Create a dictionary for the current employee's information
    employee_info = {
        "name": name,
        "salary": salary,
        "bonus": bonus,
        "final_bonus": final_bonus
    }
    
    # Add this employee's dictionary to the 'employees' dictionary
    employees[name] = employee_info
    
    # Save the updated dictionary to the file
    save_employees(employees)

# Function to print employees' data
def print_employees():
    if employees:
        print("The dictionary has been populated:")
        for emp_name, emp_info in employees.items():
            print(f"Name: {emp_name}, Details: {emp_info}")
    else:
        print("The dictionary is still empty.")

# Validate user input for name, salary, and bonus
def get_employee_data():
    name = input("Type your name: ").strip()

    while not name or any(char.isdigit() for char in name):
        print("Invalid name, please try again.")
        name = input("Type your name: ").strip()

    salary = input("Type your salary: ").strip()
    while not salary.replace('.', '', 1).isdigit():
        print("Invalid salary, please try again.")
        salary = input("Type your salary: ").strip()

    bonus = input("Type the bonus (as a decimal): ").strip()
    while not bonus.replace('.', '', 1).isdigit():
        print("Invalid bonus, please try again.")
        bonus = input("Type the bonus (as a decimal): ").strip()

    # Add validated employee info to the dictionary
    add_info_to_dict(name, float(salary), float(bonus))

    # Print the result
    bonus_total = 1000 + float(salary) * float(bonus)
    print(f"{name}, your salary is: €{float(salary):.2f} and your final bonus is: €{bonus_total:.2f}")

# Main function to handle command-line inputs
def main():
    parser = argparse.ArgumentParser(description="Manage employee data.")
    
    # Add arguments for actions
    parser.add_argument("--input", action="store_true", help="Input employee data")
    parser.add_argument("--print", action="store_true", help="Print the employee dictionary")
    
    args = parser.parse_args()
    
    # Handle the --input action
    if args.input:
        get_employee_data()
    
    # Handle the --print action
    if args.print:
        print_employees()

if __name__ == "__main__":
    main()
