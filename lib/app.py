from lib.setup import Setup
from lib.menu import Menu
from lib.stages import Stage
from lib.intermission import Intermission
from lib.saves import Save

class App:
    def __init__(self):
        self.player = Setup.prep_stage0()
        Intermission.player = self.player
        Save.create_table()
        Stage.player = self.player

    def run(self):
        self.main_menu()
    
    def main_menu(self):
        print('Main Menu')
        print('1. New Game')
        print('2. Resume Game')
        print('3. Quit')

        pivot = Menu.return_option(Menu.str_range(3))
        if pivot == "1":
            stage1 = Setup.prep_stage1()
            stage1.run()
        elif pivot == "2":
            self.resume_game()
        elif pivot == "3":
            Save.exit_program()

    def resume_game(self):
        pass

