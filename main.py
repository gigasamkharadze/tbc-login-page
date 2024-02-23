from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
from PyQt5 import QtCore


class MyWindow(QMainWindow):
    def __init__(self, email='gigasamkharadzee@gmail.com', password='123456'):
        super(MyWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.email = email
        self.password = password
        self.set_up_ui()

    def set_up_ui(self):
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login)
        self.setFixedWidth(800)
        self.setFixedHeight(700)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        if email == self.email and password == self.password:
            self.handle_login()
        else:
            self.handle_invalid_login()

    def handle_login(self):
        self.stackedWidget.setCurrentIndex(1)

    def handle_invalid_login(self):
        self.invalid_password_label.setText('Invalid email or password')
        self.password_input.setStyleSheet('border: 1px solid red')
        self.email_input.setStyleSheet('border: 1px solid red')


app = QApplication(sys.argv)
window = MyWindow('1', '1')
window.show()
sys.exit(app.exec_())
