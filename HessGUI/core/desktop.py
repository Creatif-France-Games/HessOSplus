from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Qt

class IconWidget(QWidget):
    def __init__(self, app_class, icon_path, name, parent_desktop):
        super().__init__()
        self.app_class = app_class
        self.name = name
        self.parent_desktop = parent_desktop  # ← référence au bureau

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.icon = QLabel()
        self.icon.setPixmap(QPixmap(icon_path).scaled(64, 64, Qt.KeepAspectRatio))
        layout.addWidget(self.icon)

        self.label = QLabel(name)
        self.label.setStyleSheet("color: white;")
        layout.addWidget(self.label)

        self.setLayout(layout)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        print(f"Double-clic sur {self.name}")
        self.parent_desktop.launch_app(self.app_class)

class DesktopWidget(QWidget):  # ← maintenant elle est bien définie globalement
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setStyleSheet("background: transparent;")
        self.open_windows = []  # ← on garde les apps ouvertes ici

    def set_icons(self, app_list):
        for i, app in enumerate(app_list):
            row = i // 6
            col = i % 6
            icon = IconWidget(app['class'], app['icon'], app['name'], self)
            self.layout.addWidget(icon, row, col)

    def launch_app(self, app_class):
        instance = app_class()
        instance.show()
        self.open_windows.append(instance)
