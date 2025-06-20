import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from core.desktop import DesktopWidget
from core.taskbar import Taskbar
from core.app_loader import load_apps

class HessOS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HessOS")
        self.setGeometry(0, 0, 1280, 720)
        self.showFullScreen()

        # Préparer le QLabel qui affichera le fond d'écran
        self.wallpaper = QLabel(self)
        self.wallpaper.setFixedSize(self.size())
        self.wallpaper.move(0, 0)
        self.wallpaper.lower()  # mettre derrière tout le reste
        # self.wallpaper.setStyleSheet("background: black;")  # désactivé temporairement

        # Central widget avec layout vertical (desktop + taskbar)
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        central.setLayout(layout)

        # Bureau
        self.desktop = DesktopWidget()
        layout.addWidget(self.desktop)

        # Taskbar
        self.taskbar = Taskbar(self.desktop)
        layout.addWidget(self.taskbar)

        # Charger les apps
        apps = load_apps()
        self.desktop.app_list = apps
        self.desktop.set_icons(apps)
        self.taskbar.desktop = self.desktop

    def resizeEvent(self, event):
        super().resizeEvent(event)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        wallpaper_path = os.path.join(script_dir, "assets", "wallpaper.png")
        pixmap = QPixmap(wallpaper_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
            self.wallpaper.setPixmap(pixmap)
            self.wallpaper.setFixedSize(self.size())
            self.wallpaper.move(0, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    os = HessOS()
    os.show()
    sys.exit(app.exec())
