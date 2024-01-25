import time, os

from pkgs import Menus, Game, Resources

VERSION = "1.0*a"

Menus.Menus.TitleScreen.show()

time.sleep(3)
os.system('clear')

Menus.Menus.MainMenu.show()
