class Action:
    def __init__(self,name,type,strength:int):
        self.name = name
        self.type = type
        self.strength = strength
    def __repr__(self):
        return f"{self.name}: deals {self.strength} damage of type {self.type} to the target"
    def use(self,enemy,_=None):
        if self.strength > 0:
            enemy.take_damage(self.type,self.strength)

class Magic(Action):
    all = {}
    def __init__(self,name,type,strength:int,mp_use,extra = lambda e,c : None,desc = ""):
        self.mp_use = mp_use
        self.extra = extra
        self.desc = desc
        super().__init__(name,type,strength)
        Magic.all[self.name] = self

    def __repr__(self):
        return super().__repr__() + f"{self.desc}. Uses {self.mp_use} mp"

    def use(self,enemy,caster):
        if(caster.mp >= self.mp_use):
            caster.mp -= self.mp_use
            super().use(enemy)
            self.extra(caster,enemy)
        else: print("Not enough mp")

class Attack(Action):
    all = {}
    def __init__(self,name,type,strength:int):
        super().__init__(name,type,strength)
        Attack.all[self.name] = self