#!/usr/bin/python3.7

import re
import subprocess
from network import Network

def execute(command):
    try:
        return subprocess.check_output(command, 
                                        stderr=subprocess.PIPE, 
                                        stdin=subprocess.PIPE, 
                                        shell=True).decode().strip()       
    except:
        return ''
    
class MacChanger:
    def __init__(self, interface_name=''):
        self.set_interface(interface_name)

    def initialize_connection(self, network):
        self.network = network
        self.save_current_wifi()
        self.switch_to_new_network(self.network)

    def recover_origin_network(self):
        self.switch_to_new_network(self.origin_network)

    def save_current_wifi(self):
        network_name = execute('nmcli -t -f NAME connection show --active')
        regex = re.compile(r'(.*?)(?: [\d]+)?$')
        network_name_without_end_num = re.findall(regex, network_name)[0]

        password = execute(r'cat "/etc/NetworkManager/system-connections/' + network_name_without_end_num + r'" | grep -iPo "psk=\K(.*)"')
        self.origin_network = Network(network_name_without_end_num, password)
        print('Origin network saved:', self.origin_network)


    def switch_to_new_network(self, network):
        if self.origin_network and self.origin_network == network:
            print("[+] Origin network is", network, ". No switching required")
        else:
            print('[+] Swithching to network: ', network)
            execute("nmcli dev wifi connect \"{}\" password '{}'".format(network.network_name, network.password))
            print('[+] Switched')


    def change_mac(self, mac):
        print('[+] Changing MAC address to', mac)
        execute('service network-manager stop')
        execute('ifconfig {} down'.format(self.interface_name))
        execute('macchanger --mac="{}" {}'.format(mac, self.interface_name))
        execute('ifconfig {} up'.format(self.interface_name))
        execute('service network-manager restart')
        print('[+] Changed')
        execute('sleep 15')

    def set_interface(self, interface):
        if interface:
            self.interface_name = interface
            self.default_mac = self._get_mac_of_interface(interface)
        else:
            self.interface_name, self.default_mac = self._get_wireless_interfaces()

    def _get_wireless_interfaces(self):
        output = execute('iw dev')
        regex = re.compile(r'Interface (.*)?\n.*\n.*\n.*?addr (.*)')
        return re.findall(regex, output)[0]

    def _get_mac_of_interface(self, interface):
        output = execute('ifconfig {}'.format(interface))
        regex = re.compile(r"\s((?:[a-f0-9]{2}:){5}[a-f0-9]{2})")
        return re.findall(regex, output)[0]

    def __str__(self):
        return "Interface: {}; MAC: {}".format(self.interface_name, self.default_mac)
