class CoffeeMachine:
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

    def input_(self):
        return input()

    def print_things(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
{self.money} of money''')

    def get_action(self):
        print()
        print("Write action (buy, fill, take, remaining, exit):")
        command = self.input_()
        if command == "buy":
            self.buy()
        elif command == "fill":
            self.fill()
        elif command == "take":
            self.take()
        elif command == "remaining":
            self.print_things()
        elif command == "exit":
            self.on = False

    def buy(self):
        print()
        print('''What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 
        back - to main menu:''')
        command = self.input_()
        if command == "back":
            pass
        else:
            ingredients = self.coffee_menu.get(command)
            if self.cups > 0 and self.water >= ingredients[0] and self.milk >= ingredients[1] and self.coffee >= \
                    ingredients[2]:
                self.cups -= 1
                self.water -= ingredients[0]
                self.milk -= ingredients[1]
                self.coffee -= ingredients[2]
                self.money += ingredients[3]
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < ingredients[0]:
                    print("Sorry, not enough water!")
                elif self.milk < ingredients[1]:
                    print("Sorry, not enough milk!")
                elif self.coffee < ingredients[2]:
                    print("Sorry, not enough coffee beans!")
                elif self.cups == 0:
                    print("Sorry, not enough disposable cups!")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(self.input_())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(self.input_())
        print("Write how many grams of coffee do you want to add:")
        self.coffee += int(self.input_())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(self.input_())
        print()

    def take(self):
        print(f"I gave you ${self.money}")
        print()
        self.money = 0


coffee_machine = CoffeeMachine()
while coffee_machine.on:
    coffee_machine.get_action()
