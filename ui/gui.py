from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget
from ui.ui_compiled.home import Ui_Form as HomeWidget
from ui.ui_compiled.add_book import Ui_Form as AddWidget
from ui.ui_compiled.edit_book import Ui_Form as EditWidget
from ui.ui_compiled.menu_bar import Ui_Form as MenuWidget
from ui.ui_compiled.visualize import Ui_Form as VisualizeWidget
from db.db_utils import insert_entry

class CustomWidget(QWidget, HomeWidget, AddWidget, EditWidget, MenuWidget, VisualizeWidget):
    def __init__(self, ui_class):
        super().__init__()

        self.ui = ui_class()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Resizes main window for application
        self.resize(800, 600)
        self.setWindowTitle("Personal Library")

        # Central widget for main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout for main window
        self.main_layout = QVBoxLayout(central_widget)

        # Initialize menu widget
        self.menu_widget = CustomWidget(MenuWidget)
        self.menu_widget.setMinimumSize(800, 40)

        # Initialize stacked widget for content
        # Stacked widget uses array [0, 1, 2, 3]
        # Index 0 is Home
        # Index 1 is Add Book
        # Index 2 is Edit Book
        # Index 3 is Visualize
        self.stacked_widget = QStackedWidget()
        self.add_widget_to_stack(HomeWidget)
        self.add_widget_to_stack(AddWidget)
        self.add_widget_to_stack(EditWidget)
        self.add_widget_to_stack(VisualizeWidget)
        self.stacked_widget.setMinimumSize(800, 560)

        # Add menu and stacked widget to the main layout
        self.main_layout.addWidget(self.menu_widget)
        self.main_layout.addWidget(self.stacked_widget)

    def add_widget_to_stack(self, ui_class):
        widget = CustomWidget(ui_class)
        self.stacked_widget.addWidget(widget)
