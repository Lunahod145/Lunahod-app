import sys
import threading

from lunohod_app._app.ui import Ui_MainWindow

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtMultimedia import QMediaPlayer


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self._ui.video_widget)


def start_gui() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


def main() -> None:
    gui_thread = threading.Thread(target=start_gui)
    gui_thread.start()


if __name__ == "__main__":
    main()
