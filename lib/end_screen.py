from lib.menu import Menu
from lib.saves import Save

class End_screen:
    @classmethod
    def run(self):
        from lib.setup import Setup
        Setup.reset_game()
        print("Congratulations on Finishing the Game")
        print("1. Play Again")
        print("2. Main Menu")
        print("3. Quit")
        pivot  = Menu.return_option(Menu.add_nums([
            ["p,play,play again"],
            ["m","main","menu","main menu"],
            ["q","quit"]
        ]))
        if pivot == 0:
            Setup.prep_stage1().run()
        elif pivot == 1:
            return Menu.BACK
        elif pivot == 2:
            Save.exit_program()