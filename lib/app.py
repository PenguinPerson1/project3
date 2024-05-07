from lib.setup import Setup
from lib.menu import Menu
from lib.stages import Stage
from lib.intermission import Intermission
from lib.saves import Save
from lib.fighter import Fighter
from lib.party import Player
import lib.config as config

class App:
    def __init__(self):
        Save.create_table()
        config.player = Setup.prep_stage0()

    def run(self):
        self.main_menu()
    
    def main_menu(self):
        Menu.choose_option(
            ["1. New Game",
            "2. Resume Game",
            "3. Delete Save",
            "4. Quit"],
            Menu.add_nums([
                ["n","new","new game"],
                ["r","resume","resume game"],
                ["d","delete","delete save"],
                ["q","quit"]]),[
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
                
            config.player = Player([Fighter.all[fighter]() for fighter in save[2:5]])
            
            return Intermission.between_levels(stage.stage_num)

    def choose_delete(self):
        value = Save.get_save("delete")
        if value != Menu.BACK:
            Save.delete_save(value)
        return Menu.BACK