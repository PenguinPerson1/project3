from lib.menu import Menu
from lib.fighter import Fighter
from lib.exit import Exit


class Intermission:

    @classmethod
    def restart_level(cls,is_stage_1):
        print('You Died... Retry?')
        if is_stage_1:
            print('1. Retry Level')
            print('2. Save & Quit')

            if Menu.return_option(Menu.str_range(2)) == "1":
                return True
            else:
                Exit.exit_program()
                return False
        else: 
            print('1. Retry Level')
            print('2. Edit Team')
            print('3. Save & Quit')

            pivot = Menu.return_option(Menu.str_range(3))
            print(pivot)
            if pivot == "1":
                return True
            elif pivot == "2":
                cls.edit_team(None,False)
                return True
            else:
                Exit.exit_program()
                return False

    @classmethod
    def between_levels(cls,next_level):
        print('You Won!!!')
        print("Do you want to edit your team?")
        print('1. Edit Team')
        print('2. Continue to Next Round')
        print('3. Save & Quit')

        Menu.choose_option(Menu.str_range(3),[
            lambda: cls.edit_team(next_level),
            lambda: next_level(cls.player),
            Exit.exit_program
            ])
        
    @classmethod
    def edit_team(cls,next_level,is_to_next = True):
        repeat = True
        while repeat:
            print("Which Fighter would you like to replace?")
            for i, fighter in enumerate(cls.player.fighters,start=1):
                print(i,end=": ")
                print(fighter.name)

            swap_out = int(Menu.return_option(Menu.str_range(len(cls.player.fighters)))) - 1
            print(swap_out)

            print("Which fighter would you like to replace them with?")
            for i, fighter in enumerate(Fighter.available.keys(),start=1):
                print(i,end=": ")
                print(fighter)

            swap_in = int(Menu.return_option(Menu.str_range(len(Fighter.available)))) - 1

            cls.swap_fighter(swap_out,list(Fighter.available.values())[swap_in])

            print('Would you like to replace a different fighter?')
            print("1. Replace Another")
            print("2. Continue to Next Level")
            if Menu.return_option(Menu.str_range(2)) == "1":
                repeat = True
            else:
                repeat = False
        if is_to_next:
            next_level(cls.player)

    @classmethod
    def swap_fighter(cls,n_out,f_in):
        cls.player.fighters.pop(n_out)
        cls.player.fighters.insert(n_out,f_in())
        print(cls.player.fighters[n_out].name,end=" swaps with ")
        print(cls.player.fighters[-1].name)
        pass