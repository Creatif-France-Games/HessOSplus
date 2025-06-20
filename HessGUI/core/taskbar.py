from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QMenu, QSpacerItem, QSizePolicy
from PySide6.QtCore import QTimer, QTime, Qt
from PySide6.QtGui import QAction, QIcon

class Taskbar(QWidget):
    def __init__(self, desktop):
        super().__init__()
        self.desktop = desktop
        self.setFixedHeight(40)
        self.setStyleSheet("""
            background-color: #202020;
            color: white;
        """)

        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(8, 0, 8, 0)
        self.main_layout.setSpacing(12)
        self.setLayout(self.main_layout)

        # Bouton Démarrer
        self.start_button = QPushButton("☰")
        self.start_button.setFixedSize(36, 32)
        self.start_button.clicked.connect(self.show_start_menu)
        self.start_button.setStyleSheet("background-color: #333; color: white; border: none;")
        self.main_layout.addWidget(self.start_button)

        # Conteneur icônes d'apps
        self.app_buttons_layout = QHBoxLayout()
        self.app_buttons_container = QWidget()
        self.app_buttons_container.setLayout(self.app_buttons_layout)
        self.app_buttons_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.app_buttons_container)

        # Heure
        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.clock.setStyleSheet("font-weight: bold;")
        self.main_layout.addWidget(self.clock)

        # Timer horloge
        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)
        self.update_clock()

        self.open_app_buttons = {}

    def update_clock(self):
        self.clock.setText(QTime.currentTime().toString("HH:mm:ss"))

    def show_start_menu(self):
        menu = QMenu()
        for app in self.desktop.app_list:
            action = QAction(app['name'], self)
            action.triggered.connect(lambda checked, a=app: self.desktop.launch_app(a['class']))
            menu.addAction(action)
        menu.exec_(self.start_button.mapToGlobal(self.start_button.rect().bottomLeft()))

    def add_app_button(self, app):
        if app['name'] in self.open_app_buttons:
            return

        btn = QPushButton()
        btn.setIcon(QIcon(app['icon']))
        btn.setToolTip(app['name'])
        btn.setFixedSize(36, 32)
        btn.setStyleSheet("background-color: #444; border: none;")
        btn.clicked.connect(lambda: self.bring_app_to_front(app['name']))
        self.app_buttons_layout.addWidget(btn)
        self.open_app_buttons[app['name']] = btn

    def remove_app_button(self, app_name):
        if app_name in self.open_app_buttons:
            btn = self.open_app_buttons.pop(app_name)
            self.app_buttons_layout.removeWidget(btn)
            btn.deleteLater()

    def bring_app_to_front(self, app_name):
        for window in self.desktop.open_windows:
            if window.windowTitle() == app_name:
                window.raise_()
                window.activateWindow()
