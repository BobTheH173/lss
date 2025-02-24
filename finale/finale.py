import logging

crops = []
logfile = ""


class Farm:
    # Log and set up variables
    def __init__(self, money):
        self.land = int(5)
        self.money = int(money / difficulty)
        self.name = input("Enter the name of your new farm\n= ")

        self.cows = 0
        self.pigs = 0
        self.chickens = 0

        self.potato = 0
        self.carrot = 0
        self.beetroot = 0

        self.crops_income = int(((self.potato * 8) + (self.carrot * 4) + (self.beetroot * 20)) * (difficulty / 2))
        self.animals_income = int(((self.cows * 75) + (self.pigs * 45) + (self.chickens * 30)) * (difficulty / 2))

        self.land_occupied = self.potato + self.carrot + self.beetroot + self.cows + self.pigs + self.chickens

        self.taxes = int((self.land + self.land_occupied) +
                         (self.animals_income + self.crops_income / 100) * difficulty)

        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(message)s",
                            filemode="a",
                            filename=filename)

        logging.info(f"\nWelcome to {self.name}\n"
                     f"Your farm has:\n"
                     f"Difficulty: {difficulty}\n"
                     f"Money: {self.money} (Post tax)\n"
                     f"Total income: {self.animals_income + self.crops_income}\n"
                     f"Animals: Cows={self.cows}, Pigs={self.pigs}, Chickens={self.chickens}\n"
                     f"Land: Free={self.land}, Occupied={self.land_occupied}\n")

    def iterate(self):
        logging.info(f"\nIterating {self.name}..\n")

        self.crops_income = int(((self.potato * 8) + (self.carrot * 4) + (self.beetroot * 20)) * (difficulty / 2))
        self.animals_income = int(((self.cows * 75) + (self.pigs * 45) + (self.chickens * 30)) * (difficulty / 2))
        self.land_occupied = self.potato + self.carrot + self.beetroot + self.cows + self.pigs + self.chickens
        self.taxes = int((self.land + self.land_occupied) * difficulty * 2)

        logging.info(f"Welcome to {self.name} "
                     f"Your farm has: "
                     f"Difficulty: {difficulty} "
                     f"Money: {self.money} (Post tax) [{self.taxes}] "
                     f"Total income: {self.animals_income + self.crops_income} "
                     f"Animals: Cows={self.cows}, Pigs={self.pigs}, Chickens={self.chickens} "
                     f"Land: Free={self.land}, Occupied={self.land_occupied}")

        print(f"\nWelcome to {self.name}\n"
              f"Your farm has:\n"
              f"Difficulty: {difficulty}\n"
              f"Money: {self.money} (Post tax)\n"
              f"Total income: {self.animals_income + self.crops_income}\n"
              f"Animals: Cows={self.cows}, Pigs={self.pigs}, Chickens={self.chickens}\n"
              f"Land: Free={self.land}, Occupied={self.land_occupied}\n")

        # Choose action
        iterate_choice = int(input("Enter your action [1-4]\n"
                                   "1- Shop\n"
                                   "2- Taxes\n"
                                   "3- Pass time..\n= "))  # To save money or in emergencies
        if iterate_choice == 1:
            logging.info("Going to the shop")
            self.shop()
        elif iterate_choice == 2:
            logging.info("Going to view taxes")
            print(f"Calculated taxes to pay every income: {self.taxes}")
            input("Press any key to go back to your farm..")
            self.iterate()
        elif iterate_choice == 3:
            logging.info(f"Going to pass the time")
            print(f"You waited and received {self.crops_income} from Crops and "
                  f"{self.animals_income} from Animals\n"
                  f"Paid {self.taxes} in taxes")
            self.money += (self.animals_income + self.crops_income) - self.taxes
            self.iterate()
        else:
            logging.warning(f"Going to the wrong direction, oops")
            self.iterate()

    def shop(self):
        shop_choice = int(input("\nWelcome to the shop!\n"
                                "1- Buy animals\n"
                                "2- Buy crops\n"
                                "3- Buy land\n"
                                "4- Quit shop\n= "))
        if shop_choice == 1:
            logging.info("Going to the animal shop")
            self.shop_animals()
        elif shop_choice == 2:
            logging.info("Going to the crops shop")
            self.shop_crops()
        elif shop_choice == 3:
            logging.info("Going to the land shop")
            self.shop_land()
        elif shop_choice == 4:
            logging.info("Exiting shop..")
            self.iterate()
        else:
            self.shop()

    def shop_land(self):
        shop_land_choice = int(input("\nWhat land you want to buy?\n"
                                     "1- Buy a small field [3 Land, 100 Money]\n"
                                     "2- Buy a meadow [8 Land, 180 Money] \n"
                                     "3- Buy a rangeland [25 Land, 470 Money]\n"
                                     "4- Quit land shop\n= "))
        if shop_land_choice == 1:
            if self.money < 100:
                print("You don't have enough money (100)")
            else:
                logging.info("Bought 3 land [small field]")
                print("You bought a small field for 100 Money")
                self.money -= 100
                self.land += 3
            self.shop_land()

        elif shop_land_choice == 2:
            if self.money < 180:
                print("You don't have enough money (180)")
            else:
                logging.info("Bought 8 land [meadow]")
                print("You bought a meadow for 180 Money")
                self.money -= 180
                self.land += 8
            self.shop_land()

        elif shop_land_choice == 3:
            if self.money < 470:
                print("You don't have enough money (470)")
            else:
                logging.info("Bought 25 land [rangeland]")
                print("You bought a rangeland for 470 Money")
                self.money -= 470
                self.land += 25
            self.shop_land()

        elif shop_land_choice == 4:
            logging.info("Exiting land shop..")
            self.shop()

    def shop_crops(self):
        shop_crops_choice = int(input("\nWhat crops you want to buy?\n"
                                      "1- Buy potatoes\n"
                                      "2- Buy carrots\n"
                                      "3- Buy beetroots\n"
                                      "4- Quit animal shop\n= "))
        if shop_crops_choice == 1:
            shop_crops_choice = int(input("How many potatoes do you want to buy? [1 Potato = 10 Money, 8 Land]\n= "))
            choice_potatoes_money = shop_crops_choice * 10
            choice_potatoes_land = shop_crops_choice * 8
            if choice_potatoes_money > self.money or choice_potatoes_land > self.land:
                print(f"You don't have enough money ({choice_potatoes_money}) or land ({choice_potatoes_land})")
            else:
                logging.info(f"Bought {shop_crops_choice} potatoes")
                print(f"You bought {shop_crops_choice} Potatoes "
                      f"and spent {choice_potatoes_money} Money and {choice_potatoes_land}\n Land")
                self.money -= choice_potatoes_money
                self.land -= choice_potatoes_land
                self.potato += shop_crops_choice
            self.shop_crops()

        elif shop_crops_choice == 2:
            shop_crops_choice = int(input("How many carrots do you want to buy? [1 Carrot = 20 Money, 6 Land]\n= "))
            choice_carrots_money = shop_crops_choice * 20
            choice_carrots_land = shop_crops_choice * 6
            if choice_carrots_money > self.money or choice_carrots_land > self.land:
                print(f"You don't have enough money ({choice_carrots_money}) or land ({choice_carrots_land})")
            else:
                logging.info(f"Bought {shop_crops_choice} carrots")
                print(f"You bought {shop_crops_choice} Carrots "
                      f"and spent {choice_carrots_money} Money and {choice_carrots_land} Land\n")
                self.money -= choice_carrots_money
                self.land -= choice_carrots_land
                self.carrot += shop_crops_choice
            self.shop_crops()

        elif shop_crops_choice == 3:
            shop_crops_choice = int(input("How many carrots do you want to buy? [1 Beetroots = 50 Money, 3 Land]\n= "))
            choice_beetroots_money = shop_crops_choice * 50
            choice_beetroots_land = shop_crops_choice * 3
            if choice_beetroots_money > self.money or choice_beetroots_land > self.land:
                print(f"You don't have enough money ({choice_beetroots_money}) or land ({choice_beetroots_land})")
            else:
                logging.info(f"Bought {shop_crops_choice} beetroots")
                print(f"You bought {shop_crops_choice} Beetroots "
                      f"and spent {choice_beetroots_money} Money and {choice_beetroots_land} Land\n")
                self.money -= choice_beetroots_money
                self.land -= choice_beetroots_land
                self.beetroot += shop_crops_choice
            self.shop_crops()
        elif shop_crops_choice == 4:
            logging.info("Exiting crops shop..")
            self.shop()

    def shop_animals(self):
        shop_animals_choice = int(input("\nWhat animals you want to buy?\n"
                                        "1- Buy cows\n"
                                        "2- Buy pigs\n"
                                        "3- Buy chickens\n"
                                        "4- Quit animal shop\n= "))

        if shop_animals_choice == 1:
            shop_animals_choice = int(input("How many cows do you want to buy? [1 Cow = 350 Money, 3 Land]\n= "))
            choice_cows_money = shop_animals_choice * 350
            choice_cows_land = shop_animals_choice * 3

            if choice_cows_money > self.money or choice_cows_land > self.land:
                print(f"You don't have enough money ({choice_cows_money}) or land ({choice_cows_land})")
            else:
                logging.info(f"Bought {shop_animals_choice} cows")
                print(f"You bought {shop_animals_choice} Cows "
                      f"and spent {choice_cows_money} Money and {choice_cows_land} Land\n")
                self.money -= choice_cows_money
                self.land -= choice_cows_land
                self.cows += shop_animals_choice
            self.shop_animals()

        elif shop_animals_choice == 2:
            shop_animals_choice = int(input("How many pigs do you want to buy? [1 Pig = 225 Money, 1 Land]\n= "))
            choice_pigs_money = shop_animals_choice * 225
            choice_pigs_land = shop_animals_choice * 1

            if choice_pigs_money > self.money or choice_pigs_land > self.land:
                print(f"You don't have enough money ({choice_pigs_money}) or land ({choice_pigs_land})")
            else:
                logging.info(f"Bought {shop_animals_choice} pigs")
                print(f"You bought {shop_animals_choice} Pigs "
                      f"and spent {choice_pigs_money} Money and {choice_pigs_land} Land\n")
                self.money -= choice_pigs_money
                self.land -= choice_pigs_land
                self.pigs += shop_animals_choice
            self.shop_animals()

        elif shop_animals_choice == 3:
            shop_animals_choice = int(
                input("How many chickens do you want to buy? [1 Chicken = 105 Money, 2 Land]\n= "))
            choice_chickens_money = shop_animals_choice * 105
            choice_chickens_land = shop_animals_choice * 2

            if choice_chickens_money > self.money or choice_chickens_land > self.land:
                print(f"You don't have enough money ({choice_chickens_money}) or land ({choice_chickens_land})")
            else:
                logging.info(f"Bought {shop_animals_choice} chickens")
                print(f"You bought {shop_animals_choice} Chickens "
                      f"and spent {choice_chickens_money} Money and {choice_chickens_land} Land\n")
                self.money -= choice_chickens_money
                self.land -= choice_chickens_land
                self.chickens += shop_animals_choice
            self.shop_animals()

        elif shop_animals_choice == 4:
            logging.info("Exiting animal shop")
            self.shop()


# Set game difficulty
def setup():
    global logfile
    while True:
        try:
            game_difficulty = int(input("Enter the difficulty of the game [1-5]\n= "))
            if game_difficulty < 1:
                print("Game difficulty has been set to 1")
                game_difficulty = 1
            elif game_difficulty > 5:
                print("Game difficulty has been set to 5")
                game_difficulty = 5

            logfile = input("Enter the log file name of the game\n= ")
            return game_difficulty
        except ValueError:
            print("Please enter a valid value..")


# For less code, BUT I CAN'T SEEM TO GET IT RIGHT

# def try_choice(value):
#     global temp_choice
#     try:
#         temp_choice = input(int(value))
#     except ValueError:
#         print("Please enter a valid value..")
#         try_choice(value)
#
#     return temp_choice

# choice = try_choice("Enter something")


difficulty = setup()
filename = logfile + ".log"
own_farm = Farm(int(300))
own_farm.iterate()
