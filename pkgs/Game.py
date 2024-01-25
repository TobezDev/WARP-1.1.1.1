import os

from .Colors import Colors
from .Resources import colorInput, createName, typePrint, sleepByType


def PlayNew():
    _ = input()
    os.system('clear')
    typePrint(
        speed='f',
        text="Welcome, packet! This is the Hub. Enter a name to get started:"
    )
    global name, username, user_identifier
    name = colorInput('default')
    username, user_identifier = createName(name)
    typePrint(
        speed='f',
        text=f"Welcome {name}, your identifier is {Colors.MENU_CYAN}{username}{Colors.TEXT_DEFAULT}. This'll be your name across the network, so don't forget it!"
    )
    
