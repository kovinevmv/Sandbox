import requests, json, random
from multiprocessing import Pool

path_users = '/home/venom/Desktop/git/gp-classes-backend/users.csv'


def read_users():
    users = []
    with open(path_users) as f:
        data = f.read().split('\n')
        for line in data:
            splited_line = line.split(',')
            email, password = splited_line[3], splited_line[4]
            users.append((email, password))
    return users


def auth(user):
    print('Call auth:', user)

    login, password = user[0], user[1]
    data = {'login': login, 'password': password, 'saveMe': False}
    s = requests.Session()
    resp = s.post('http://local.gazprom-classes.etu.ru:70/api/auth/login', data=json.dumps(data), headers={'Content-Type': 'application/json;charset=UTF-8'})
    print('Resp:', resp.text)
    
    return s

def admission(session):
    course_url = 'http://local.gazprom-classes.etu.ru:70/api/education/courses/1/start'
    print('Admintion to course:', course_url)

    resp = session.post(course_url)
    print('Resp:', resp.text)


def start_test(session):
    s_link = 'http://local.gazprom-classes.etu.ru:70/api/education/courses/tests/1/start'
    print('Start to course:', s_link)
    resp = session.post(s_link)
    print('Resp:', resp.text)

def submit(session):
    link = 'http://local.gazprom-classes.etu.ru:70/api/education/courses/tests/1/progress'

    data = {"test":[{"id":2,"answer":[1]},{"id":3,"answer":[2]},{"id":1,"answer":[1]},{"id":4,"answer":[2]}]}

    cookies_task = {'test_1_3_text': "%5B1%5D", "test_1_4_text": "%5B2%5D", "test_1_2_text" : "%5B1%5D", "ebook1": "5", "test_1_5_text": "%5B2%5D"}
    for cookie_name, cookie_vakue in cookies_task.items():
        session.cookies[cookie_name] = cookie_vakue
    
    print('Submit asnwer:', json.dumps(data))
    resp = session.put(link, data=json.dumps(data), headers={'Content-Type':'application/json;charset=UTF-8'})
    print('Resp: ', resp.text)

def solve(s):
    submit(s)


users = read_users()[150:200]
ss = []

for user in users:
    session = auth(user)
    admission(session)
    start_test(session)
    ss.append(session)

p = Pool(len(ss))
p.map(solve, ss)



