from lib.type import Type
from lib.fighter import Fighter
from lib.actions import Attack,Magic
from lib.party import Enemy, Player
from lib.conditions import Condition
from lib.stages import Stage
import lib.config as config

class Setup:
    @classmethod
    def reset_game(cls):
        Type.all.clear()
        Condition.all.clear()
        Attack.all.clear()
        Magic.all.clear()
        Fighter.all.clear()
        Fighter.available.clear()
        config.player = Setup.prep_stage0()
    @classmethod
    def prep_stage0(cls):
        Type("normal",[],[])
        Type("fire",["water"],["grass"])

        Attack('slash',Type.all["normal"],35)

        Magic('smite',Type.all["fire"],70,20)
        Magic('heal',Type.all["normal"],0,20,
              lambda c,e : c.current_fighter.heal(30),
              " but heals caster by 30 hp")

        Fighter.add_func("knight",Type.all["fire"],200,40,
                         [Attack.all['slash'],Attack.all['slash']],
                         [Magic.all['smite'],Magic.all['heal']])
        
        # Knight is always available for the player to use
        Fighter.add_available(["knight"])

        return Player([Fighter.all['knight']() for _ in range(3)])

    @classmethod
    def prep_stage1(cls):
        Type("grass",["fire"],["water"])

        Condition('poison',lambda f,i : f.take_damage(Type.all["grass"],i),"poisoned")

        Attack('stab',Type.all["normal"],40)

        Magic('leech life',Type.all["grass"],30,30,
              lambda c,_: c.current_fighter.heal(20),
              " and heals caster by 20 hp")
        Magic('poisoned blade',Type.all["grass"],20,20,
              lambda _,e: e.current_fighter.set_condition(Condition.all['poison'],10),
              " and poisons target")

        goblin = Fighter.add_func("goblin",Type.all["grass"],120,50,
                                  [Attack.all['stab'],Attack.all['stab']],
                                  [Magic.all['leech life'],Magic.all['poisoned blade']])

        return Stage(1,Enemy([goblin(),goblin()]),["goblin"])
    
    @classmethod
    def prep_stage2(cls):
        # Whenever players are stage 2 or later, they have access to goblin
        Fighter.add_available(["goblin"])

        Type("water",["grass"],["fire"])

        Condition('regen',lambda f,i : f.heal(i),"regenerating")

        Attack('sea spray',Type.all['water'],30)

        Magic('water of life',Type.all['water'],0,50,
              lambda c,_: c.current_fighter.set_condition(Condition.all['regen'],5),
              " and starts healing wounds")
        
        mermaid = Fighter.add_func("mermaid",Type.all['water'],250,50,
                                 [Attack.all['stab'],Attack.all['sea spray']],
                                 [Magic.all['water of life'],Magic.all['water of life']])
        
        return Stage(2,Enemy([mermaid(),mermaid(),mermaid()]),["mermaid"])
    
    @classmethod
    def prep_stage3(cls):
        Fighter.add_available(["mermaid"])

        Type("rock",["grass","water"],["fire"])

        Attack('boulder',Type.all['rock'],30)
        Attack('sea spray',Type.all['water'],25)

        Magic('quake',Type.all['rock'],70,20)

        troll = Fighter.add_func("troll",Type.all['rock'],320,50,
                                 [Attack.all['boulder'],Attack.all['sea spray']],
                                 [Magic.all['quake'],Magic.all['leech life']])

        return Stage(3,Enemy([troll(),Fighter.all['mermaid'](),troll()]),["troll"])
        pass

    @classmethod
    def prep_stage4(cls):
        Fighter.add_available(["troll"])

        Attack('ember',Type.all['fire'],30)

        def breathe_fire(_,e):
            for enemy in e.alive_fighters:
                enemy.take_damage(Type.all['fire'],20)

        Magic('fire breath',Type.all['fire'],50,20,breathe_fire)

        dragon = Fighter.add_func("dragon",Type.all['fire'],600,100,
                                 [Attack.all['slash'],Attack.all['ember']],
                                 [Magic.all['fire breath'],Magic.all['fire breath']])
        
        return Stage(4,Enemy([dragon()]),[])    

    ALL = [
        lambda: Setup.prep_stage0(),
        lambda: Setup.prep_stage1(),
        lambda: Setup.prep_stage2(),
        lambda: Setup.prep_stage3(),
        lambda: Setup.prep_stage4()
    ]