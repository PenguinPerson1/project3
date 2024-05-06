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
            "3. Delete Save","4. Quit"],Menu.add_nums([["new","new game"],["resume","resume game"],["delete","delete save"],["quit"]]),[
            lambda: Setup.prep_stage1().run(),
            self.resume_game,
            self.choose_delete,
            Save.exit_program
        ])

    def resume_game(self):
        save = Save.get_save("Resume")
        if save == Menu.BACK:
            return Menu.BACK
        else:
            Save.set_id(save)

            stage = None
            for setup in Setup.ALL[0:save[1]+1]:
                stage = setup()
                
            self.player = Player([Fighter.all[fighter]() for fighter in save[2:5]])
            
            Intermission.between_levels(stage.stage_num)

    def choose_delete(self):
        value = Save.get_save("delete")
        if value != Menu.BACK:
            Save.delete_save(value)
        return Menu.BACK

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self,value):
        self._player = value
        Intermission.player = value
        Stage.player = value
