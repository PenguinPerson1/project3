from lib.turns import Turn
from lib.fighter import Fighter
from lib.setup import Setup
from lib.intermission import Intermission

class Stage:

    @classmethod
    def stage1(self,player):
        enemies = Setup.prep_stage1()
        restart = True
        while restart == True:
            print("You've Started Level 1")
            if Turn.battle_loop(player,enemies):
                Fighter.add_available(["goblin"])
                Intermission.between_levels(self.stage2,1)
                restart = False
            else: restart = Intermission.restart_level(True)

    @classmethod
    def stage2(self,player):
        enemies = Setup.prep_stage2()
        restart = True
        while restart == True:
            print("You've Started Level 2")
            if Turn.battle_loop(player,enemies):
                Fighter.add_available(["mermaid"])
                Intermission.between_levels(self.stage3,2)
                restart = False
            else: restart = Intermission.restart_level(False)

    @classmethod
    def stage3(self,player):
        print("stage 3")


    stages = [stage1,stage2,stage3]