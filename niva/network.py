class Network:
    def __init__(self, network_name, password):
        self._network_name = network_name
        self._password = password

    @property 
    def password(self):
        return self._password
    
    @property
    def network_name(self):
        return self._network_name

    def serialize(self):
        return {'network_name': self._network_name, 'password': self._password}

    def __str__(self):
        return 'Network(ESSID:"{}", password:"{}")'.format(self._network_name, self._password)

    def __eq__(self, value):
        return (self.network_name == value.network_name and
                self.password == value.password)
    