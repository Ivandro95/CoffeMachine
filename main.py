
total_coin = 0
profits_money = 0
another = True

def sum_coins(quarter,dime, nickle,pennie):
    quarter *= 0.25
    dime *= 0.10
    nickle *= 0.05
    pennie *= 0.01
    return quarter + dime + nickle + pennie

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino)"
while another:
    user_choice = input("What would you like? espresso, latte or capuccino \n ").lower()
    if user_choice == "off":
        another = False
    elif user_choice == "report":
        print(resources)
    elif resources["water"] <= MENU[user_choice]["ingredients"]["water"]:
        print("Sorry there is not enough water.")

    elif resources["milk"] <= MENU[user_choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] <= MENU[user_choice]["ingredients"]["milk"]:
        print("Sorry there is not enough coffe.")
    else:
        print("Please insert coins.")
        quarter_coins = int(input("how many quarters? "))
        dime_coins = int(input("how many dimes? "))
        nickle_coins = int(input("how many nickles? "))
        pennie_coins = int(input("how many pennies? "))
        total_coin = sum_coins(quarter=quarter_coins,dime= dime_coins,nickle=nickle_coins,pennie=pennie_coins)
#TODO 2:  Check that the user has inserted enough money to purchase the drink they selected.

        if total_coin < MENU[user_choice]["cost"]:
            print(f"Sorry that's not enough money. Money refunded.")
        elif total_coin >= MENU[user_choice]["cost"] and user_choice == "espresso":
            resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            resources["money"] = 0
            resources["money"] += MENU[user_choice]["cost"]
        elif total_coin >= MENU[user_choice]["cost"]:
            resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
            resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            resources["money"] = 0
            resources["money"] += MENU[user_choice]["cost"]
            resources["money"] += MENU[user_choice]["cost"]


        print(f"Here is ${total_coin - MENU[user_choice]['cost']} in change.")
        print(f"Here is your {user_choice} ☕️. Enjoy!")
