import re

class Parser:
    def __init__(self, file_csv, network_name='niva_sv'):
        self.file_csv = file_csv
        self.network_name = network_name
    
    def _read_file(self):
        with open(self.file_csv, 'r') as f:
            data = f.read()
        return data
    
    def parse(self):
        data = self._read_file()
        regex = re.compile(r'((?:[0-9A-F]{2}:){5}[\dA-F]{2}), \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, +\d+, +\d+, WPA2?, CCMP,PSK, -\d{2}, +\d+, +\d+,  +0.  0.  0.  0, +\d+, ' + self.network_name + ',')
        niva_macs = re.findall(regex, data)
            macs = []
        for niva_mac in niva_macs:
            regex_macs = re.compile(r'((?:[0-9A-F]{2}:){5}[\dA-F]{2}), \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, +\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, +-\d+, +\d+, +' + niva_mac)
            macs_of_current_niva = re.findall(regex_macs, data)
            macs += macs_of_current_niva

        return macs
    
p = Parser('/home/alien/macs_dump_2019_11_09.csv-01.csv')
print(p.parse())