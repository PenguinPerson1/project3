from lib.fighter import Fighter
import random
class Party:
    def __init__(self,fighters=[]):
        self.fighters = fighters.copy()
        self.current_fighter = self.fighters[0]
        self.alive_fighters = self.fighters.copy()
        for fighter in self.alive_fighters:
            fighter.on_death = lambda f: self.kill_fighter(f)
    
    def kill_fighter(self,fighter):
        self.alive_fighters.remove(fighter)
        fighter.on_death = lambda _: print("dead fighter has triggered on_death")
        print("they have been removed from battle")
        if len(self.alive_fighters) == 0:
            return True
        
    def reset(self):
        self.alive_fighters = self.fighters.copy()
        self.current_fighter = self.fighters[0]
        for fighter in self.fighters:
            fighter.hp = fighter.hp_max
            fighter.mp = fighter.mp_max
            fighter.condition = None
            fighter.on_death = lambda f: self.kill_fighter(f)

class Player(Party):
    def add_fighter(self,fighter):
        if len(self.fighters) > 2:
            raise OverflowError()
        if type(fighter) != Fighter:
            raise TypeError()
        self.fighters.append(fighter)
        if len(self.fighters) == 1:
            self.current_fighter = self.fighters[0]

    def delete_fighter(self,f_index:int):
        self.fighters.pop(f_index)
    
    def swap_current_fighter(self,index:int):
        self.current_fighter = self.alive_fighters[index]
        print("changed fighter")
    
    def current_fighter_attack(self,atk_num:int,enemy):
        self.current_fighter.attacks[atk_num].use(enemy)

    def current_fighter_magic(self,atk_num:int,enemy):
        self.current_fighter.magics[atk_num].use(enemy,self.current_fighter)

    def kill_fighter(self, fighter):
        if super().kill_fighter(fighter):
            return True
        from lib.turns import Turn
        Turn.choose_switch(self)

class Enemy(Party):
    def do_random_action(self,enemy):
        viable_moves = [self.current_fighter.attacks[0],self.current_fighter.attacks[1]]
        for magic in self.current_fighter.magics:
            if self.current_fighter.mp >= magic.mp_use:
                viable_moves.append(magic)
        random.choice(viable_moves).use(enemy,self.current_fighter)
    
    def kill_fighter(self,fighter):
        if super().kill_fighter(fighter):
            return True
        if len(self.alive_fighters) == 0:
            print("No enemies left")
            return
        self.current_fighter = random.choice(self.alive_fighters)