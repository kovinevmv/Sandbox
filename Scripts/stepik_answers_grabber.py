import requests
import re
import json
import os


with open('cookies.txt', 'r') as f: 
    cookies_raw = json.loads(f.read())

cookies = {}
for cookie in cookies_raw:
    cookies[cookie['name']] = cookie['value']

def parse_url(url):
    regex = re.compile('[0-9]+');
    id = re.findall(regex, url)[0]
    if id == url:
        url = 'https://stepik.org/course/{}/syllabus'.format(id)
    return id, url
    
def parse_task(info, solution):
    correct_submission = list(filter(lambda x : x['status'] == 'correct', solution['submissions']))
    if not correct_submission:
        return [('Not', 'solved')]
    else:
        answer = correct_submission[0]['reply']
        result = []
        if 'options' in info and 'choices' in answer:
            text = info['options']
            answer = answer['choices']
            for variant, state in zip(text, answer):
                symbol = '+' if state else '-'
                result.append((symbol, variant))
        elif 'pairs' in info and 'ordering' in answer:
            text = info['pairs']
            answer = answer['ordering']
            for index, order in enumerate(answer):
                result.append((text[index]['first'] + " :", text[order]['second']))
        elif 'options' in info and 'ordering' in answer:
            text = info['options']
            answer = answer['ordering']
            result = [(_ + 1, text[order]) for _, order in enumerate(answer)]
        elif 'text' in answer:
            result.append(('Answer:', answer['text']))

    return result



id_user_solved_task = '19621617'
url_stepik_course = '2586'
stepik_api = 'https://stepik.org/api'
id, url_stepik_course = parse_url(url_stepik_course);

course_info = json.loads(requests.get('{}/courses/{}'.format(stepik_api, id)).text)
sections = course_info['courses'][0]['sections']

main_json = [None] * len(sections)

for index_section, section in enumerate(sections):
    section_info = json.loads(requests.get('{}/sections/{}'.format(stepik_api, section)).text)
    title_section = section_info['sections'][0]['title']
    units = section_info['sections'][0]['units']

    main_json[index_section] =  {'title': title_section, 'num': index_section + 1, 'content': [None] * len(units)}

    for index_lesson, unit in enumerate(units):

        unit_info = json.loads(requests.get('{}/units/{}'.format(stepik_api, unit)).text)
        lesson = unit_info['units'][0]['lesson']
        
        lesson_info = json.loads(requests.get('{}/lessons/{}'.format(stepik_api, lesson)).text)
        title_lesson = lesson_info['lessons'][0]['title']
        steps = lesson_info['lessons'][0]['steps']

        main_json[index_section]['content'][index_lesson] = {'title': title_lesson, 'num': index_lesson + 1, 'content': [None] * len(steps)}

        for index_step, step in enumerate(steps):
            attempts = json.loads(requests.get('{}/attempts?step={}&user={}'.format(stepik_api, step, id_user_solved_task), cookies=cookies).text)
            if (attempts['attempts']):
                task_info = attempts['attempts'][0]['dataset']
                solution = json.loads(requests.get('{}/submissions?&step={}&user={}'.format(stepik_api, step, id_user_solved_task), cookies=cookies).text)
                
                main_json[index_section]['content'][index_lesson]['content'][index_step] = {'solution': parse_task(task_info, solution)}
            else:
                main_json[index_section]['content'][index_lesson]['content'][index_step] = {'solution': [('Not', 'found attempts to solve')]}


def write_task(task, path):
    task = task['solution']
    with open(path, 'w') as f:
        for row in task:
            f.write(f"{row[0]} {row[1]}\n".encode().decode('cp1251'))


path = 'course_id{}'.format(id)
os.mkdir(path)

with open(path + '/dump.json', 'w') as f:
    f.write(json.dumps(main_json))


for section in main_json:
    index_section, title_section = section['num'], section['title']
    os.mkdir(f"{path}/{index_section}. {title_section}")
    for lesson in section['content']:
        index_lesson, title_lesson = lesson['num'], lesson['title']
        os.mkdir(f"{path}/{index_section}. {title_section}/{index_lesson}. {title_lesson}")
        for index_task, task in enumerate(lesson['content'], start=1):
            if task:
                write_task(task, f"{path}/{index_section}. {title_section}/{index_lesson}. {title_lesson}/{index_section}-{index_lesson}-{index_task}.txt")







