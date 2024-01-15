'''
用户视图层
'''
import sys
from PyQt6.QtWidgets import QWidget,QApplication
from ui.login import Ui_Form
from conf import settings

import logging
from conf import settings
test_logger = logging.getLogger('视图层')

class LoginWindow(QWidget):

    def login(self):
        test_logger.debug('登录')

    def open_register_page(self):
        test_logger.debug('打开注册界面')




def run():
    app = QApplication(sys.argv)
    login_window  = LoginWindow()
    ui = Ui_Form()
    ui.setupUi(login_window)

    login_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()