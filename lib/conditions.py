class Condition:
    all = {}
    def __init__(self,name,onTrigger,description):
        self.description = description
        self.name = name
        self.onTrigger = onTrigger
        Condition.all[name] = self