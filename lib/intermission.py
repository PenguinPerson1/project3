from lib.menu import Menu
from lib.fighter import Fighter
from lib.saves import Save
import lib.config as config


class Intermission:
    RETRY_OPTIONS = ["r","retry","retry level"]
    EDIT_OPTIONS = ["e","edit","edit team"]
    SAVE_OPTIONS = ["s","q","save","quit","save and quit","save & quit"]
    CONTINUE_OPTIONS = ["c","continue","next","continue to next round"]
    DESCRIPTION_OPTIONS = ["g","d","get","descriptions","get descriptions"]

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
                Save.save_exit(cls.num_level,config.player)
                return False

    @classmethod
    def between_levels(cls,num_level):
        cls.num_level = num_level
        from lib.setup import Setup
        next_level = Setup.ALL[num_level+1]()

        Menu.choose_option([
            "Do you want to edit your team?",
            "1. Edit Team",
            "2. Get Descriptions",
            "3. Continue to Next Round",
            "4. Save & Quit"
        ],Menu.add_nums([
            cls.EDIT_OPTIONS,
            cls.DESCRIPTION_OPTIONS,
            cls.CONTINUE_OPTIONS,
            cls.SAVE_OPTIONS
        ]),[
            cls.edit_team,
            cls.get_descriptions,
            next_level.run,
            lambda: Save.save_exit(cls.num_level,config.player)
        ])
        
    @classmethod
    def edit_team(cls):
        repeat = True
        while repeat:
            print("Which Fighter would you like to replace?")
            for i, fighter in enumerate(config.player.fighters,start=1):
                print(i,end=": ")
                print(fighter.name)

            swap_out = Menu.return_option(Menu.add_nums([[fighter.name,fighter.name[0]] for fighter in config.player.fighters]))

            print("Which fighter would you like to replace them with?")
            for i, fighter in enumerate(Fighter.available.keys(),start=1):
                print(i,end=". ")
                print(fighter)

            swap_in = Menu.return_option(Menu.add_nums([[fighter,fighter[0]] for fighter in Fighter.available]))

            cls.swap_fighter(swap_out,list(Fighter.available.values())[swap_in])

            print('Would you like to replace a different fighter?')
            print("1. Replace Another")
            print("2. Back")

            pivot = Menu.return_option(Menu.add_nums([
                ["r","replace","another","replace another"],
                ["b","back"],
            ]))
            if pivot == 0:
                repeat = True
            elif pivot == 1:
                return Menu.BACK

    @classmethod
    def get_descriptions(cls):
        for fighter in Fighter.available.values():

            print("\n -------------------- \n")

            curr = fighter()
            print(f"Name: {curr.name}")
            print(f"Type: {curr.type}")
            print(f"Attack 1: {curr.attacks[0]}")
            print(f"Attack 2: {curr.attacks[1]}")
            print(f"Magic 1: {curr.magics[0]}")
            print(f"Magic 2: {curr.magics[1]}")

        print("\nEnter anything to go back:")
        user_input = input(">>> ")
        return Menu.BACK

    @classmethod
    def swap_fighter(cls,n_out,f_in):
        f_out = config.player.fighters.pop(n_out)
        config.player.fighters.insert(n_out,f_in())
        print(f_out.name,end=" swaps with ")
        print(config.player.fighters[n_out].name, end="\n\n")