from lib.fighter import Fighter
from lib.menu import Menu


class Stage:

    all = []
    player = None

    def __init__(self,stage_num,enemies,enemies_to_add):
        self.stage_num = stage_num
        self.enemies = enemies 
        self.enemies_to_add = enemies_to_add
        Stage.all.append(self)
    
    def run(self):
        from lib.intermission import Intermission
        restart = True
        while restart == True:
            print(f"You've Started Level {self.stage_num}")
            if self.battle_loop():
                Fighter.add_available(self.enemies_to_add)
                print('You Won!!!')
                Intermission.between_levels(self.stage_num)
                restart = False
            else: restart = Intermission.restart_level(self.stage_num)

    def battle_loop(self):
        self.enemies.reset()
        Stage.player.reset()
        is_player_turn = True
        while len(Stage.player.alive_fighters) > 0 and len(self.enemies.alive_fighters) > 0:
            if is_player_turn: self.player_turn()
            else: self.enemy_turn()
            is_player_turn = not is_player_turn
        return True if(len(self.enemies.alive_fighters)) == 0 else False

    def enemy_turn(self):
        self.enemies.do_random_action(Stage.player.current_fighter)
        self.trigger_conditions(self.enemies)

    def player_turn(self):
        print("Enemy Team")
        for fighter in self.enemies.alive_fighters:
            print(fighter)
        print("Your Party")
        for fighter in Stage.player.alive_fighters:
            print(fighter)
        # Player acts
        print('Your Turn')

        Menu.choose_option(
            ["1. Attack","2. Magic","3. Switch"],
            Menu.add_nums([["attack"],["magic"],["switch"]]),
            [
            self.choose_attack,
            self.choose_magic,
            self.choose_switch
            ])
        
        # End of turn, trigger all conditions
        self.trigger_conditions(Stage.player)
        

    def trigger_conditions(self,party):
        for fighter in party.fighters:
            if fighter.condition != None:
                fighter.condition['condition'].onTrigger(fighter,fighter.condition['amount'])
    
    def choose_attack(self):
        return Menu.choose_option([
            f"1. {Stage.player.current_fighter.attacks[0]}",
            f"2. {Stage.player.current_fighter.attacks[1]}",
            "3. Back"],
            Menu.add_nums([
                [Stage.player.current_fighter.attacks[0].name],
                [Stage.player.current_fighter.attacks[1].name],
                "back"]),
            [
            lambda: Stage.player.current_fighter_attack(0,self.enemies.current_fighter),
            lambda: Stage.player.current_fighter_attack(1,self.enemies.current_fighter)
            ],True)
    
    def choose_magic(self):
        return Menu.choose_option([
            f"1. {Stage.player.current_fighter.magics[0]}",
            f"2. {Stage.player.current_fighter.magics[1]}",
            "3. Back"],
            Menu.add_nums([
                [Stage.player.current_fighter.magics[0].name],
                [Stage.player.current_fighter.magics[1].name],
                "back"]),
            [
            lambda: Stage.player.current_fighter_magic(0,self.enemies.current_fighter),
            lambda: Stage.player.current_fighter_magic(1,self.enemies.current_fighter)
            ],True)

    @classmethod
    def choose_switch(cls,if_back = True):
        def create_swap(i):
            return lambda: cls.player.swap_current_fighter(i)

        swap_li = [create_swap(i) for i in range(len(cls.player.alive_fighters))]
        options_li = [[fighter.name] for fighter in cls.player.alive_fighters]
        text_li = [f"{i+1}. {fighter}" for i,fighter in enumerate(cls.player.alive_fighters)]

        if if_back: 
            text_li.append(f"{len(cls.player.alive_fighters)+1}: Back")
            options_li.append("back")

        return Menu.choose_option(text_li, Menu.add_nums(options_li), swap_li,if_back)
        
