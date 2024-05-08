from lib.fighter import Fighter
from lib.menu import Menu
from lib.end_screen import End_screen
import lib.config as config

class Stage:    
    def __init__(self,stage_num,enemies,enemies_to_add):
        self.stage_num = stage_num
        self.enemies = enemies 
        self.enemies_to_add = enemies_to_add
    
    def run(self):
        from lib.intermission import Intermission
        from lib.setup import Setup
        restart = True
        while restart == True:
            print(f"\nYou've Started Level {self.stage_num} \n")
            if self.battle_loop():
                Fighter.add_available(self.enemies_to_add)
                print('You Won!!!')
                if self.stage_num == len(Setup.ALL)-1:
                    return End_screen.run()
                else:
                    return Intermission.between_levels(self.stage_num)
                restart = False
            else: restart = Intermission.restart_level(self.stage_num)

    def battle_loop(self):
        self.enemies.reset()
        config.player.reset()
        is_player_turn = True
        while len(config.player.alive_fighters) > 0 and len(self.enemies.alive_fighters) > 0:
            if is_player_turn: self.player_turn()
            else: self.enemy_turn()
            print("\n")
            is_player_turn = not is_player_turn
        return True if(len(self.enemies.alive_fighters)) == 0 else False

    def enemy_turn(self):
        self.enemies.do_random_action(config.player.current_fighter)
        self.trigger_conditions(self.enemies)

    def player_turn(self):
        print("-----------------------")
        print("Enemy Team")
        for fighter in self.enemies.alive_fighters:
            print(fighter)
        print("\nYour Party")
        for fighter in config.player.alive_fighters:
            print(fighter)
        # Player acts
        print('\nYour Turn')

        Menu.choose_option(
            ["1. Attack","2. Magic","3. Switch"],
            Menu.add_nums([["a","attack"],["m","magic"],["s","switch"]]),
            [
            lambda: self.choose_action("attack"),
            lambda: self.choose_action("magic"),
            self.choose_switch
            ])
        
        # End of turn, trigger all conditions
        self.trigger_conditions(config.player)
        

    def trigger_conditions(self,party):
        for fighter in party.fighters:
            if fighter.condition != None:
                print(f"\n{fighter.name} is {fighter.condition['condition'].description}:")
                fighter.condition['condition'].onTrigger(fighter,fighter.condition['amount'])
    
    def choose_action(self,sub_action):
        action_0 = getattr(config.player.current_fighter,f'{sub_action}s')[0]
        action_1 = getattr(config.player.current_fighter,f'{sub_action}s')[1]
        return Menu.choose_option([
            f"1. {action_0}",
            f"2. {action_1}",
            "3. Back"],
            Menu.add_nums([
                [action_0.name,action_0.name[0]],
                [action_1.name,action_1.name[0]],
                ["b","back"]]),
            [
            lambda: getattr(config.player,f'current_fighter_{sub_action}')(0,self.enemies.current_fighter),
            lambda: getattr(config.player,f'current_fighter_{sub_action}')(1,self.enemies.current_fighter)
            ],True)

    @classmethod
    def choose_switch(cls,if_back = True):
        def create_swap(i):
            return lambda: config.player.swap_current_fighter(i)

        swap_li = [create_swap(i) for i in range(len(config.player.alive_fighters))]
        options_li = [[fighter.name,fighter.name[0]] for fighter in config.player.alive_fighters]
        text_li = [f"{i+1}. {fighter}" for i,fighter in enumerate(config.player.alive_fighters)]

        if if_back: 
            text_li.append(f"{len(config.player.alive_fighters)+1}: Back")
            options_li.append(["b","back"])

        return Menu.choose_option(text_li, Menu.add_nums(options_li), swap_li,if_back)
        
