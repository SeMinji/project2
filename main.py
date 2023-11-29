from PyQt6.QtWidgets import QApplication
from gui import VoteApp

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = VoteApp()
    window.show()
    sys.exit(app.exec())
