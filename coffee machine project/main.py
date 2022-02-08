class Coffee_Machine:
    running = False

    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

        if not Coffee_Machine.running:
            self.start()

    def start(self):
        self.running = True
        self.action = input("Write action (buy, report, off):\n")
        print()
        if self.action == "buy":
            self.buy()
        elif self.action == "off":
            exit()
        elif self.action == "report":
            self.status()

    def return_to_menu(self):
        print()
        self.start()

    def check_ingridients(self):
        self.not_available = ""
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee - self.reduced[2] < 0:
            self.not_available = "coffee"

        if self.not_available != "":
            print(f"Sorry, not enough {self.not_available}!")
            return False
        else:
            print("Making a coffee")
            return True

    def supplies(self):
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee -= self.reduced[2]
        self.money -= self.reduced[3]

    def buy(self):
        self.choice = input("What do you want to buy? espresso, latte, cappuccino, back - to main menu:\n")
        if self.choice == "espresso":
            self.reduced = [150, 0, 20, 3]
            if self.check_ingridients():
                self.supplies()
            print("Your espresso is done, have a good day")

        elif self.choice == "latte":
            self.reduced = [200, 35, 20, 2]
            if self.check_ingridients():
                self.supplies()
            print("Your latte is done, have a good day")

        elif self.choice == "cappuccino":
            self.reduced = [200, 75, 25, 5]
            if self.check_ingridients():
                self.supplies()
            print("Your cappuccino is done, have a good day")
        elif self.choice == "back":
            self.return_to_menu()

        self.return_to_menu()

    def status(self):
        print(f"The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee} g of coffee")
        print(f"{self.money}$ of money")
        self.return_to_menu()


Coffee_Machine(500, 300, 100, 250)
