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

    def run(self):
        self.main_menu()
    
    def main_menu(self):
        Menu.choose_option(
            ["1. New Game","2. Resume Game",
            "3. Delete a Save","4. Quit"],Menu.str_range(4),[
            lambda: Setup.prep_stage1().run(),
            self.resume_game,
            self.choose_delete,
            Save.exit_program
        ])

    def resume_game(self):
        saves = Save.read_all()
        print("Choose a Save to Resume:")
        for i, save in enumerate(saves, start= 1):
            print(f"{i}. After Stage {save[1]} with party {', '.join(save[2:5])}")
        print(f"{len(saves)+1}. Back")
        pivot = Menu.return_option(Menu.str_range(len(saves)+1))

        if pivot == str(len(saves)+1):
            return Menu.BACK

        stage = None
        for setup in Setup.ALL[0:saves[int(pivot)-1][1]+1]:
            stage = setup()
            
        self.player = Player([Fighter.all[fighter]() for fighter in saves[int(pivot)-1][2:5]])
        
        Intermission.between_levels(stage.stage_num)

    def choose_delete(self):
        saves = Save.read_all()
        print("Choose a Save to Delete:")

        for i, save in enumerate(saves, start= 1):
            print(f"{i}. After Stage {save[1]} with party {', '.join(save[2:5])}")
        print(f"{len(saves)+1}. Back")
        pivot = Menu.return_option(Menu.str_range(len(saves)+1))

        if pivot == str(len(saves)+1):
            return Menu.BACK

        Save.delete_save(saves[int(pivot)-1])

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self,value):
        self._player = value
        Intermission.player = value
        Stage.player = value
