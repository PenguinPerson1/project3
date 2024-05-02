from lib.fighter import Fighter
from lib.party import Player
from lib.setup import Setup
from lib.menu import Menu
from lib.stages import Stage
from lib.intermission import Intermission
from lib.exit import Exit

class App:
    def __init__(self):
        # self.setup = Setup()
        Setup.prep_stage0()
        self.player = Player([Fighter.all['knight']() for _ in range(3)])
        Intermission.player = self.player

    def run(self):
        self.main_menu()

        
        Exit.exit_program()
    
    def main_menu(self):
        print('Main Menu')
        print('1. New Game')
        print('2. Resume Game')
        print('3. Quit')

        pivot = Menu.return_option(Menu.str_range(3))
        if pivot == "1":
            Stage.stage1(self.player)

    def resume_game(self):
        pass

