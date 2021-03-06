import random
import math
from utils import *
from player import Player

"""
Class that represents the Game
"""
class Game:

    players_num = 0
    players = []
    cities = ["BOLOGNA","MILANO","VENEZA","TORINO"]
    game_level = ['1. APPRENTICE ', '2. ADVENTURER ', '3. MASTER ', '4. GREAT MASTER']
    type_of_justice = ["1 - FAIR", "2 - MODERATE", "3 - AGRESSIVE", "4 - ABUSIVE"]
    level = 0

    season = None
    seasons = ['DROUGHT - THREAT OF HUNGER! ',' BAD WEATHER - POOR CROP ',' TIME ONLY - REASONABLE CROP ',' GOOD TIME - GOOD HARVEST ',' GREAT WEATHER - GREAT HARVEST']

    over = False

    def __init__(self):
        pass

    def show_welcome(self):
        self.clrscr(15)

        print("")
        print("")        
        print("WELCOME TO BOLOGNA & MILANO")
        print("")
        print("")
        print("BOLOGNA & MILANO IS A FANTASTIC GAME")
        print("")
        print("")
        print("THAT WILL TEST YOUR ABILITY TO MANAGE A CITY, STATE OR A NATION")
        print("")
        print("")        

    def players_number(self,input_test):
        self.clrscr(40)
        print("PLAYERS")
        self.clrscr(10)
        try:
            self.players_num = int( get_input("How much players will play? (up to 4): ",input_test) )
            if (self.players_num < 1 or self.players_num > 4):
                self.players_number()
        except ValueError:
            print("Invalid number of players.")
            self.players_number()

    #Prompt player to few questions        
    def choose_player(self, reg, name, gender):
        self.clrscr(40)
        print("CHOOSE PLAYER")
        self.clrscr(10)
        #print("Player #"+str(reg+1))
        print("Welcome Governor of "+self.cities[reg])
        player = Player()
        player.city = self.cities[reg]
        player.input_name(name)
        player.input_gender(gender)
        #player.input_age()
        #player.show_player(reg)

        # we need to initialize some variables accordinly to the level of the game
        if self.level in range(1,5):
            player.population = 1000
            player.production = 0
            player.rats = 0
            player.cash = 10000
            player.demand = 0
            player.backup = 10000
            player.land = 10000
            player.gain = 0
            player.soldiers = 500
            player.nobles = 0
            player.bishops = 0
            player.sellers = 0
            player.settlers = 0
            player.bank_interest = 5

        self.players.insert(reg,player)

    def show_instructions(self):
        print('A PARTIR DE AGORA  VOCE SERA O GOVERNANTE DE UMA CIDADE-ESTADO DO SECULO  XV.')
        print('A CADA PERIODO DE BOM GOVERNO VOCE RECEBERA TITULOS CADA VEZ MAIORES.');
        print('A EXPECTATIVA DE VIDA NAQUELA EPOCA ERA MUITO CURTA, LOGO VOCE DISPORA DE');
        print('POUCO TEMPO PARA GOVERNAR.');
        print('QUEM PRIMEIRO CHEGAR A REI OU RAINHA SERA O VENCEDOR DO JOGO.');
        print('O TAMANHO DA TORRE NO CANTO SUPERIOR ESQUERDO INDICARA SE SUAS DEFESAS SAO');
        print('ADEQUADAS.');
        print('O TERMOMETRO INDICA SE SUAS TERRAS ESTAO EM FRANCA PRODUCAO, CASO CONTRARIO');
        print('VOCE PRECISARA DE MAIS SERVOS.');
        print('UMA BOA DISTRIBUICAO DE GRAOS A POPULACAO, AUMENTARA  A TAXA DE NATALIDADE E');
        print('INCENTIVARA A MIGRACAO DE NOVOS SERVOS.');
        print('TAXAS E IMPOSTOS ELEVADOS, AUMENTAM A ARRECADACAO MAS AFETAM A ECONOMIA DA');
        print('NACAO.');
        print('FACA UM GOVERNO DEMOCRATICO E LEMBRE-SE QUE, SEMPRE BOM COMPRAR NA BAIXA PARA');
        print('VENDER NA ALTA.');
        print('GOOD LUCK!');

    def choose_level(self,input_test):
        print("GAME LEVEL")
        for level in self.game_level:
            print(level)

        try:
            self.level = int( get_input("Please Choose Game Level (1 to 4): ",input_test) )
            if (self.level < 1 or self.level > 4):
                self.choose_level(input_test)
        except ValueError:
            print("Invalid level.")
            self.choose_level(input_test)

    # In agriculture, the harvest is the process of gathering mature crops from the fields. 
    def show_season(self):
        print("Season:"+ self.season)

    def rats(self, player):

        if self.level == 0:
            player.rats = int(random.uniform(10,20))
        elif self.level == 1:
            player.rats = int(random.uniform(20,30))
        elif self.level == 2:
            player.rats = int(random.uniform(3,40))
        elif self.level == 3:
            player.rats = int(random.uniform(40,50))
        elif self.level == 4:
            player.rats = int(random.uniform(50,60))

        player.backup = player.backup - ( ( player.backup * player.rats ) / 100 )

    def random_season(self):
        self.season = random.choice(self.seasons)  

    def production(self, player):
        player.year += 1

        if self.level == 0:
            player.production_rate = int(random.uniform(10,20) + (math.sqrt(player.land)/10))
        elif self.level == 1:
            player.production_rate = int(random.uniform(5,10) + (math.sqrt(player.land)/10))
        elif self.level == 2:
            player.production_rate = int(random.uniform(3,10) + (math.sqrt(player.land)/10))
        elif self.level == 3:
            player.production_rate = int(random.uniform(2,10) + (math.sqrt(player.land)/10))
        elif self.level == 4:
            player.production_rate = int(random.uniform(1,10) + (math.sqrt(player.land)/10))

        if self.season == self.seasons[0]:
            #player.production_rate = player.production_rate - ( ( player.production_rate * 100 ) / 100 )
            player.land_price = int(random.uniform(player.production_rate,100) * player.production_rate) / 100
            player.grain_price = int(random.uniform(40,50) * player.production_rate) / 100
        elif self.season == self.seasons[1]:
            player.production_rate = player.production_rate - ( ( player.production_rate * 80 ) / 100 )
            player.land_price = int(random.uniform(100,200) * player.production_rate)
            player.grain_price = int(random.uniform(30,40) * player.production_rate)
        elif self.season == self.seasons[2]:
            player.production_rate = player.production_rate - ( ( player.production_rate * 60 ) / 100 )
            player.land_price = int(random.uniform(200,300) * player.production_rate)
            player.grain_price = int(random.uniform(20,30) * player.production_rate)
        elif self.season == self.seasons[3]:
            player.production_rate = player.production_rate - ( ( player.production_rate * 40 ) / 100 )
            player.land_price = int(random.uniform(300,400) * player.production_rate)
            player.grain_price = int(random.uniform(10,20) * player.production_rate)
        elif self.season == self.seasons[4]:
            player.production_rate = player.production_rate - ( ( player.production_rate * 20 ) / 100 )
            player.land_price = int(random.uniform(400,500) * player.production_rate)
            player.grain_price = int(random.uniform(1,10) * player.production_rate)

        player.production = int( player.backup + ( ( player.backup * player.production_rate ) / 100 ) )

        player.backup = int ( player.backup + player.production )

        player.demand = int (player.population + ( ( player.population * player.production_rate ) / 100 ) )


    def economic_options(self, player, input_test):
        player.show_player()
        self.clrscr(20)
        print("Year:" +str(player.year))
        print("")
        print("RATS ATE "+str(player.rats)+"% OF YOUR GRAIN STORAGE RESERVE")
        print("")
        print("Season:"+ self.season)
        print("")
        print("PRODUCTION "+str(player.production)+ " BAGS")
        print("")
        print("Production rate: "+str(player.production_rate)+"%")
        print("")
        print('GRAIN      GRAIN       GRAIN      LAND        CASH')
        print('RESERVE    DEMAND      PRICE      PRICE');
        values = ""
        values = str(player.backup).ljust(11)
        values = values +  str(player.demand).ljust(12)  
        values = values +  str(player.grain_price).ljust(11)
        values = values +  str(player.land_price).ljust(12)      
        values = values +  str(player.cash).ljust(7)                
        #print(str(player.backup)+"       "+str(player.demand)+"         "+str(player.grain_price)+"        "+str(player.land_price)+"      "+str(player.cash))
        print(values)
        print('BAGS       BAGS        BAG        ACRE        FLORINS')
        print("")
        print('       ECONOMIC OPTIONS')
        print('       =================')
        print('       1. BUY GRAIN ')
        print('       2. SELL GRAIN ')
        print('       3. BUY LANDS')
        print('       4. SELL LANDS')
        print('       0. CONTINUE     ')
        print("")
        print("LAND ==> "+str(player.land)+" ACRE")
        print("POPULATION    ==> "+str(player.population)+"")

        if input_test is None:    
            self.input_economic_option(player, input_test)        

    def input_economic_option(self, player, input_test):
        try:
            player.economic_option = int( get_input("Option? (0 to 4): ",input_test) )
            if (player.economic_option < 0 or player.economic_option > 4):
                self.input_economic_option(player)
        except ValueError:
            print("Invalid seconomic_option.")
            self.input_economic_option(player, input_test)

        if input_test is None:    
            self.choose_economic_option(player.economic_option, player, input_test)

    def choose_economic_option(self, option, player, input_test):
        if option == 1:
            self.buy_grain(player, input_test)
            self.economic_options(player, input_test)
        elif option == 2:
            self.sell_grain(player, input_test)
            self.economic_options(player, input_test)
        elif option == 3:
            self.buy_land(player, input_test)
            self.economic_options(player, input_test)
        elif option == 4:
            self.sell_land(player, input_test)
            self.economic_options(player, input_test)
        elif option == 0:
            None


    def buy_grain(self, player, input_test):
        try:
            player.grain_to_buy = int( get_input("How much grain will you buy?: ",input_test) )
            if (player.grain_to_buy < 0):
                self.buy_grain(player)
            if player.grain_price * player.grain_to_buy >  player.cash:
                can_buy = player.cash / player.grain_price
                print("You dont have Cash to buy so much grain, you can buy up to "+str(int(can_buy))+ " grains")
                player.cash -= ( player.grain_price * can_buy )
                player.backup += can_buy
                print("You bought "+str(can_buy)+" grains")
                wait(1)
                return

            player.cash -= ( player.grain_price * player.grain_to_buy )
            player.backup += player.grain_to_buy
            print("You bought "+str(player.grain_to_buy)+" grains")
            wait(1) 
        except ValueError:
            print("Invalid number of grains.")
            self.buy_grain(player, input_test)

    def sell_grain(self, player, input_test):
        try:
            player.grain_to_sell = int( get_input("How much grain will you sell?: ",input_test) )
            if (player.grain_to_sell < 0):
                self.sell_grain(player)
            if player.backup < player.grain_to_sell:
                print("You cant sell more than "+str(player.backup)+ " grains")
                #self.sell_grain(player)
                player.cash += ( player.backup * player.grain_price ) 
                print("You sold ALL your "+str(player.backup)+" grains")
                player.backup = 0
                wait(1)
                return

            player.backup -= player.grain_to_sell
            player.cash += ( player.grain_to_sell * player.grain_price )
            print("You sold "+str(player.grain_to_sell)+" grains")
            wait(1) 
        except ValueError:
            print("Invalid number of grains.")
            self.sell_grain(player, input_test)

    def buy_land(self, player, input_test):
        try:
            player.land_to_buy = int( get_input("How much land will you buy?: ",input_test) )
            if player.land_to_buy < 0:
                self.buy_land(player)
            if player.cash < ( player.land_to_buy * player.land_price ):
                can_buy = int( player.cash /  player.land_price)
                print("Buddy, you can buy up to "+ str(can_buy) + " ACRES")
                #self.buy_land(player)
                player.cash -= ( can_buy * player.land_price )
                player.land += can_buy
                print("You bought "+str(can_buy)+" ACRES")
                wait(1)
                return

            player.cash -= ( player.land_to_buy * player.land_price )
            player.land += player.land_to_buy
            print("You bought "+str(player.land_to_buy)+" ACRES")
            wait(1)
        except ValueError:
            print("Invalid number of ACRES.")
            self.buy_land(player, input_test)

    def sell_land(self, player, input_test):
        try:
            player.land_to_sell = int( get_input("How much land will you sell?: ", input_test) )
            if player.land_to_sell < 0:
                self.sell_land(player)
            #Cant sell more than 50% of the land at a minimum of 1000 ACRES
            if ( ( player.land_to_sell > ( player.land * 0.5 ) ) or ( player.land - player.land_to_sell < 1000 )) :
                print("Please sell less land... remember you need land for agriculture... ")
                #self.sell_land(player)
                return
            player.land -= player.land_to_sell
            player.cash += player.land_to_sell * player.land_price
            print("You sold "+str(player.land_to_sell)+" ACRES")

        except ValueError:
            print("Invalid number of ACRES.")
            self.sell_land(player, input_test)

    def grains_to_people(self, player, input_test):
        try:
            player.grains_to_people = int( get_input("How much grains will you give to your people ?: ", input_test) )
            if (player.grains_to_people < 0):
                self.grains_to_people(player)
            twenty_percent = int( player.backup * ( 0.2 ) )
            if ( player.backup - player.grains_to_people) < twenty_percent:
                can_give = player.backup - twenty_percent
                print("You need to keep 20% ("+ str(twenty_percent) +" grains) for your stock. So you can give up to "+str(can_give)+ " of grains.")
                #self.grains_to_people(player)
                player.grains_to_people = can_give
                player.backup = player.backup - player.grains_to_people
                print("You gave to people "+str(can_give)+" grains")
                return

            player.backup = player.backup - player.grains_to_people
            print("You gave to people "+str(player.grains_to_people)+" grains")

        except ValueError:
            print("Invalid number of grains.")
            self.grains_to_people(player, input_test)

    def count_births(self, player):
        if player.grains_to_people > player.demand:
            player.births = int ( ( player.population * random.uniform( 1, 100 ) ) / 100 )
        else:
            player.births = int ( ( player.population * ( random.uniform( 1, player.grains_to_people / player.demand ) / 100 ) ) ) 
        print(str(player.births)+" villagers born this season")

    def count_deaths(self, player):
        if player.grains_to_people > player.demand:
            player.deaths = int ( player.births * ( random.uniform( 1, 10 ) / 100 ) )
        else:
            if player.births < 10:
                player.deaths = int ( player.population * ( random.uniform( 10, 50 )  / 100 ) ) 
            else:
                player.deaths = int ( player.births * ( random.uniform( 10, 50 ) ) ) 
        print(str(player.deaths)+" villagers died this season")

    def count_immigrants(self, player):
        if player.grains_to_people > player.demand:
            player.immigrants = int ( ( player.population * ( random.uniform( 1, player.grains_to_people / player.demand ) / 100 ) ) )
        else:
            player.immigrants = 0
        print(str(player.immigrants) + " villagers moved to your country this season")

    def count_emigrants(self, player):
        if player.grains_to_people < player.demand:
            player.emigrants = int ( player.population * ( random.uniform( 1, player.production_rate ) / 100 ) )
        else:
            player.emigrants = 0
        print(str(player.emigrants) + " villagers moved to neighbor countries this season")

    def count_settlers(self, player):
        player.population += player.births - player.deaths + player.immigrants - player.emigrants 
        print(" This season your country has a population of "+str(player.population)+" settlers")

    def population(self, player, input_test):
        if input_test is None:
            self.clrscr(40)
        player.show_player()
        self.clrscr(10)
        print("Year:" +str(player.year))
        self.count_births(player)
        self.count_deaths(player)
        self.count_immigrants(player)
        self.count_emigrants(player)
        self.count_settlers(player)

    def invasion(self, player, input_test):
        if self.level == 0:
            player.invasion_rate = max ( int ( random.uniform(10,20) - float(player.soldiers) / 100) , 1)
        elif self.level == 1:
            player.invasion_rate =  max ( int ( random.uniform(20,30) - float(player.soldiers) / 100) , 1)
        elif self.level == 2:
            player.invasion_rate =  max ( int ( random.uniform(30,40) - float(player.soldiers) / 100) , 1)
        elif self.level == 3:
            player.invasion_rate =  max ( int ( random.uniform(40,50) - float(player.soldiers) / 100) , 1)
        elif self.level == 4:
            player.invasion_rate =  max ( int ( random.uniform(50,60) - float(player.soldiers) / 100) , 1)


        player.lands_lost = int (player.land * player.invasion_rate / 100 )
        player.soldiers_lost = int (player.soldiers * player.invasion_rate / 100 )

        player.land -= player.lands_lost
        player.soldiers -= player.soldiers_lost

        self.clrscr(40)
        player.show_player()
        self.clrscr(10)

        print("Year:" +str(player.year))

        print("Barbarians invaded your land and attached "+str(player.lands_lost)+" ACRES")
        print("You lost "+str(player.soldiers_lost)+" soldiers in the battlefield. Now you have "+str(player.soldiers))

    def market(self, player, input_test):
        self.clrscr(40)
        player.show_player()
        self.clrscr(10) 
        print("Your markets profit were "+str(player.markets_profit)+" Florins")
        print("Your mills  profit were "+str(player.mills_profit)+" Florins")
        print("Military expenses were "+str(player.military_expenses)+" N Florins")

    #The Black Death was one of the most devastating pandemics in human history, peaking in Europe between 1348 and 1350
    def black_death(self, player, input_test):
        self.clrscr(40)
        player.show_player()
        print("")
        print(' **** BLACK DEATH ****')
        print("")
        print('THE BLACK DEATH DEVASTATED YOUR CIY KILLING:')
        print(str(player.black_death_nobles) + '   NOBRES +')
        print(str(player.black_death_bishops) + '   BISPOS E PADRES +')
        print(str(player.black_death_sellers) + '   COMERCIANTES +')
        print(str(player.black_death_settlers) + '   SERVOS +')

    def bank(self, player, input_test):
        self.clrscr(40)
        player.show_player()
        self.clrscr(10)
        print("Banks charged you in "+ str(player.bank_interest) + "% INTEREST ON DEBT")

    def monetary(self, player, input_test):
        self.clrscr(40)
        player.show_player()
        self.clrscr(10)
        print('STATE GAIN: ' +str(player.gain)+ ' FLORINS')
        print('***************')
        print('CUSTOMS  SELLING  OTHER  JUSTICE')
        print('TAXES    TAXES    TAXES  (TYPE)')
        print("")
        print('    '+str(player.customs_taxes)+'%     '+str(player.selling_taxes)+'%        '+str(player.taxes)+'%     '+str(player.justice))
        print("")
        print('    '+str(player.customs_taxes_profit)+'      '+str(player.selling_taxes_profit)+'         '+str(player.taxes_profit)+'      '+str(player.total_profit))
        print('FLORINS  FLORINS    FLORINS    FLORINS')
        print("")
        print('         MONETARY OPTIONS')
        print('         ==================')
        print('         1. CUSTOM TAXES')
        print('         2. SELLING TAXES     ')
        print('         3. OTHER TAXES  ')
        print('         4. TYPE OF JUSTICE  ')
        print('         0. CONTINUE          ')
        print("")

    def input_monetary_option(self, player, input_test):
        try:
            player.monetary_option = int( get_input("Option? (0 to 4): ", input_test) )
            if (player.monetary_option < 0 or player.monetary_option > 4):
                self.input_monetary_option(player, input_test)
        except ValueError:
            print("Invalid  monetary option.")
            self.input_monetary_option(player, input_test)

        self.choose_monetary_option(player.economic_option, player, input_test)

    def choose_monetary_option(self, option, player, input_test):
        if option == 1:
            self.customs_taxes(player, input_test)
        elif option == 2:
            self.selling_taxes(player, input_test)
        elif option == 3:
            self.taxes(player, input_test)
        elif option == 4:
            self.justice(player, input_test)
        elif option == 0:
            None

    def customs_taxes(self, player, input_test):
        try:
            player.customs_taxes = int( get_input("What is the new customs taxes (0 To 100%) ?: ", input_test) )
            if (player.customs_taxes < 0 or player.customs_taxes > 100):
                self.customs_taxes(player, input_test)
        except ValueError:
            print("Invalid number of %.")
            self.customs_taxes(player, input_test)        

    def selling_taxes(self, player, input_test):
        try:
            player.selling_taxes = int( get_input("What is the new selling_taxes (0 To 50%) ?: ", input_test) )
            if (player.selling_taxes < 0 or player.selling_taxes > 50):
                self.selling_taxes(player, input_test)
        except ValueError:
            print("Invalid number of %.")
            self.selling_taxes(player, input_test)

    def taxes(self, player, input_test):
        try:
            player.taxes = int( input("What is the new taxes (0 To 25%) ?: ") )
            if (player.taxes < 0 or player.selling_taxes > 25):
                self.taxes(player, input_test)
        except ValueError:
            print("Invalid number of %.")
            self.taxes(player, input_test)

    def justice(self, player, input_test):
        for justice in self.type_of_justice:
            print(justice)
        try:
            player.justice = int( get_input("Choose the kind of Justice (1 to 4): ", input_test) )
            if (player.justice < 1 or player.justice > 4):
                self.justice(player, input_test)
        except ValueError:
            print("Invalid option.")
            self.justice(player, input_test)

    def investments(self, player, input_test):
        self.clrscr(40)
        player.show_player()
        self.clrscr(10)

        print('STATE INVESTMENTS:')
        print('***********************')
        print('1. MARKETS   (1000 FLORINS, EACH)')
        print('2. MILLS     (2000 FLORINS, EACH)')
        print('3. PALACE    (3000 FLORINS, EACH PART)')
        print('4. CATHEDRAL (5000 FLORINS, EACH PART)')
        print('5. MILITARY COSTS (500 FLORINS, TO FORM A TROOP)')
        print('6. COMPARE')
        print('7. MAP')
        print('0. CONTINE')
        print
        print('AVAILABLE CASH: '+str(player.cash)+' FLORINS')

    def input_investments_option(self, player, input_test):
        try:
            player.investments_option = int( get_input("Option? (0 to 7): ", input_test) )
            if (player.investments_option < 0 or player.investments_option > 7):
                self.input_investments_option(player, input_test)
        except ValueError:
            print("Invalid investments option.")
            self.input_investments_option(player, input_test)

        self.choose_investments_option(player.investments_option, player, input_test)        

    def choose_investments_option(self, option, player, input_test):
        if option == 1:
            self.markets_to_buy(player)
        elif option == 2:
            self.mills_to_buy(player)
        elif option == 3:
            self.palaces_to_buy(player)
        elif option == 4:
            self.cathedral_to_buy(player)
        elif option == 5:
            self.troops_to_buy(player)
        elif option == 6:
            self.compare(player)
        elif option == 7:
            self.map(player)
        elif option == 0:
            None

    def markets_to_buy(self, player, input_test):
        try:
            player.markets_to_buy = int( get_input("How much markets will you buy?: ", input_test) )
            if (player.markets_to_buy < 0 or player.markets_to_buy > 10000):
                self.markets_to_buy(player, input_test)
        except ValueError:
            print("Invalid number of markets.")
            self.markets_to_buy(player, input_test)        

    def mills_to_buy(self, player, input_test):
        try:
            player.mills_to_buy = int( get_input("How much mills will you buy?: ", input_test) )
            if (player.mills_to_buy < 0 or player.mills_to_buy > 10000):
                self.mills_to_buy(player, input_test)
        except ValueError:
            print("Invalid number of mills.")
            self.mills_to_buy(player, input_test)

    def palace_to_buy(self, player, input_test):
        try:
            player.palace_to_buy = int( get_input("How much palace will you buy?: ", input_test) )
            if (player.palace_to_buy < 0 or player.palace_to_buy > 10000):
                self.palace_to_buy(player, input_test)
        except ValueError:
            print("Invalid number of palace.")
            self.palace_to_buy(player, input_test)                

    def cathedral_to_buy(self, player, input_test):
        try:
            player.cathedral_to_buy = int( get_input("How much cathedral will you buy?: ", input_test) )
            if (player.cathedral_to_buy < 0 or player.cathedral_to_buy > 10000):
                self.cathedral_to_buy(player, input_test)
        except ValueError:
            print("Invalid number of cathedral.")
            self.cathedral_to_buy(player, input_test)

    def troops_to_buy(self, player, input_test):
        try:
            soldier_price = max(int(float(player.invasion_rate)-(float(player.invasion_rate)*float(player.population/100)/float(player.population/(player.population/100)*10))),10)
            print("The price of a soldier is " + str(soldier_price))#str(max(player.invasion_rate * 10,10)))
            wait(3)
            #soldier_price = max(player.invasion_rate * 10,10)
            twenty_percent = int( player.population * ( 0.2 ) )
            player.troops_to_buy = int( get_input("How much soldiers will you buy?: ", input_test) )
            if (player.troops_to_buy > twenty_percent or player.cash < player.troops_to_buy * soldier_price):
                can_buy = twenty_percent
                if can_buy * soldier_price < player.cash:
                    print("Soldiers are limited in 20% ("+ str(twenty_percent) +" soldiers) of your population. So you bought "+str(can_buy)+ " of soldiers.")
                else:
                    can_buy = player.cash / soldier_price
                    print("You dont have money to buy " + str(player.troops_to_buy) + " so you bougth " + str(can_buy) + " soldiers to your troop of " + str(player.soldiers) + "soldiers")
                wait(1)
                player.soldiers += can_buy
                player.cash -= can_buy * soldier_price
                return

            player.soldiers += player.troops_to_buy
            player.cash -= player.troops_to_buy * soldier_price

        except ValueError:

            print("Invalid number of troops.")
            self.troops_to_buy(player, input_test)

    def compare(self, player, input_test):
        print("Year:" +str(player.year))
        print('NOB   SOL   CLE   COM   SERV    ACRE       CASH ');
        print('====================================================');
        print(str(player.nobles).ljust(6)+str(player.soldiers).ljust(6)+str(player.bishops).ljust(6)+str(player.sellers).ljust(6)+str(player.population).ljust(8)+str(player.land).ljust(11)+str(player.cash))

    def map(self, player):
        print("MAP...")

    def promotion(self, player, input_test):
        self.clrscr(40)
        player.show_player()
        self.clrscr(10)
        print("")
        print("*******  CONGRATULATIONS *******")
        self.clrscr(5)
        print("You are now "+ player.show_title() + "of "+ player.city)

    def press_any_key(self, input_test):
        try:
            pressed = get_input("Press any key to Continue or Q to quit the game... ", input_test)
            if (pressed == "Q"):
                self.over = True
        except ValueError:
            print("Invalid key")
            self.press_any_key(input_test)        

    def clrscr(self,lines):
        for i in range(1, lines):
            print("")             

    """
    This is the heart of the game that runs every turn for each player. Need to be tested in the same order of events.
    """
    def start_turn(self):
        for player in self.players:
            self.clrscr(25)

            #We need to calculate production values according to the season and difficulty level
            # % of losts with rats
            self.rats(player)
            self.random_season()
            self.production(player)

            self.economic_options(player,None)
            self.grains_to_people(player,None)
            self.population(player,None)
            self.press_any_key(None)
            self.troops_to_buy(player,None)
            self.press_any_key(None)
            self.invasion(player,None)
            self.press_any_key(None)
            self.compare(player,None)
            self.press_any_key(None)
            self.market(player,None)
            self.press_any_key(None)
            self.black_death(player,None)
            self.press_any_key(None)
            self.monetary(player,None)
            self.input_monetary_option(player,None)
            self.bank(player,None)
            self.press_any_key(None)            
            self.investments(player,None)
            self.input_investments_option(player,None)
            self.bank(player,None)
            self.press_any_key(None)
            self.promotion(player,None)
            self.press_any_key(None)            


