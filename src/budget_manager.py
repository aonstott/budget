import sqlite3


class Database:

    conn = sqlite3.connect("budget.db")
    cursor = conn.cursor()
    def configure_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, amount DECIMAL(10, 2), date DATE, category VARCHAR(256))''')

    def add_trans_to_db(self, amount, date, category):
        self.cursor.execute("INSERT INTO transactions (amount, date, category) VALUES (?,?,?)", (amount, date, category))
        self.conn.commit()

    def remove_trans_from_db(self, id_delete):
        self.cursor.execute("REMOVE FROM transactions WHERE id = ?", id_delete)
        self.conn.commit()

    def get_all_trans(self):
        self.cursor.execute("SELECT amount, date, category FROM transactions")
        transactions = self.cursor.fetchall()
        return transactions

    def clear_db(self):
        self.cursor.execute("DELETE FROM transactions")

