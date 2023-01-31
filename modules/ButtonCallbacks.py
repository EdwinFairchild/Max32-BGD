
from main_app import *
from modules import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import zlib
import sys
import time
from . charSettingsWidget import Ui_widgetChar
from . serviceSettingsWidget import Ui_widgetService
from . descriptorSettingsWidget import Ui_widgetDescriptor

# ----------

timeTodelete = False
# TODO turn into dictionary
attributeDict = {}


def btn_add_descriptor(interface):
    test = attributeDict[f"attribute: 5"]
    test[0].label_9.setText(f"I am : {interface.services['count']}")

# ------------------------------------------------------------------------


def btn_add_service(interface):

    # Add top level element to Gatt Server Tree Widget
    temp_name = f"Service [{interface.services['count']}]"
    newService = QTreeWidgetItem([temp_name])
    interface.ui.gatt_tree.addTopLevelItem(newService)

    # highlight and select current top-level item in Gatt Tree Widget
    interface.ui.gatt_tree.setCurrentItem(
        interface.ui.gatt_tree.topLevelItem(interface.services['count']))
    interface.selected_service = interface.ui.gatt_tree.currentItem()

    # Add widget to Main Scroll Area
    scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
    widget = QWidget()           # Widget that contains the collection of Vertical Box

    # Make an empty widget to load the service widget UI into
    tempWidget = QtWidgets.QWidget()
    uiwidget = Ui_widgetService()
    tempWidget.setMinimumHeight(790)
    uiwidget.setupUi(tempWidget)
    tempWidget.setLayout(QVBoxLayout())
    uiwidget.lbl_service_name.setText(temp_name)

    # add to grid layout row,column ( when vbox =  gridlayout)
    #interface.vbox.addWidget(tempWidget, interface.services['count'], 0)
    # add to vertical layout 
    interface.vbox.addWidget(tempWidget)
    interface.vbox.setContentsMargins(QMargins(5, 5, 5, 5))
    attributeDict[f"attribute: {interface.services['count']}"] = (
        uiwidget, interface.services['count'])
    # retreive the widget object from the tuple in the dictionary
    test = attributeDict[f"attribute: {interface.services['count']}"]
    # test[0].label_9.setText(f"I am : {interface.services['count']}")

    # connect callbacks and change name label
    # uiwidget.btnToggle_permit_read.clicked.connect(
    #     lambda state: btn_read_property(interface, test[1]))
    widget.setLayout(interface.vbox)

    interface.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    interface.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    interface.ui.scrollArea.setWidgetResizable(True)
    interface.ui.scrollArea.setWidget(widget)
    
    # add new item to service list
    layout = QGridLayout()
    service_dict = {'grid_index': interface.services['count'],
                    'scroll_area': uiwidget.serviceScrollArea, 'grid_layout': layout, 'char_count': 0, 'chars': None}
    interface.services[f"Service [{interface.services['count']}]"] = service_dict
    interface.services['count'] += 1

    # # removes the 0th item in list until list is empty
    # vbox.removeWidget(attributeDict[0])
    # attributeDict.remove(attributeDict[0])
    # timeTodelete =False

    # register widget callback

    # get the item
    # gattTreeWidgetItem = interface.ui.gatt_tree.currentItem()
    # print("crurent item")
    # print(gattTreeWidgetItem.text(0))
    # child = QTreeWidgetItem([f"test {interface.services['count']}"])
    # parent = gattTreeWidgetItem.parent()
    # print(parent)
    # gattTreeWidgetItem.addChild(child)

# ------------------------------------------------------------------------


def btn_add_char(interface):
    global timeTodelete
    global attributeDict

    # get the top level service of the currently higlghted Gatt Tree Widget item
    topLevelService = interface.ui.gatt_tree.currentItem()
    while topLevelService.parent() != None:
        topLevelService = topLevelService.parent()

    # prints the text of the current item, text is used as key value in interface.services dictionary
    # print(f"parent : {gattTreeWidgetItem.text(0)}")

    # make a new characteristic widget
    widget = QWidget()      # Widget that contains the collection of Vertical Box

    tempWidget = QtWidgets.QWidget()
    uiwidget = Ui_widgetChar()
    tempWidget.setMinimumHeight(460)

    uiwidget.setupUi(tempWidget)
    uiwidget.lbl_char_name.setText(
        f"Char[{interface.services[topLevelService.text(0)]['char_count']}]")
   # interface.services[topLevelService.text(0)]["char_count"] +=1
    # Add characteristic widget gridlayout of parent service
    layout2 = interface.services[topLevelService.text(0)]['grid_layout']
    layout2.addWidget(
        tempWidget, interface.services[topLevelService.text(0)]['char_count'], 0)
    layout2.setContentsMargins(QMargins(5, 5, 5, 5))

    # add child to Gatt tree widget
    child = QTreeWidgetItem(
        [f"Char[{interface.services[topLevelService.text(0)]['char_count']}]"])
    parent = topLevelService.parent()
    topLevelService.addChild(child)

    interface.services[topLevelService.text(0)]['char_count'] += 1

    # # removes the 0th item in list until list is empty
    # vbox.removeWidget(attributeDict[0])
    # attributeDict.remove(attributeDict[0])
    # timeTodelete =False

    # register widget callback

    widget.setLayout(layout2)

    # interface.service_scroll_areas[interface.services['count']-1].setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    # interface.service_scroll_areas[interface.services['count']-1].setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    # interface.service_scroll_areas[interface.services['count']-1].setWidgetResizable(True)
    interface.services[topLevelService.text(
        0)]['scroll_area'].setWidget(widget)


# ------------------------------------------------------------------------

def btn_github(interface):
    webbrowser.open('https://github.com/EdwinFairchild/Max32-BGD')
# ------------------------------------------------------------------------


def register_button_callbacks(interface):
    # Menu button callbacks

    interface.ui.btnRepo.clicked.connect(lambda state: btn_github(interface))

    interface.ui.btn_Add_Characteristic.clicked.connect(
        lambda state: btn_add_char(interface))
    interface.ui.btn_Add_Service.clicked.connect(
        lambda state: btn_add_service(interface))
    interface.ui.btn_Add_Descriptor.clicked.connect(
        lambda state: btn_add_descriptor(interface))
