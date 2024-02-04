from ui.gui_utils import init_add_book_window, app
from db.db_utils import run_db_commands
import sys

def main():
    # Runs initial database creation in memory
    run_db_commands()
    # Starts application window with add book page
    init_add_book_window()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
