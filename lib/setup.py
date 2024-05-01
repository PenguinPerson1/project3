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
    
