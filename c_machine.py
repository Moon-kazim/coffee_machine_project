from art import logo
from data_type import resources, MENU

print("welcome to coffee machine".title())
print(logo)


# 3. printing report
def report(r_water, r_milk, r_coffee, r_money):
    return


# 4. check resourses
"""returns true when order can be made, false when ingredients are not sufficent"""
def is_resources_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True

profit = 0


# 5. Process coin
def process_coin():
    """return the total number of coins inserted"""
    print("Insert the coin:")
    total = float(input("How many quaters: "))*.25
    total += float(input("How many dimes: "))*.1
    total += float(input("How many nickles: "))*.05
    total += float(input("How many pennies: "))*.01
    return total


# 6. check transaction
def is_transaction_succesful(money_recived, drink_cost):
    """Return true when payment is succesful and flase is inserted money is in sufficent"""
    if money_recived>drink_cost:
        change = round(money_recived - drink_cost, 2)
        if change > 0:
            print(f"please collect your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry the money recived is insufficent, please collect your ${money_recived}")
        return False


# 7. make a coffee
def make_coffee(drink_name, order_ingredent):
    """Deduct the ingredients from the resourses"""
    for item in order_ingredent: 
        resources[item] -= order_ingredent[item]
    print(f"Your {drink_name} is ready ")

# 1. Asking user choice
machine = True
while machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ".lower())
    """2. Turn off the Coffee Machine"""
    if choice == "off":
        print("Coffee machine is under maintenance!\nPlease check after some time!")
        machine = False
    elif choice == "report":
        print(f"water : {resources['water']} ")
        print(f"milk : {resources['milk']}")       
        print(f"coffee : {resources['coffee']}") 
        print(f"money : {profit}")
    else:
        drink = MENU[choice]
        # 4.
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            # 6.
            if is_transaction_succesful(payment,drink["cost"]):
                # 7.
                make_coffee(drink_name=choice, order_ingredent=drink["ingredients"])