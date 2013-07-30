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
from game import Game

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



