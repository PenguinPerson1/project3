from lib.fighter import Fighter
from lib.party import Player
from lib.setup import Setup
from lib.menu import Menu
from lib.stages import Stage
from lib.intermission import Intermission
from lib.exit import Exit

class App:
    def __init__(self):
        self.player = Setup.prep_stage0()
        Intermission.player = self.player

    def run(self):
        self.main_menu()
    
    def main_menu(self):
        print('Main Menu')
        print('1. New Game')
        print('2. Resume Game')
        print('3. Quit')

        Menu.choose_option(Menu.str_range(3),[
            lambda: Stage.stage1(self.player),
            self.resume_game,
            Exit.exit_program
        ])

    def resume_game(self):
        pass

