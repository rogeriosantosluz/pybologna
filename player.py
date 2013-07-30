from utils import get_input

"""
Class that represents a player
"""
class Player:

    #gender = None
    #name = ""

    year = 1300

    title = 0
    title_male = ['Knight ', 'Baron ', 'Viscount ', 'Count ', 'Marquess ', 'Duke ', 'Grand Duke ', 'Archiduke', '* KING * ', '** EMPEROR **']
    title_female = ['Dame ','Baroness ','Viscountess ', 'Countess ', 'Marchioness ','Duchess ','Grand Duchess ','Archduchess ','* QUEEN * ','* EMPRESS * ']

    city = None

    land_price = 0
    grain_price = 0    

    production = 0
    production_rate = 0
    rats = 0
    cash = 0
    demand = 0
    backup = 0
    land = 0

    gain = 0
   
    economic_option = 0
    economic_options = []

    grain_to_buy = 0
    grain_to_sell = 0
    land_to_buy = 0
    land_to_sell = 0

    grains_to_people = 0

    invasion_rate = 0
    lands_lost = 0
    soldiers = 0
    soldiers_lost = 0

    births = 0
    deaths = 0
    immigrants = 0
    emigrants = 0
    
    black_death_nobles = 0
    black_death_bishops = 0
    black_death_sellers = 0
    black_death_settlers = 0
    nobles = 0
    bishops = 0
    sellers = 0
    settlers = 0
    population = 0
 
    markets_profit = 0
    mills_profit = 0
    military_expenses = 0

    customs_taxes = 0
    selling_taxes = 0
    taxes = 0
    justice = None

    customs_taxes_profit = 0
    selling_taxes_profit= 0
    taxes_profit = 0
    total_profit = 0

    bank_interest = 0

    monetary_option = 0

    investments_option = 0
    
    is_playing = True

    #def __init__(self):
        #print("Player Iniciado")

    def input_gender(self,input_test):
        self.gender = get_input("Please type your gender(M/F): ",input_test)
        if self.gender != "M" and self.gender != "F":
            self.input_gender()

    def input_age(self,input_test):
        try:
            self.age = int( get_input("Please type your age in years (1 to 110): ",input_test) )
            if (self.age < 1 or self.age > 110):
                self.input_age()
        except ValueError:
            print("Invalid age.")
            self.input_age()

    def input_name(self,input_test):
        self.name = get_input("What is your name:",input_test)

    def show_title(self):
        if self.gender == "M":
            return self.title_male[self.title]
        else:
            return self.title_female[self.title]
        
    def show_player(self, reg=0):
        print(self.show_title()+self.name)


