import yaml
import datetime

def datatime_to_str(data):
        return data.strftime("%Y-%m-%d-%H.%M.%S")



# TODO replace duplicate reg
class MacStatistic:
    def __init__(self, path):
        self.path = path
        self.data = self.read()
        self._check_new_macs_in_yaml()

    def read(self):
        with open(self.path, 'r') as f:
            info = yaml.safe_load(f.read())
        return info

    def write(self, data=''):
        if not data:
            data = self.data
        with open(self.path, 'w') as f:
            f.write(yaml.dump(data))

    def _create_new_mac_stat(self, mac):
        return {'success_attemps_count': 0, 
                'last_access': datatime_to_str(datetime.datetime(2019, 10, 20, 0, 0, 1)), 
                'total_attempts_count': 0, 
                'speed': []}

    def _check_new_macs_in_yaml(self, data=''):
        if not data:
            data = self.data
        macs = data['macs']
        for mac in macs:
            if mac not in data.keys():
                print("Found new mac: {}".format(mac))
                data[mac] = self._create_new_mac_stat(mac)
        self.data = data

    def sort(self):
        # TODO reversed as param
        l, d = reversed(sorted(self.data.items(), key=lambda x: x[1]['last_access'] if x[0] != 'macs' else datatime_to_str(datetime.datetime.now()))), {}
        for key, value in l:
            d[key] = value
        self.data = d

    def get_data(self):
        return self.data

    def failure(self, mac):
        self.data[mac] =  {'success_attemps_count': self.data[mac]['success_attemps_count'], 
                                'last_access': self.data[mac]['last_access'], 
                                'total_attempts_count': self.data[mac]['total_attempts_count'] + 1, 
                                'speed': self.data[mac]['speed']}
        self.write()

    def success(self, mac):
        self.data[mac] =  {'success_attemps_count': self.data[mac]['success_attemps_count'] + 1, 
                                'last_access': datatime_to_str(datetime.datetime.now()), 
                                'total_attempts_count': self.data[mac]['total_attempts_count'] + 1, 
                                'speed': self.data[mac]['speed']}
        self.write()
