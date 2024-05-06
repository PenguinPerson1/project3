from lib.setup import Setup
from lib.menu import Menu
from lib.stages import Stage
from lib.intermission import Intermission
from lib.saves import Save
from lib.fighter import Fighter
from lib.party import Player

class App:
    def __init__(self):
        Save.create_table()
        self.player = Setup.prep_stage0()
        Intermission.player = self.player
        Stage.player = self.player

    def run(self):
        self.main_menu()
    
    def main_menu(self):
        print('Main Menu')
        print('1. New Game')
        print('2. Resume Game')
        print('3. Delete a Save')
        print('4. Quit')

        pivot = Menu.return_option(Menu.str_range(4))
        if pivot == "1":
            stage1 = Setup.prep_stage1()
            stage1.run()
        elif pivot == "2":
            self.resume_game()
        elif pivot == "3":
            self.choose_delete()
        elif pivot == "4":
            Save.exit_program()

    def resume_game(self):
        saves = Save.read_all()
        print("Choose a Save to Resume:")
        for i, save in enumerate(saves, start= 1):
            print(f"{i}) After Stage {save[1]} with party {', '.join(save[2:5])}")
        pivot = Menu.return_option(Menu.str_range(len(saves)))

        stage = None
        for setup in Setup.ALL[0:saves[int(pivot)-1][1]+1]:
            stage = setup()
            
        self.player = Player([Fighter.all[fighter]() for fighter in saves[int(pivot)-1][2:5]])
        Stage.player = self.player
        Intermission.player = self.player
        
        Intermission.between_levels(stage.stage_num)

    def choose_delete(self):
        saves = Save.read_all()
        print("Choose a Save to Delete:")

        for i, save in enumerate(saves, start= 1):
            print(f"{i}) After Stage {save[1]} with party {', '.join(save[2:5])}")
        pivot = Menu.return_option(Menu.str_range(len(saves)))

        Save.delete_save(saves[int(pivot)-1])

