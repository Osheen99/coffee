LATTE = 1  
ESPRESSO = 2
CAPACCINO = 3
MACHINE_TURN_OFF_PROMPT = "off" 
MACHINE_TURN_OFF_PROMPT_INT = 78
REPORT = "report"
REPORT_INT = 43
is_on = True
resources = {  
    "water": "380",
    "milk": "200",
    "coffee": "1000"

}
money = 0
while is_on:
    user_choice = (input("what would you like? (latte/espresso/capaccino)"))

    if user_choice == MACHINE_TURN_OFF_PROMPT:
      user_choice = MACHINE_TURN_OFF_PROMPT_INT
    elif user_choice == REPORT:
       user_choice = REPORT_INT
    
    if int(user_choice) == LATTE:
        print(f"user choice: {user_choice}")
    elif int(user_choice) == ESPRESSO:
        print(f"user choice: {user_choice}")
    elif int(user_choice) == CAPACCINO: 
        print(f"user choice: {user_choice}")
    elif int(user_choice) == MACHINE_TURN_OFF_PROMPT_INT:
        is_on = False
    elif int(user_choice) == REPORT_INT:
        print(f" water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print("money: ${money}")

    else:
        print("wrong output")
        
 


