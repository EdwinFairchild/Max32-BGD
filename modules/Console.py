from main_app import *
from modules import Slots
from modules import MiscHelpers

interface = None


def console_init(main_interface):
    global interface
    interface = main_interface


def log(data):
    global interface
    print(data)
    # interface.ui.console.verticalScrollBar().setSliderPosition(10)


def errMsg(data):
    log(str(data))
