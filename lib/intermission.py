from lib.menu import Menu
from lib.fighter import Fighter
from lib.saves import Save


class Intermission:

    @classmethod
    def restart_level(cls,num_level):
        print('You Died... Retry?')
        cls.num_level = num_level-1
        if num_level == 1:
            print('1. Retry Level')
            print('2. Quit')

            if Menu.return_option(Menu.str_range(2)) == "1":
                return True
            else:
                Save.exit_program()
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
                cls.edit_team()
                return True
            else:
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

        pivot = Menu.return_option(Menu.str_range(3),)
        if pivot == "3":
            Save.save_exit(cls.num_level,cls.player)
        else:
            if pivot == "1": cls.edit_team()
            next_level.run()
        
    @classmethod
    def edit_team(cls):
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
            print("3. Save and Quit")

            pivot = Menu.return_option(Menu.str_range(3))
            if pivot == "1":
                repeat = True
            elif pivot == "2":
                repeat = False
            elif pivot == "3":
                Save.save_exit(cls.num_level,cls.player)

    @classmethod
    def swap_fighter(cls,n_out,f_in):
        f_out = cls.player.fighters.pop(n_out)
        cls.player.fighters.insert(n_out,f_in())
        print(f_out.name,end=" swaps with ")
        print(cls.player.fighters[n_out].name)