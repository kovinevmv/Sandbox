import requests, json

class Auth:
    def __init__(self):
        self.auth_url = 'http://local.gazprom-classes.etu.ru:70/api/auth/login'
    
    def auth_user(self, user):
        return self.auth(user.login, user.password)

    def auth(self, login, password):
        form_data = {'login': login, 'password': password, 'saveMe': False}
    
        s = requests.Session()
        resp = s.post(self.auth_url, data=json.dumps(form_data), headers={'Content-Type': 'application/json;charset=UTF-8'})

        print(f'Auth as user: {login}:{password}, Session: {s.cookies.get_dict()}')
        return s