import re
import requests
import json

stepic_api_url = 'https://stepik.org/api'

my_stepic_id = '19621617'
client_id = '4zjhKkRt1atYA23lPsxULmZU0qKb6jPDdMpVInei'
client_secret = 'DamSVzsMdjK8JDCnbgR23gxbmRKNuQKeecvrHOWGFHc3kNJXBieBbzcbgwi4mAPM4lDgPgKukVjQAl1dMMODZutbsYDYwQW9HwpXoyazsl5jDAfAUrMDXObTqbqIBTWG'

class StepikAPI:
    def __init__(self, course, user_id=my_stepic_id):
        self.course_id, self.course_url = self._parse_course_id(course)
        self.user_id = user_id
        self.authrorize()

    def authrorize(self):
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        resp = requests.post('https://stepik.org/oauth2/token/',
                     data={'grant_type': 'client_credentials'},
                     auth=auth)
        self.token = json.loads(resp.text)["access_token"]
        self.headers = {'Authorization': 'Bearer ' + self.token}

        print(self.headers)

    def _api_call_by_name(self, name, data):
        api_url = f'{stepic_api_url}/{name}{data}'
        return json.loads(requests.get(api_url, headers=self.headers).text)

    def get_sections_of_course(self):
        return self._api_call_by_name('courses/', self.course_id)['courses'][0]['sections']
    
    def get_units_by_sections(self, sections):
        response = self._api_call_by_name('sections', '?ids[]=' + ('&ids[]='.join([str(section) for section in sections])))
        units = {}
        for section in response['sections']:
            units[section['id']] = {'title': section['title'], 
                                    'units': section['units']}

        return units
    
    def get_lessons_from_units(self, units):
        response = self._api_call_by_name('units', '?ids[]=' + ('&ids[]='.join([str(unit) for unit in units])))
        lessons = {}
        for unit in response['units']:
            lessons[unit['id']] = unit['lesson']

        return units
    
    def get_steps_from_lessons(self, lessons):
        response = self._api_call_by_name('lessons', '?ids[]=' + ('&ids[]='.join([str(lesson) for lesson in lessons])))
        steps = {}
        for lesson in response['lessons']:
            steps[lesson['id']] = {'title': lesson['title'], 
                                   'steps': lesson['steps']}

        return steps

    def get_attempts_of_step(self, step, user_id=None):
        pass
    
    def get_submission_of_step(self, step, user_id=None):
        pass

    def convert_solution(self, variants, solution):
        pass
    
    def _parse_course_id(self, course):
        url = course
        regex = re.compile('[0-9]+');
        id = re.findall(regex, course)[0]

        # if passed only id, generate url
        if id == course:
            url = 'https://stepik.org/course/{}/syllabus'.format(id)

        # else return input course is url
        return id, url


c = StepikAPI(course='53334')
sections = c.get_sections_of_course()
print('Sections:', sections)
units = c.get_units_by_sections(sections)
print('Units:', units)
lessons = c.get_lessons_from_units(units[sections[1]]['units'])
print('Lessons:', lessons)
steps = c.get_steps_from_lessons(lessons)
print(steps)