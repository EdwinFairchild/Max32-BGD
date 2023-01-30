from main_app import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from modules import Console


def init_icons(interface):
    interface.ui.btnRepo.setIcon(QIcon('resources/icons/Github.svg'))


# ------------------------------------------------------------------------


def set_button_icons(interface, currentButton):
    for button in interface.buttonList:
        if button == currentButton:
            icon = interface.iconDictionary[currentButton][1]
            currentButton.setIcon(QIcon(icon))
            icon_size = QSize()
            icon_size.setHeight(20)
            icon_size.setWidth(20)
            currentButton.setIconSize(icon_size)

        elif button == interface.ui.btnMenu:
            pass

        else:
            icon = interface.iconDictionary[button][0]
            button.setIcon(QIcon(icon))
            icon_size = QSize()
            icon_size.setHeight(20)
            icon_size.setWidth(20)
            button.setIconSize(icon_size)
# ------------------------------------------------------------------------


def set_connected_icon_color(interface, color):
    if color == "blue":
        interface.ui.btnConnectedState.setIcon(
            QIcon('resources/icons/Ble_Large_Blue.svg'))
        icon_size = QSize()
        icon_size.setHeight(50)
        icon_size.setWidth(50)
        interface.ui.btnConnectedState.setIconSize(icon_size)
    else:
        interface.ui.btnConnectedState.setIcon(
            QIcon('resources/icons/Ble_Large.svg'))
        icon_size = QSize()
        icon_size.setHeight(50)
        icon_size.setWidth(50)
        interface.ui.btnConnectedState.setIconSize(icon_size)
# ------------------------------------------------------------------------


def copy_to_clipboard(interface, str):
    cp = QApplication.clipboard()
    cp.clear()
    cp.setText(str)
# ------------------------------------------------------------------------


def set_alternate_button_mode_color(interface, button, fore, back):
    stylesheet = f"QPushButton{{ text-align: center; background-color: rgb({back[0]}, {back[1]}, {back[2]});  ;border-radius:5px;color: rgb({fore[0]}, {fore[1]}, {fore[2]});border:none;}}QPushButton:hover{{color: rgb(255, 255, 255);background-color: rgb(170, 77, 77);}}QPushButton:pressed{{color: rgb(255, 255, 255);background-color: rgb(170, 27, 27);}}"
    button.setStyleSheet(stylesheet)
