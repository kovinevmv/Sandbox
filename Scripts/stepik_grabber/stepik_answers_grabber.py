import requests
import re
import json
import os
from stepik_api import StepikAPI


course_id = '10524'





path = 'course_id{}'.format(course_id)
os.mkdir(path)

with open('dump.json', 'r') as f:
    main_json = json.loads(f.read())

def write_step(path, data):
    with open(path, 'w') as f:
        for d in data:
            f.write(str(d[0]) + ' ' + str(d[1]) + '\n')

for section_id, section_info in main_json.items():
    title_section = section_info['title']
    os.mkdir(f"{path}/{title_section}")
    for unit in section_info['units']:
        unit_title = list(unit.values())[0]['title']
        os.mkdir(f"{path}/{title_section}/{unit_title}")
        for step in list(unit.values())[0]['steps']:
            print(step['num'], step['answer'])
            write_step(f"{path}/{title_section}/{unit_title}/" + str(step['num']), step['answer'])


c = StepikAPI(course=course_id)

sections = c.get_sections_of_course()
units = c.get_units_by_sections(sections)

# Indexing titles of sections
for index, section in enumerate(sections, start=1):
    units[section]['title'] = '{}. {}'.format(index, units[section]['title'])

main_json = units

def dump_json(file, path):
    with open(path, 'w') as f:
        f.write(json.dumps(main_json))

for section_id, unit_data in units.items():
    lessons = c.get_lessons_from_units(unit_data['units'])
    main_json[section_id]['units'] = lessons

    steps = c.get_steps_from_lessons(lessons)
    for lesson_id, lesson_info in steps.items():
        index_of_l = main_json[section_id]['units'].index(lesson_id)
        lesson_info['title'] = '{}. {}'.format(index_of_l + 1, lesson_info['title'])
        lesson_info.update({'num': index_of_l + 1})
        main_json[section_id]['units'][index_of_l] = {lesson_id: lesson_info}
    
    for lesson_id, lesson_data in steps.items():
        steps_list = lesson_data['steps']
        for i, el in enumerate(main_json[section_id]['units']):
            if lesson_id in el.keys():
                index_of_l = i
                break
        
        main_json[section_id]['units'][index_of_l][lesson_id]['steps'] = []
        for index_step, step in enumerate(steps_list):
            print('Current step:', step)
            attempts = c.get_attempts_of_step(step)
            if attempts:
                sub = c.get_submissions_of_step(step)
                answer = c.convert_solution(attempts, sub)
                main_json[section_id]['units'][index_of_l][lesson_id]['steps'].append({'num': '{}-{}-{}'.format(section_id, index_of_l, index_step), 'answer': answer})
                dump_json(main_json, 'dump.json')





