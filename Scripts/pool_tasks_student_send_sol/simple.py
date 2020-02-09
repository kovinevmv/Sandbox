import json
import requests

from multiprocessing import Pool

TEST_ID = 1
COURSE_ID = 1
user_auth = 'Lavonne.Bartell@hotmail.com:YNVkkMnUGgM0rzP'
LEN_MESSAGE = 50


def auth(data):
    s = requests.Session()
    login, password = data.split(':')
    data = {'login': login, 'password': password, 'saveMe': False}
    resp = s.post('http://local.gazprom-classes.etu.ru:70/api/auth/login', data=json.dumps(data),
                  headers={'Content-Type': 'application/json;charset=UTF-8'})
    print('Auth:', resp, resp.text[:LEN_MESSAGE] + '...')
    return s


def start_course(session):
    course_url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{COURSE_ID}/start'
    resp = session.post(course_url)
    print('Start course:', resp, resp.text[:LEN_MESSAGE] + '...')


def start_test(session):
    test_url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{COURSE_ID}/tests/{TEST_ID}/start'
    resp = session.post(test_url)
    print('Start test:', resp, resp.text[:LEN_MESSAGE] + '...')


def progress_test(session):
    payload = {"test": [{"id": 2, "answer": None}, {"id": 3, "answer": None}, {"id": 4, "answer": None},
                        {"id": 1, "answer": None}, {"id": 6, "answer": None}, {"id": 5, "answer": None},
                        {"id": 7, "answer": ["Object001"]}]}
    session.headers.update({'Content-Type': 'application/json;charset=UTF-8'})
    resp = session.put(
        f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{COURSE_ID}/tests/{TEST_ID}/progress',
        data=json.dumps(payload))

    print('Progress:', resp, resp.text[:LEN_MESSAGE] + '...')


def call_parallel(session):
    p = Pool(10)
    p.map(progress_test, [session for _ in range(10)])


def call_sequence(session):
    for _ in range(10):
        progress_test(session)


session = auth(user_auth)
start_course(session)
start_test(session)

call_parallel(session)
# call_sequence(session)
