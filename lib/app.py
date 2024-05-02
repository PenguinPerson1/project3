from lib.fighter import Fighter
from lib.party import Player
from lib.setup import Setup
from lib.turns import Turn
from lib.menu import Menu

class App:
    def __init__(self):
        self.setup = Setup()
        self.player = Player([Fighter.all['knight']() for _ in range(3)])
        self.restart = True

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
        enemies = self.setup.prep_stage1()
        while self.restart == True:
            print("You've Started Level 1")
            if Turn.battle_loop(self.player,enemies):
                self.between_levels(self.stage2)
            else: self.restart_level(self.stage1)

    def stage2(self):
        print("stage 2")

    def restart_level(self,level):
        print('You Died... Retry?')
        if level == self.stage1:
            print('1. Retry Level')
            print('2. Save & Quit')

            Menu.choose_option(Menu.str_range(2),[
                lambda: None,
                self.exit_program
                ])

    def between_levels(self,next_level):
        print('You Won!!!')
        self.restart = False
        print("Do you want to edit your team?")
        print('1. Edit Team')
        print('2. Continue to Next Round')
        print('3. Save & Quit')

        Menu.choose_option(Menu.str_range(3),[
            lambda: self.edit_team(next_level),
            next_level,
            self.exit_program
            ])
        
    def edit_team(self,next_level):
        repeat = True
        while repeat:
            print("Which Fighter would you like to replace?")
            for i, fighter in enumerate(self.player.fighters,start=1):
                print(i,end=": ")
                print(fighter.name)

            swap_out = int(Menu.return_option(Menu.str_range(len(self.player.fighters)))) - 1
            print(swap_out)

            print("Which fighter would you like to replace them with?")
            for i, fighter in enumerate(Fighter.all.keys(),start=1):
                print(i,end=": ")
                print(fighter)

            swap_in = int(Menu.return_option(Menu.str_range(len(self.player.fighters)))) - 1
            print(swap_in)

            self.swap_fighter(swap_out,list(Fighter.all.values())[swap_in])

            print('Would you like to replace a different fighter?')
            print("1. Replace Another")
            print("2. Continue to Next Level")
            if Menu.return_option(Menu.str_range(2)) == "1":
                repeat = True
            else:
                repeat = False
        next_level()

    def swap_fighter(self,n_out,f_in):
        self.player.fighters.pop(n_out)
        self.player.fighters.insert(n_out,f_in())
        print(self.player.fighters[n_out].name,end=" swaps with ")
        print(self.player.fighters[-1].name)
        pass

    def resume_game(self):
        pass

    def exit_program(self):
        self.restart = False
        print("goodbye!")

