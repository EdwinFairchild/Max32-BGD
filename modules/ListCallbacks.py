from main_app import *
from modules import Console
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def btn_gatt_tree_item_pressed(interface):

    topLevelService = interface.ui.gatt_tree.currentItem()
    while topLevelService.parent() != None:
        topLevelService = topLevelService.parent()

    gattTreeWidgetItemText = topLevelService.text(0)

    # scroll to currently selected item
    index = interface.services[topLevelService.text(0)]['grid_index']
    interface.ui.scrollArea.ensureWidgetVisible(
        interface.vbox.itemAt(index).widget())

# ------------------------------------------------------------------------


def register_list_callbacks(interface):

    interface.ui.gatt_tree.itemPressed.connect(
        lambda state: btn_gatt_tree_item_pressed(interface))
