#!/usr/bin/python3.7

from time import sleep


from tools import *
from mac_changer import *
from network import Network
from mac_stat import MacStatistic


macs_file_path = '/home/alien/Desktop/git/Sandbox/Scripts/macs.txt'


niva_sv = Network('niva_sv', '9cVEr3Sda')

changer = MacChanger()
changer.initialize_connection(niva_sv)


macs_statistic = MacStatistic(macs_file_path)
macs_statistic.sort()

print('Starting "niva_sv" connection...')

for mac, statistic in macs_statistic.get_data().items():
    if mac != 'macs':
        changer.change_mac(mac)
        print('Wait reconnecting to network', end='')
        while (is_internet_access() == False):
            sleep(1)
            print('.', end='', sep='')
        r = is_niva_verification_required()
        print('\nInternet access:', is_internet_access(), 'niva:', r)
        if not r:
            macs_statistic.success(mac)
            print('Find')
            break
        macs_statistic.failure(mac)

#TODO remove very old

#    try_connect_network(network)
#    res = check_access_internet()
#    if res:
#        speed = check_speed(macs_statistic, mac)
#        success(speed)
#        print('Success')
#        exit(0)
#    else:
#        update_statistic_failure(macs_statistic, mac['mac'], )
#    
#    write_stat(macs_file_path)


#def success(macs_file_path, macs_statistic):
#    update_statistic_success(macs_statistic, mac['mac'])
#    write_stat()
