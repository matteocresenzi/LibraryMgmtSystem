from ui.gui_utils import main_window_start, app, menu_navigation, page_function, table_populate, selected_items
from db.db_utils import run_db_commands
import sys

def main():
    # Runs initial database creation in memory
    run_db_commands()
    # Starts application window with add book page
    main_window_start()

    # Hosts menu navigation
    menu_navigation()
    # Functionality for all pages
    page_function()

    # Populates table from sql query
    table_populate()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
