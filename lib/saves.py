from . import CONN, CURSOR

class Save:
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
    def save_exit(cls,stage,party):
        cls.save_program(stage, party)
        cls.exit_program()