class Menu:
    @classmethod
    def str_range(self,max):
        return [str(i+1) for i in range(max)]

    @classmethod
    def choose_option(self,options:list,results:list):
        user_input = ''

        while user_input not in options:
            user_input = input(">>> ")
            if user_input not in options:
                print("Invalid option please enter a number listed")

        for i in range(len(options)):
            if user_input == options[i]:
                results[i]()