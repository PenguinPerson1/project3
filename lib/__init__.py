import sqlite3

CONN = sqlite3.connect('db/main.db')
CURSOR = CONN.cursor()