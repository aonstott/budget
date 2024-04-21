from budget_manager import Database
from datetime import date


def main():
    database = Database()
    database.configure_db()
    database.clear_db()
    database.add_trans_to_db(20, date.today(), "Travel")
    print(database.get_all_trans())
    print('hiya')


main()