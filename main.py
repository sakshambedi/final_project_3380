from database import DataBase
from gui import Gui


def main():
    db = DataBase(False)
    run_console(db)
    
    
def run_console(db):
    Gui()
    
if __name__ == '__main__':
    main()
