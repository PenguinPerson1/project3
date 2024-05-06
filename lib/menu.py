class Menu:
    BACK = "BACK"
    @classmethod
    def str_range(cls,max):
        return [str(i+1) for i in range(max)]

    @classmethod
    def choose_option(cls,display:list,options:list,results:list,include_back = False):
        repeat = True
        i = 0
        while repeat:
            repeat = False

            for text in display:
                print(text)

            user_input = cls.return_option(options)
            if include_back and user_input == options.pop():
                return cls.BACK
            
            for i in range(len(options)):
                if user_input == options[i]:
                    res = results[i]()
                    if res == cls.BACK:
                        repeat = True


    @classmethod
    def return_option(cls,options:list):
        user_input = ''
        # options is a list of any string you will accept
        while user_input not in options:
            user_input = input(">>> ")
            if user_input not in options:
                print("Invalid option please enter a number listed")

        return user_input