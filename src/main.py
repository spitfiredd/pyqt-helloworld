import sys
from PyQt5 import QtWidgets

from .ui import Ui_Dialog


class TestApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(TestApp, self).__init__(parent)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.name_input.textChanged[str].connect(self.on_change)
        self.show()

    # My test app doesn't have any GUI boilerplate just my application
    # logic
    def on_change(self, text):
        text = 'Hello {}!'.format(text)
        self.results_window.setText(text)
        self.results_window.adjustSize()


if __name__ == '__main__':
    # Run outside of pyxll
    app = QtWidgets.QApplication(sys.argv)
    qt_app = TestApp()
    sys.exit(app.exec_())
