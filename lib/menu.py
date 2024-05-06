class Menu:
    BACK = "BACK"
    @classmethod
    def add_nums(cls,li:list):
        return [(str(i+1), *item) for i, item in enumerate(li)]

    @classmethod
    def str_range(cls,max):
        return [[str(i+1)] for i in range(max)]

    @classmethod
    def choose_option(cls,display:list,options:list,results:list,include_back = False):
        repeat = True
        i = 0
        while repeat:
            repeat = False

            for text in display:
                print(text)

            option_num = cls.return_option(options)
            if include_back and option_num == len(options)-1:
                return cls.BACK

            res = results[option_num]()
            if res == cls.BACK:
                repeat = True

                
            # for i in range(len(options)):
            #     if user_input.lower() in options[i]:
            #         res = results[i]()
            #         if res == cls.BACK:
            #             repeat = True
            #         break


    @classmethod
    def return_option(cls,options:list):
        user_input = ''
        # options is a list of any string you will accept
        print(options)
        user_input = input(">>> ")
        while not any(user_input.lower() in sl for sl in options):
            print("Invalid option please enter a number listed")
            user_input = input(">>> ")

        for i in range(len(options)):
            if user_input.lower() in options[i]:
                return i