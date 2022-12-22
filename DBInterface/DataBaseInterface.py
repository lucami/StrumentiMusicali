import time

import mysql.connector


class DBInterface:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost", user="root", password="Password1!", database="Strumenti")
        self.cursor = self.db.cursor()

    def get_new_lines(self):
        self.cursor.execute("SELECT nome, prezzo FROM Strumenti WHERE visualizzato = '0'")
        result = self.cursor.fetchall()
        for x in result:
            print(x)

        self.change_new_to_old()


    def change_new_to_old(self):
        sql = "UPDATE Strumenti SET visualizzato = '1' WHERE visualizzato = '0'"
        self.cursor.execute(sql)
        self.db.commit()


    def get_today_lines(self):
        self.cursor.execute(f"SELECT nome, prezzo FROM Strumenti WHERE data_aggiunta = '{time.strftime('%Y-%m-%d')}'")
        result = self.cursor.fetchall()
        for x in result:
            print(x)


    def insert(self, nome, link, prezzo, date):
        sql = "INSERT INTO Strumenti (link, nome, prezzo, data_aggiunta, visualizzato) VALUES (%s, %s, %s, %s, %s)"
        val = (link, nome, prezzo, date, 0)
        self.cursor.execute(sql, val)
        self.db.commit()


if __name__ == '__main__':
    interface = DBInterface()
    #interface.get_today_lines()
    interface.get_new_lines()
