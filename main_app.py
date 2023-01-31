from click import style
from main_gui import Ui_MainWindow
from modules import ButtonCallbacks
from modules import ListCallbacks
from modules import MiscHelpers
from modules import SerialThread as ser_ctl
from modules import Console
from PyQt5 import Qt as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation, QPoint, QEasingCurve, pyqtSignal, QSequentialAnimationGroup
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QPushButton, QToolTip
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from bleak import *
import asyncio
import platform
import sys
import os
import time
import atexit
from asyncqt import QEventLoop
import webbrowser


QtWidgets.QApplication.setAttribute(
    QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
os.environ["QT_FONT_DPI"] = "96"


class MainInterface(QMainWindow):
    # OS check should a reason to do something different on each arise
    # if sys.platform == 'win32':
    #     print("Windows")
    # else:
    #     print("Linux!")

    # TODO : Refactor a lof of these parameters/flasgs that could be
    #        turned into pyqtSignals

    # TODO move this to seprate file
    # This grid layout will live in the scroll area of the Designer
    #vbox = QGridLayout()
    vbox = QVBoxLayout()
    services = {'count': 0}
    selected_service = None

    def __init__(self):
        QMainWindow.__init__(self)
        # setup gui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        Console.console_init(self)

        ButtonCallbacks.register_button_callbacks(self)
        ListCallbacks.register_list_callbacks(self)
        MiscHelpers.init_icons(self)

        self.ui.scrollArea.setStyleSheet("""
        /* VERTICAL */
        QScrollBar:vertical {
            border: none;
            background: rgb(39, 52, 105);
            width: 10px;
            margin: 10px 0px 10px 0px;
           
        }

        QScrollBar::handle:vertical {
            background: rgb(170,200,255);
            min-height: 26px;
            
        }

        QScrollBar::add-line:vertical {
            background: none;
            height: 26px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
            
        }

        QScrollBar::sub-line:vertical {
            background: none;
            height: 26px;
            subcontrol-position: top left;
            subcontrol-origin: margin;
            position: absolute;
            
        }

        QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
            width: 26px;
            height: 20px;
            background: white;
            
            
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
            
        }

    """)

    # ------------------------------------------------------------------------
    # def eventFilter(self, source, event):

    #     if event.type() == QtCore.QEvent.Enter and source == self.ui.sideBar:
    #         self.menuAnimate(self.ui.sideBar, True)
    #     if event.type() == QtCore.QEvent.Leave and source == self.ui.sideBar:
    #         self.menuAnimate(self.ui.sideBar, False)
    #     return super().eventFilter(source, event)
    # ------------------------------------------------------------------------

########################################################################################


def exitFunc():
    # TODO add cleanup code as necessary
    Console.log("Goodbye")


    # ------------------------------------------------------------------------
if __name__ == '__main__':
    # todo: compile resurces into python files, not sure if its even necessary at this point
    # pyrcc5 image.qrc -o image_rc.py
    # compile gui
    os.system("pyuic5 -x main_gui.ui -o main_gui.py")
    atexit.register(exitFunc)
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    loop = QEventLoop(app)
    # asyncio.set_event_loop(loop)
    interface = MainInterface()
    interface.show()

    app.exec_()
