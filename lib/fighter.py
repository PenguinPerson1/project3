from lib.actions import Attack,Magic
from lib.type import Type
import math


class Fighter:
    all={}
    available = {}
    def __init__(self,name:str,type,hp_max:int,mp_max:int,attacks,magics):
        self.name = name
        self.type = type
        self.hp_max = hp_max
        self.hp = hp_max
        self.mp_max = mp_max
        self.mp = mp_max
        self.attacks = attacks
        self.magics = magics
        self.condition = None
        self.on_death = lambda: None

    def __repr__(self):
        base = f"A {self.name} with {self.hp} hp and {self.mp} mp left."
        condition = f" They are {self.condition['condition'].description}" if self.condition != None else ""
        return base + condition

    def take_damage(self,damage_type,damage):
        if damage_type.name in self.type.is_weak_to:
            damage = math.floor(damage*1.5)
        self.hp = round(self.hp - damage)
        if self.hp <= 0:
            self.die()
        else: print(f"{self.name} took {damage} damage. They are now at {self.hp} hp")

    def set_condition(self,condition,amount):
        if(self.condition == None or self.condition['condition'] != condition or self.condition['amount'] < amount):
            self.condition = {"condition":condition,"amount":amount}
    
    def heal(self,amount):
        self.hp += amount
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        print(f"{self.name} healed {amount} damage. They are now at {self.hp} hp")
    
    def die(self):
        print(f"{self.name} has died.")
        self.condition = None
        self.hp = 0
        self.on_death(self)
    
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self,val):
        if type(val) == Type:
            self._type = val
    
    @property
    def attacks(self):
        return self._attacks
    @attacks.setter
    def attacks(self,val):
        if len(val) == 2:
            if type(val[0]) == Attack and type(val[1]) == Attack:
                self._attacks = val

    @property
    def magics(self):
        return self._magics
    @magics.setter
    def magics(self,val):
        if len(val) == 2:
            if type(val[0]) == Magic and type(val[1]) == Magic:
                self._magics = val
    
    @classmethod
    def add_func(cls,name:str,type,hp_max:int,mp_max:int,attacks,magics):
        cls.all[name] = lambda:cls(name,type,hp_max,mp_max,attacks,magics)
        return cls.all[name]
    
    @classmethod
    def add_available(cls,names:list):
        for name in names:
            cls.available[name] = cls.all[name]