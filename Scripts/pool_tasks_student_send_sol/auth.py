from multiprocessing import Pool

import json
import requests

path_users = '/home/alien/Desktop/git/gp-classes-backend/users.csv'


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
    resp = s.post('http://local.gazprom-classes.etu.ru:70/api/auth/login', data=json.dumps(data),
                  headers={'Content-Type': 'application/json;charset=UTF-8'})
    print('Resp:', resp.text)

    return s


def admission(session):
    course_url = 'http://local.gazprom-classes.etu.ru:70/api/education/courses/1/start'
    print('Admintion to course:', course_url)

    resp = session.post(course_url)
    print('Resp:', resp.text)


def start_test(session):
    s_link = 'http://local.gazprom-classes.etu.ru:70/api/education/courses/1/tests/1/start'
    print('Start to course:', s_link)
    resp = session.post(s_link)
    print('Resp:', resp.text)


def submit(session):
    link = 'http://local.gazprom-classes.etu.ru:70/api/education/courses/1/tests/1/progress'

    data = {"test": [{"id": 6, "answer": None}, {"id": 5, "answer": None}, {"id": 4, "answer": ["Object001"]},
                     {"id": 3, "answer": [4]}, {"id": 1, "answer": "\\imath -19 \\Longleftarrow -40 \\star -98 "},
                     {"id": 7, "answer": ["Object001"]}, {"id": 2,
                                                          "answer": "-1 \\measuredangle \\ast \\succnsim \\psi \\longmapsto \\geqslant 49 \\propto \\Psi \\ntrianglelefteq \\ddagger 88 "}]}

    print('Submit asnwer:', json.dumps(data))
    resp = session.put(link, data=json.dumps(data), headers={'Content-Type': 'application/json;charset=UTF-8'})
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
