from . import CONN, CURSOR
from lib.menu import Menu

class Save:
    @classmethod
    def set_id(cls,save):
        cls.id = save[0]
    @classmethod
    def exit_program(cls):
        print("goodbye!")
        exit()

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS saves (
            id INTEGER PRIMARY KEY,
            stage INTEGER,
            fighter0 TEXT,
            fighter1 TEXT,
            fighter2 TEXT
        );
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def save_program(cls,stage,party):
        sql = "INSERT INTO saves (stage,fighter0,fighter1,fighter2) VALUES ( ? , ? , ? , ? );"

        CURSOR.execute(sql, [stage] + [fighter.name for fighter in party.fighters] + [None for _ in range(3-len(party.fighters))])
        CONN.commit()

    @classmethod
    def update_save(cls,stage,party):
        sql = """UPDATE saves SET stage = ?, fighter0 = ?, fighter1 = ?, fighter2 = ? WHERE id = ?"""
        CURSOR.execute(sql,[stage] + [fighter.name for fighter in party.fighters] + [None for _ in range(3-len(party.fighters))] + [cls.id])
        CONN.commit()

    @classmethod
    def save_exit(cls,stage,party):
        if hasattr(cls,"id"): 
            Menu.choose_option(["Overwrite Previous Save?","1. Yes","2. No"],
            Menu.str_range(2),[
                lambda: cls.update_save(stage, party),
                lambda: cls.save_program(stage, party)])
        else: cls.save_program(stage, party)
        cls.exit_program()

    @classmethod
    def read_all(cls):
        sql = """
        SELECT * FROM saves;
        """

        saves = CURSOR.execute(sql).fetchall()
        return saves
    
    @classmethod
    def delete_save(cls,save):
        sql = """
        DELETE FROM saves WHERE id = ?;
        """

        CURSOR.execute(sql, [save[0]])
        CONN.commit()

    @classmethod
    def get_save(cls,method:str):
        saves = cls.read_all()
        if saves == []:
            print("No Saves currently exist")
            print("Returning you to Main Menu")

        else:
            print(f"Choose a Save to {method}:")
            for i, save in enumerate(saves, start= 1):
                print(f"{i}. After Stage {save[1]} with party {', '.join(save[2:5])}")
            print(f"{len(saves)+1}. Back")
            pivot = Menu.return_option(Menu.str_range(len(saves)+1))

            if pivot != str(len(saves)+1):
                return saves[int(pivot)-1]
        return Menu.BACK
