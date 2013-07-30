'''
Bologna & Milano text only turn based game originally written in BASIC in the 1980's
Author: Rogerio Luz - rogeriosantosluz@gmail.com
Based on Pascal version: http://joaomorais.com.br/pascal/push.php?download=52539484
Thanks to joaomorais.com.br/usr/local/lib/python2.7/dist-packages/pybologna-0.1.2-py2.7.egg/bologna.py

v0.0.1 Simple engine to run a Text Game with few simple questions to build a Game, Players number and Players
v0.1.0 Game starts, # of players, choose players, Turns are working, economic options (buy/sell grain and land) are OK.

v0.1.1 Text to English, calculate population, better text format (tables) and screens

v0.1.2 get_input() is being used to treat input and raw_input compatibilities betweeen python 2 and 3

v0.1.3 TDD implemented. Please see the last lines of this code to run tests. 'Invasion' and 'Troops to buy' functions created. Best production random values. Invasion needs adjustments (barbarians are very efficient) and soldiers neeed to be summarized with villagers to adjust 20% militar population. 

TODO: initial variables for all levels, random values for production are very wide, need to implement market, black death, monetary, bank, maps, investments and promotions, 

'''
import sys
import random
import unittest
import time
import math

def wait(seconds):
    time.sleep(0.1)

def get_input(prompt,input_test):
    if input_test is None:
        if sys.hexversion > 0x03000000:
            return input(prompt)
        else:
            return raw_input(prompt)
    else:
        return input_test

#Class that represents a player
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

# Class that represents the Game
class Game:

    gtalk = None
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

        if self.gtalk != None:

#        self.gtalk.replyMessage("")        
#            self.gtalk.replyMessage("WELCOME TO BOLOGNA & MILANO")
#            self.gtalk.replyMessage("")
#            self.gtalk.replyMessage("")
#            self.gtalk.replyMessage("BOLOGNA & MILANO IS A FANTASTIC GAME")
#            self.gtalk.replyMessage("")
#            self.gtalk.replyMessage("")
#            self.gtalk.replyMessage("THAT WILL TEST YOUR ABILITY TO MANAGE A CITY, STATE OR A NATION")
#            self.gtalk.replyMessage("")
#            self.gtalk.replyMessage("")      

            self.gtalk.replyMessage("WELCOME TO BOLOGNA & MILANO")  

        else:

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

"""
TestGame class
"""
class TestGame(unittest.TestCase):
    """
    Basic setup, creates 4 random users, with 4 random game levels
    """
    def setUp(self):
        random_names = ['Rogerio','John','Alexander','Fiona','Shrek','Martin','Luther','Chopin']
        random_gender = ['M','F']
    	self.game = Game()
    	game_level = random.randint(1,4)
    	print "Game Level " , str(game_level)
    	self.game.choose_level(game_level)
    	players_number = random.randint(1,4)
    	print "Players Number " , str(players_number)
        self.game.players_number(players_number)
        for reg in range (0,self.game.players_num):
            self.game.choose_player(reg, random_names[random.randint(0,len(random_names)-1)], random_gender[random.randint(0,len(random_gender)-1)])

    def tearDown(self):
        #print(dir(self.game))
        #print self.game.__dict__
        pass

    """
    Test the 4 game level possibilities
    """
    def test_game_level(self):
        self.assertIn(self.game.level,range(1,5),msg="Game Level Error")
    
    """
    Test the 4 player number possibilities
    """
    def test_players_number(self):
        self.assertIn(self.game.players_num,range(1,5),msg="Players Number Error")
    
    """
    Test production and game engines simulating player actions like buy and sell grains and lands
    The game doesnt have an 'end' set, yet, so the test fail when a player is out of cash or land
    This test function acts like the game loop function called 'start_turn' so new functions need to be called here, for testing.
    """
    def test_production_mechanism(self):
        wait(1)
        for player in self.game.players:
            print("PLAYER YEAR: "+str(player.year))
            self.game.rats(player)
            self.game.random_season()
            self.game.production(player)
            self.game.economic_options(player,1)
            wait(.4)
            self.game.input_economic_option(player,1)
            if player.grain_price < 100:
                self.game.choose_economic_option(1,player,(player.cash*player.grain_price)/40) #buy grain
            else:
                self.game.choose_economic_option(1,player,1) #buy grain
            wait(.1)
            if player.grain_price > 1000:
                self.game.choose_economic_option(2,player,player.backup/4) #sell grain
            else:
                self.game.choose_economic_option(2,player,1) #sell grain
            wait(.1)
            if player.land_price < 100:
                self.game.choose_economic_option(3,player,(player.cash*player.land_price)/30) #buy land
            else:
                self.game.choose_economic_option(3,player,1) #buy land
            wait(.1)
            if player.land_price > 1000:
                self.game.choose_economic_option(4,player,1000) #sell land
            else:
                self.game.choose_economic_option(4,player,1) #sell land
            wait(.1)
            if player.cash > 100000:
                self.game.choose_economic_option(3,player,(player.cash*player.land_price)/4) #buy land
            #print "Game:", self.game.__dict__
            self.game.grains_to_people(player,max(player.backup-player.demand,0))
            #print player.__dict__
            self.game.population(player,1)
            wait(2)
            self.game.troops_to_buy(player,(player.cash/10)*0.50)
            self.failIf(player.land==0)
            self.game.invasion(player,None)
            self.game.compare(player,None)
            wait(2)
            self.failIf(player.cash<0)
            self.failIf(player.land<100)
    
    """
    Test 10 years of production mechanism calling the test above 10 times
    """
    def test_multiple_production_cicles(self):
        for cycle in range(1,10):
            self.test_production_mechanism()

    """
    Should print game results but dont know why it doesnt print
    """
    def test_final_results(self):
        print "#########################"
        print "Game:", self.game.__dict__
        for player in self.game.players:
            print "Player:", player.__dict__
        print "#########################"

"""
Starts the game, choose players and start turn while game is not over (never stops)
"""
def start_game(gtalk):
    game = Game()
    game.gtalk = gtalk
    game.show_welcome
    game.clrscr(15)
    game.choose_level(None)
    #prompts for the number of Players
    game.players_number(None)
    #for each player prompt for some questions and create players in the game
    for reg in range (0,game.players_num):
        game.choose_player(reg, None, None)
    # NOW that we have a Game and some Players we need to do something with them
    while not game.over:
        #TURNS
        game.start_turn()
        #game.over = True
    

"""
Main function to start the game
"""
def main(argv):
    start_game(None)

"""
Feel free to fix this.
Uncomment lines below to play
"""
if __name__ == "__main__":
    main(sys.argv)    


"""
Comment lines below to test the game
"""
#if __name__ == '__main__':
#    for number_of_tests in range(1):
#        unittest.main(exit=False)        

