# Use While to allow the use to type till the information is correct

#user name, salary, and bonus
name_valid = False
salary_valid = False
bonus_valid = False

while not name_valid:
    try:
        name = input("Type your name: ")

        #verify the name
        if len(name) == 0:
            raise ValueError("The name cannot be blank.")
        elif any(char.isdigit() for char in name):
            raise ValueError("The name cannot have numbers")
        else:
            print("Name valid: ", name)
            name_valid = True
    except ValueError as e:
        print(e)

    
    #Check user salary going through the while loop.
while not salary_valid:
    try:
        salary = float(input("Type your salary: "))
        if salary < 0:
            print("Please, type a positive value for salary: ")
        else:
            salary_valid = True
    except ValueError:
        print("Invalid enter, please type a number")

    #Check user bonus going through the while loop.
while not bonus_valid:
    try:
        bonus = float(input("Type the bonus: "))
        if bonus < 0:
            print("Plese, type a positive number.")
        else:
            bonus_valid=True
    except ValueError:
        print("Invalid enter, please type a number.")

bonus_total = 1000 + salary * bonus

#print the result
print(f"{name}, your salary is: €{salary:.2f} and your final bonus is: €{bonus_total:.2f}")





