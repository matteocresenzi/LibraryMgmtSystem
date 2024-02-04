from ui.gui_utils import main_window_start, app, menu_navigation, page_function
from db.db_utils import run_db_commands
import sys

def main():
    # Runs initial database creation in memory
    run_db_commands()
    # Starts application window with add book page
    main_window_start()
    menu_navigation()
    page_function()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
