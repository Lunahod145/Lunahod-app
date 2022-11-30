from lunohod_app._app.gui import GUIThread


def main() -> None:
    gui_thread = GUIThread()
    gui_thread.start()


if __name__ == "__main__":
    main()
