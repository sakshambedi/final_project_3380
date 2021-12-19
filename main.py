from database import DataBase

def main():
    db = DataBase(False)
    run_console(db)
    
    
def run_console(db):
    print("Welcome to the database console !")
    enter = str(input("db >"))
    inputs = enter.strip().split()
    if inputs[0] == "p":
        print("Getting names of the nba players .. ")
        db.all_players()
    elif inputs[0] == "q":
        print("Goodbye")
    
    
if __name__ == '__main__':
    main()
