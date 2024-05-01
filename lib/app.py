from lib.fighter import Fighter
from lib.party import Player
from lib.setup import Setup
from lib.turns import Turn
from lib.menu import Menu

class App:
    def __init__(self):
        self.setup = Setup()
        self.player = Player([Fighter.all['knight']() for _ in range(3)])

    def run(self):
        self.main_menu()
    
    def main_menu(self):
        print('Main Menu')
        print('1. New Game')
        print('2. Resume Game')
        print('3. Quit')

        Menu.choose_option(Menu.str_range(3),[
            self.stage1,
            self.resume_game,
            self.exit_program
            ])

    def stage1(self):
        "You've Started Level 1"
        enemies = self.setup.prep_stage1()
        while len(self.player.alive_fighters) > 0 and len(enemies.alive_fighters) > 0:
            Turn.player_turn(self.player,enemies)
            if not (len(self.player.alive_fighters) > 0 and len(enemies.alive_fighters) > 0):
                break
            Turn.enemy_turn(enemies,self.player.current_fighter)
        print("Level 1 Over")

    def resume_game(self):
        pass

    def exit_program(self):
        pass

