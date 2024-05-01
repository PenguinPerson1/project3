from lib.menu import Menu
class Turn:
    @classmethod
    def enemy_turn(cls,enemies,player_fighter):
        enemies.do_random_action(player_fighter)

    @classmethod
    def player_turn(cls,player,enemies):
        enemy = enemies.current_fighter
        print("Enemy Team")
        for fighter in enemies.alive_fighters:
            print(fighter)
        print("Your Party")
        for fighter in player.alive_fighters:
            print(fighter)
        # Player acts
        print('Your Turn')
        print('1. Attack')
        print('2. Magic')
        print('3. Switch')

        Menu.choose_option(Menu.str_range(3),[
            lambda: cls.choose_attack(player,enemy),
            lambda: cls.choose_magic(player,enemy),
            lambda: cls.choose_switch(player)
            ])
        
        # End of turn, trigger all conditions
        for fighter in player.fighters:
            if fighter.condition != None:
                fighter.condition['condition'].onTrigger(fighter,fighter.condition['amount'])
    
    @classmethod
    def choose_attack(cls,player,enemy):
        print("1.",end=' ')
        print(player.current_fighter.attacks[0])
        print("2.",end=' ')
        print(player.current_fighter.attacks[1])
        Menu.choose_option(Menu.str_range(2),[
            lambda: player.current_fighter_attack(0,enemy),
            lambda: player.current_fighter_attack(1,enemy)
            ])
    
    @classmethod
    def choose_magic(cls,player,enemy):
        print("1.",end=' ')
        print(player.current_fighter.magics[0])
        print("2.",end=' ')
        print(player.current_fighter.magics[1])
        Menu.choose_option(Menu.str_range(2),[
            lambda: player.current_fighter_magic(0,enemy),
            lambda: player.current_fighter_magic(1,enemy)
            ])

    @classmethod    
    def choose_switch(cls,player):
        num_players = len(player.alive_fighters)
        li = []
        def create_swap(i):
            return lambda: player.swap_current_fighter(i)
        for i in range(num_players):
            print(i+1,end=": ")
            print(player.alive_fighters[i])
            li.append(create_swap(i))
        
        Menu.choose_option(Menu.str_range(num_players), li)