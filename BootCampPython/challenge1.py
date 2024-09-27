#name
user_name = input ("type your name: ")

#salary
user_salary = float(input("Type your salary: "))

#bonus
user_bonus = float(input("Type your bonus: "))

#constant bonus 
CONSTANTE_BONUS = 1000

bonus_value = CONSTANTE_BONUS + user_salary * user_bonus

print(f"User {user_name} will get the bonus of {bonus_value}")