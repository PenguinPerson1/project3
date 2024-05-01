class Type:
    all={}
    def __init__(self,name:str,is_weak_to:list,is_strong_against:list):
        self.name = name
        self.is_weak_to = is_weak_to
        self.is_strong_against = is_strong_against
        Type.all[self.name] = self
    
    def __repr__(self):
        return self.name