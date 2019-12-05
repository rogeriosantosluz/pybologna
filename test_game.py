import unittest
from utils import *
from game import Game
import random

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
        print("Game Level {}".format(game_level))
        self.game.choose_level(game_level)
        players_number = random.randint(1,4)
        print("Players Number {}".format(players_number))
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
        print("#########################")
        print("Game: {}".format(self.game.__dict__))
        for player in self.game.players:
            print("Player: {}".format(player.__dict__))
        print("#########################")

"""
Comment lines below to test the game
"""
if __name__ == '__main__':
    for number_of_tests in range(1):
        unittest.main(exit=False)        

