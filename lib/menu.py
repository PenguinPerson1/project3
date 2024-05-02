class Menu:
    @classmethod
    def str_range(cls,max):
        return [str(i+1) for i in range(max)]

    @classmethod
    def choose_option(cls,options:list,results:list):
        
        user_input = cls.return_option(options)

        for i in range(len(options)):
            if user_input == options[i]:
                results[i]()

    @classmethod
    def return_option(cls,options:list):
        user_input = ''
        # options is a list of any string you will accept
        while user_input not in options:
            user_input = input(">>> ")
            if user_input not in options:
                print("Invalid option please enter a number listed")

        return user_input