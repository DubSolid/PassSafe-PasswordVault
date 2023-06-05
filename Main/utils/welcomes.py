from .tcolors import tcolors


def banner():
    print(tcolors.GREEN('''
     _____  _______ _______ _______     _______ _______ _______ _______      _    _ _______ _     _        _______
    |_____] |_____| |______ |______ ___ |______ |_____| |______ |______       \  /  |_____| |     | |         |   
    |       |     | ______| ______|     ______| |     | |       |______        \/   |     | |_____| |_____    |                                                                                                                                   
    '''))


def display_welcome():
    print(tcolors.GREEN('Welcome to Pass-Safe Vault!'))


def welcomed_to_vault():
        seperator = '-' * 22
        print('\n')
        print(seperator)
        print(tcolors.GREEN('Welcome to your vault!'))
        print(seperator)


def print_banner():
     banner()
     display_welcome()
