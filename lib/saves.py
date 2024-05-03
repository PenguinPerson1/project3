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
            fighter1 TEXT,
            fighter2 TEXT,
            fighter3 TEXT
        );
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def save_program(cls,stage,party):
        pass