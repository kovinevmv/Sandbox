import yaml
import datetime
import urllib
import requests

def read_file_in_yaml(path):
    with open(path, 'r') as f:
        info = yaml.safe_load(f.read())
    return info

def write_file_in_yaml(info, path):
    with open(path, 'w') as f:
        f.write(yaml.dump(info))

def datatime_to_str(data):
    return data.strftime("%Y-%m-%d-%H.%M.%S")

def create_new_mac_stat(mac):
    return {'success_attemps_count': 0, 'last_access': datatime_to_str(datetime.datetime(1970, 1, 1, 0, 0, 1)), 'total_attempts_count': 0, 'speed': []}
    
def check_new_macs_in_yaml(data):
    macs = data['macs']
    for mac in macs:
        if mac not in data.keys():
            print("Found new mac: {}".format(mac))
            data[mac] = create_new_mac_stat(mac)

def sort(data):
    l, d = reversed(sorted(data.items(), key=lambda x: x[1]['last_access'] if x[0] != 'macs' else datatime_to_str(datetime.datetime.now()))), {}
    for key, value in l:
        d[key] = value
    return d

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

