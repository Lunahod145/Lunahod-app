import sys
import typing as t
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtMultimedia import QMediaPlayer

from .ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self._ui.video_widget)


class GUIThread(Thread):
    def __init__(self, argv: t.Sequence[str] = []) -> None:
        self._argv = argv

    def run(self) -> None:
        app = QApplication(self._argv)

        window = MainWindow()
        window.show()

        sys.exit(app.exec())
