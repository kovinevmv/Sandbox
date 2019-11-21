from multiprocessing import Pool
from urllib.parse import unquote, quote
import requests, re, json

COOKIES_PATH = './cookies'
URL = 'http://local.gazprom-classes.etu.ru:70/api/education/courses/tests/1/progress'

with open(COOKIES_PATH) as f:
    data = f.read()
    cookies = {}
    for pair in data.split('; '):
        cookies_parsed = pair.split('=')
        cookies[cookies_parsed[0]] = cookies_parsed[1]

def get_user_solutions():
    solutions = []
    for cookie_name, cookie_value in cookies.items():
        if 'test' in cookie_name:
            res = re.findall("test_\d+_(\d+)_(\w+)", cookie_name)[0]
            solutions.append((int(res[0])-1, res[1], unquote(cookie_value)[1:-1]))
    return solutions

def get_tasks_exclude_task(task, tasks):
    index = tasks.index(task)
    return tasks[:index] + tasks[index + 1 :]
    
def generate_tasks(task):
    generated = []
    if task[1] == 'text':
        for i in range(1, 10):
            generated.append((task[0], task[1], str(i)))
    return generated


def generate_solutions(solution):
    generated = []
    
    for task in solution:
        other_tasks = get_tasks_exclude_task(task, solution)
        new_tasks = generate_tasks(task)
        for new_task in new_tasks:
            generated.append(other_tasks + [new_task])
    return generated
       


def generate_cookie_by_sol(solution):
    current_cookies = cookies
    for cookie_name, cookie_value in current_cookies.items():
        if 'test' in cookie_name:
            index = int(re.findall("test_\d+_(\d+)_(\w+)", cookie_name)[0][0]) - 1
            for task in solution:
                if task[0] == index:
                    current_cookies[cookie_name] = quote('[' + task[2] + ']')
    return current_cookies

def generate_data_by_sol(solution):
    data = []
    for task in solution:
        answer = task[2]
        try:
            answer = int(answer)
        except:
            answer = answer[1:-1]
        data.append({"id": task[0], "answer": [answer]})
    return json.dumps({"test": data})


def call_request(i):
    solution = solutions[i]
    cookie = generate_cookie_by_sol(solution)
    data = generate_data_by_sol(solution)
    print(i, 'Send:', data)
    res = send_request(cookie, data)
    print(i, 'Response:', res)
    print()

def send_request(cookie, data):
    return requests.put(URL, cookies=cookie, data=data, headers={'content-type':'application/json;charset=UTF-8'}).text

solutions = generate_solutions(get_user_solutions())

def call_parallel():
    p = Pool(len(solutions))
    p.map(call_request, range(len(solutions)))

def call_sequence():
    for i in range(len(solutions)):
        call_request(i)


#call_parallel()
call_sequence()