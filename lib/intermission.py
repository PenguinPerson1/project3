from lib.menu import Menu
from lib.fighter import Fighter
from lib.saves import Save


class Intermission:
    RETRY_OPTIONS = ["retry","retry level"]
    EDIT_OPTIONS = ["edit","edit team"]
    SAVE_OPTIONS = ["save","quit","save and quit","save & quit"]
    CONTINUE_OPTIONS = ["continue","next","continue to next round"]

    @classmethod
    def restart_level(cls,num_level):
        print('You Died... Retry?')
        cls.num_level = num_level-1
        if num_level == 1:
            print('1. Retry Level')
            print('2. Quit')

            pivot = Menu.return_option(Menu.add_nums([cls.RETRY_OPTIONS,["quit"]]))

            if pivot == 0:
                return True
            else:
                Save.exit_program()
                return False
        else: 
            print('1. Retry Level')
            print('2. Edit Team')
            print('3. Save & Quit')

            pivot = Menu.return_option(Menu.add_nums([
                cls.RETRY_OPTIONS,
                cls.EDIT_OPTIONS,
                cls.SAVE_OPTIONS
            ]))

            if pivot == 0:
                return True
            elif pivot == 1:
                cls.edit_team()
                return True
            elif pivot == 2:
                Save.save_exit(cls.num_level,cls.player)
                return False

    @classmethod
    def between_levels(cls,num_level):
        cls.num_level = num_level
        from lib.setup import Setup
        next_level = Setup.ALL[num_level+1]()
        print("Do you want to edit your team?")
        print('1. Edit Team')
        print('2. Continue to Next Round')
        print('3. Save & Quit')

        pivot = Menu.return_option(Menu.add_nums([
            cls.EDIT_OPTIONS,
            cls.CONTINUE_OPTIONS,
            cls.SAVE_OPTIONS
        ]),)
        if pivot == 2:
            Save.save_exit(cls.num_level,cls.player)
        else:
            if pivot == 0: 
                cls.edit_team()
            next_level.run()
        
    @classmethod
    def edit_team(cls):
        repeat = True
        while repeat:
            print("Which Fighter would you like to replace?")
            for i, fighter in enumerate(cls.player.fighters,start=1):
                print(i,end=": ")
                print(fighter.name)

            swap_out = Menu.return_option(Menu.add_nums([[fighter.name] for fighter in cls.player.fighters]))
            print(swap_out)

            print("Which fighter would you like to replace them with?")
            for i, fighter in enumerate(Fighter.available.keys(),start=1):
                print(i,end=": ")
                print(fighter)

            swap_in = Menu.return_option(Menu.add_nums([[fighter] for fighter in Fighter.available]))

            cls.swap_fighter(swap_out,list(Fighter.available.values())[swap_in])

            print('Would you like to replace a different fighter?')
            print("1. Replace Another")
            print("2. Continue to Next Level")
            print("3. Save and Quit")

            pivot = Menu.return_option(Menu.add_nums([
                ["replace","another","replace another"],
                cls.CONTINUE_OPTIONS,
                cls.SAVE_OPTIONS
            ]))
            if pivot == 0:
                repeat = True
            elif pivot == 1:
                repeat = False
            elif pivot == 2:
                Save.save_exit(cls.num_level,cls.player)

    @classmethod
    def swap_fighter(cls,n_out,f_in):
        f_out = cls.player.fighters.pop(n_out)
        cls.player.fighters.insert(n_out,f_in())
        print(f_out.name,end=" swaps with ")
        print(cls.player.fighters[n_out].name)