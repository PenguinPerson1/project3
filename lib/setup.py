from lib.type import Type
from lib.fighter import Fighter
from lib.actions import Attack,Magic
from lib.party import Enemy
from lib.conditions import Condition

class Setup:
    def __init__(self):
        Type("normal",[],[])
        Type("fire",["water"],["grass"])

        Attack('slash',Type.all["normal"],30)

        Magic('smite',Type.all["fire"],70,10)
        Magic('heal',Type.all["normal"],0,10,
              lambda c,e : c.heal(30),
              " but heals caster by 30 hp")

        Fighter.add_func("knight",Type.all["fire"],200,20,
                         [Attack.all['slash'],Attack.all['slash']],
                         [Magic.all['smite'],Magic.all['heal']])
        
        # Knight is always available for the player to use
        Fighter.add_available("knight")

    def prep_stage1(self):
        Type("grass",["fire"],["water"])

        Condition('poison',lambda f,i : f.take_damage(Type.all["grass"],i),"poisoned")

        Attack('stab',Type.all["normal"],40)

        Magic('leech_life',Type.all["grass"],30,30,
              lambda c,_: c.heal(20),
              " and heals caster by 20 hp")
        Magic('poisoned_blade',Type.all["grass"],20,20,
              lambda _,e: e.set_condition(Condition.all['poison'],10),
              " and poisons target")

        goblin = Fighter.add_func("goblin",Type.all["grass"],120,50,
                                  [Attack.all['stab'],Attack.all['stab']],
                                  [Magic.all['leech_life'],Magic.all['poisoned_blade']])

        return Enemy([goblin()])
    
    def prep_stage2(self):
        # Whenever players are stage 2 or later, they have access to goblin
        Fighter.add_available("goblin")

        Type("water",["grass"],["fire"])

        Condition('regen',lambda f,i : f.heal(i),"regenerating")

        Attack('sea_spray',Type.all['water'],25)

        Magic('water_of_life',Type.all['water'],0,50,
              lambda c,_: c.set_condition(Condition.all['regen'],5),
              " and starts healing wounds")
        
        mermaid = Fighter.add_func("mermaid",Type.all['water'],250,50,
                                 [Attack.all['stab'],Attack.all['sea_spray']],
                                 [Magic.all['water_of_life'],Magic.all['water_of_life']])
        
        return Enemy([mermaid()])
