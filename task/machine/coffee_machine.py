water = 400
milk = 540
coffee = 120
cups = 9
money = 550
coffee_menu = {
    "1": (250, 0, 16, 4),
    "2": (350, 75, 20, 7),
    "3": (200, 100, 12, 6)
}
on = True


def print_things():
    print(f'''The coffee machine has:
{water} of water
{milk} of milk
{coffee} of coffee beans
{cups} of disposable cups
{money} of money''')


def get_action():
    global on
    print()
    print("Write action (buy, fill, take):")
    command = input()
    if command == "buy":
        buy()
    elif command == "fill":
        fill()
    elif command == "take":
        take()
    elif command == "remaining":
        print_things()
    elif command == "exit":
        on = False


def buy():
    global cups
    global coffee
    global water
    global milk
    global money
    print()
    print('''What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 
    back - to main menu:''')
    command = input()
    if command == "back":
        pass
    else:
        ingredients = coffee_menu.get(command)
        if cups > 0 and water >= ingredients[0] and milk >= ingredients[1] and coffee >= ingredients[2]:
            cups -= 1
            water -= ingredients[0]
            milk -= ingredients[1]
            coffee -= ingredients[2]
            money += ingredients[3]
        else:
            if water < ingredients[0]:
                print("Sorry, not enough water!")
            elif milk < ingredients[1]:
                print("Sorry, not enough milk!")
            elif coffee < ingredients[2]:
                print("Sorry, not enough coffee beans!")
            elif cups == 0:
                print("Sorry, not enough disposable cups!")
    print()


def fill():
    global cups
    global coffee
    global water
    global milk
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee do you want to add:")
    coffee += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())
    print()


def take():
    global money
    print(f"I gave you ${money}")
    print()
    money = 0


while on:
    get_action()
