from auth import Auth

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.session = Auth().auth(self.login, self.password)

    def get_session(self):
        return self.session


