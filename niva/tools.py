
import urllib
import requests



def is_internet_access():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=2)
        return True
    except: 
        return False

def is_niva_verification_required():
    try:
        flag = 'seanet' in requests.get('http://216.58.192.142').text
    except:
        return 'undefined'
    return flag

