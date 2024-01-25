from colorama import Fore, Style


class Colors:

    ERROR = f"{Style.BRIGHT+ Fore.RED}"

    MENU_DEFAULT = f"{Style.RESET_ALL + Style.BRIGHT + Fore.LIGHTMAGENTA_EX}"

    MENU_RED = f"{Fore.RED}"
    MENU_YELLOW = f"{Fore.LIGHTYELLOW_EX}"
    MENU_GREEN = f"{Fore.GREEN}"
    MENU_CYAN = f"{Fore.CYAN}"

    MENU_LIST = f"{Fore.WHITE}"
    MENU_TITLE = f"{Fore.WHITE}"
    MENU_WHITE = f"{Fore.WHITE}"

    TEXT_DEFAULT = f"{Style.RESET_ALL}{Style.BRIGHT}{MENU_WHITE}"
    INPUT_DEFAULT = f"{Style.RESET_ALL}{Style.BRIGHT}{MENU_WHITE}"


class Effects:

    DIM = Style.DIM
    BOLD = Style.BRIGHT
    NORMAL = Style.NORMAL
    RESET_ALL = Style.RESET_ALL
