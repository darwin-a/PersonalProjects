import sys
from PySide2.QtWidgets import QApplication
from spacer_app.interface import Window


def run():
    app = QApplication(sys.argv)

    gui = Window()

    gui.show()

    # load data from
    gui.load_data()
    app.setStyle('Fusion')

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
