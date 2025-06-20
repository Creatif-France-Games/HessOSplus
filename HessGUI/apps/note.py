from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog, QHBoxLayout
)
from PySide6.QtGui import QFont
import os

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NoteBloc")
        self.resize(600, 400)

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Consolas", 12))

        self.open_btn = QPushButton("📂 Ouvrir")
        self.save_btn = QPushButton("💾 Sauvegarder")

        self.open_btn.clicked.connect(self.ouvrir_fichier)
        self.save_btn.clicked.connect(self.sauvegarder_fichier)

        top_bar = QHBoxLayout()
        top_bar.addWidget(self.open_btn)
        top_bar.addWidget(self.save_btn)

        layout = QVBoxLayout()
        layout.addLayout(top_bar)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def ouvrir_fichier(self):
        chemin, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Texte (*.txt);;Tous les fichiers (*)")
        if chemin and os.path.exists(chemin):
            with open(chemin, 'r', encoding='utf-8') as f:
                self.text_edit.setPlainText(f.read())

    def sauvegarder_fichier(self):
        chemin, _ = QFileDialog.getSaveFileName(self, "Sauvegarder", "", "Texte (*.txt);;Tous les fichiers (*)")
        if chemin:
            with open(chemin, 'w', encoding='utf-8') as f:
                f.write(self.text_edit.toPlainText())

def get_icon():
    return "assets/icons/note.png"
