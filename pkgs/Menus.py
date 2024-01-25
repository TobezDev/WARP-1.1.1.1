import os

from colorama import Fore, Style, Back

from pkgs.Resources import colorInput
from pkgs import Game
from pkgs.Colors import Colors

VERSION = "1.0*a"

class Menus:
	class MainMenu:
		@classmethod
		def show(cls):
			print(f"""{Colors.MENU_DEFAULT}
[ ================= ]
[ === {Colors.MENU_LIST}Main Menu{Colors.MENU_DEFAULT} === ]
[ ================= ]
[ {Colors.MENU_LIST}1. {Colors.MENU_GREEN}New Game{Colors.MENU_DEFAULT}       ]
[ {Colors.MENU_LIST}2. {Colors.MENU_YELLOW}Help{Colors.MENU_DEFAULT}           ]
[ {Colors.MENU_LIST}3. {Colors.MENU_YELLOW}Credits{Colors.MENU_DEFAULT}        ]
[ {Colors.MENU_LIST}4. {Colors.MENU_RED}Exit{Colors.MENU_DEFAULT}           ]""")
			main = colorInput('default')
			os.system('clear')
			if main == '1':
				Menus.Game.NewGame.show()
			elif main == '2':
				menu = f"""{Colors.MENU_DEFAULT}
[ ================= ]
[ === {Colors.MENU_LIST}Help Menu{Colors.MENU_DEFAULT} === ]
[ ================= ]
[      {Colors.MENU_LIST}The Aim{Colors.MENU_DEFAULT}      ]
	1. 
				"""
			elif main == '3':
				menu = f"""{Colors.MENU_DEFAULT}
[ ================== ]
[ = {Colors.MENU_LIST}Credits{Colors.MENU_DEFAULT} = ]
[ ================== ]
[ 1.    Developer    ]
	- replit/@TobezEdu
	- github/@tobezdev
[ 2.    Testers      ]
	- github/@cromite
	- github/
			"""
			elif main == '4':
				exit(Colors.ERROR + "Game was quit." + Style.RESET_ALL)
			else:
				raise ValueError(Colors.ERROR + "Value {} given in Function main where only '1', '2', '3' and '4' allowed.".format(main))

	class TitleScreen:
		@classmethod
		def show(cls):
			print(f"""{Colors.MENU_DEFAULT}
[ ================= ]
[ ====== {Colors.MENU_TITLE}The{Colors.MENU_DEFAULT} ====== ]
[ ==== {Colors.MENU_TITLE}Network{Colors.MENU_DEFAULT} ==== ]
[ === {Colors.MENU_TITLE}Adventure{Colors.MENU_DEFAULT} === ]
[ ================= ]
[ = {Colors.MENU_TITLE}By: @TobezEdu{Colors.MENU_DEFAULT} = ] 
[ ================= ]
[ == {Colors.MENU_TITLE}Vrsn: {Colors.MENU_CYAN}{VERSION}{Colors.MENU_DEFAULT} == ]
[ ================= ]""")

	class NewGameScreen:
		@classmethod
		def show(cls):
			print(f"""{Colors.MENU_DEFAULT}
[ ================= ]
[ === {Colors.MENU_TITLE}New  Game{Colors.MENU_DEFAULT} === ]
[ ================= ]
[ == {Colors.MENU_TITLE}Press ENTER{Colors.MENU_DEFAULT} == ]
[ === {Colors.MENU_TITLE}To  Start{Colors.MENU_DEFAULT} === ]
[ ================= ]""")
			Game.PlayNew()
