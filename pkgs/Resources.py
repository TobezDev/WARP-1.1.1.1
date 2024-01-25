import asyncio
import time
import sys
import random

from colorama import Fore, Style

from pkgs.Colors import Colors

used_ids = []


def colorInput(prompt: str):
    if prompt.lower() == 'default':
        prompt = '>>>'
    x = input(Colors.INPUT_DEFAULT + prompt + "   " + Style.RESET_ALL + Colors.MENU_WHITE)
    return x


async def sleepByType(t: str, d: int):
    if type not in ['p', 'a', 'c', 'program', 'activity', 'current']:
        raise ValueError(
            Style.BRIGHT + Fore.RED +
            "Value {} given in Function sleepByType where only 'p', 'a' and 'c' allowed."
            .format(t) + Style.RESET_ALL)
    else:
        if t in ['p', 'program']:
            time.sleep(d - .05)
        elif t in ['a', 'activity', 'c', 'current']:
            await asyncio.sleep(d - .05)
        else:
            raise ValueError(
                Style.BRIGHT + Fore.RED +
                "Value {} given in Function sleepByType where only 'p' and 'a' allowed."
                .format(t) + Style.RESET_ALL)


def typePrint(text: str, speed: str):
    if speed[0].lower() not in ['f', 'fast', 'a', 'average', 's', 'slow']:
        return ValueError(
            "Speed of function typePrint must be fast ('f'), average ('a') or slow ('s')."
        )
    else:
        if speed in ['f', 'fast']:
            delay = 0.05
        elif speed in ['a', 'average']:
            delay = 0.15
        elif speed in ['s', 'slow']:
            delay = 0.30
        else:
            return ValueError(f"{Colors.ERROR}")
        print(Colors.TEXT_DEFAULT, end=None)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print('\n')
        time.sleep(0.5)


def createName(name: str):
    identifier = 1
    while identifier in used_ids:
        identifier = random.randint(1, 255)
    used_ids.append(identifier)
    name = "192.168.0.{}".format(name)
    return [name, str(identifier)]
