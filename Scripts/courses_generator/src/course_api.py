import requests, json, os
from course import Course

class CourseApi:
    def __init__(self, user=None, session=None):
        if user:
            self.session = user.get_session()
        elif session:
            self.session = session
        else:
            self.session = requests.Session()
        
    def create_course(self):
        creation_url = 'http://local.gazprom-classes.etu.ru:70/api/education/courses'
        resp = self.session.post(creation_url)
        return json.loads(resp.text)

    def get_data_by_course_id(self, course_id):
        url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{course_id}/content?all=true'
        return json.loads(self.session.get(url))

    def update_info(self, course_id, data):
        url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{course_id}'
        resp = self.session.put(url, data=json.dumps(data), headers={'Content-Type': 'application/json;charset=UTF-8'})
        return json.loads(resp.text)

    def upload_file(self, path):
        url = 'http://local.gazprom-classes.etu.ru:70/api/files/upload'

        files = {'file': (os.path.split(path)[1], open(path, 'rb'), 'image/png')}
        r = self.session.post(url, files=files)
        data = json.loads(r.text)[0]
        return {'id': data['id'], 'url': 'http://local.gazprom-classes.etu.ru:70/api/files/' + data['physicalName']}

    def delete_course_by_id(self, course_id):
        url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{course_id}'
        return self.session.delete(url)

    def delete_all_courses(self):
        for i in range(1, 200):
            print(self.delete_course_by_id(i))

    def update_structure(self, course_id, data):
        url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{course_id}/content'
             
        resp = self.session.put(url, data=json.dumps(data), headers={'Content-Type': 'application/json;charset=UTF-8'})
        return resp

    def get_structure_by_course_id(self, course_id):
        url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{course_id}/content?all=true'
        resp = self.session.get(url)
        return json.loads(resp.text)

    def update_task(self, course_id, task_id, data):
        url = f'http://local.gazprom-classes.etu.ru:70/api/education/courses/{course_id}/content/subsections/{task_id}'
        resp = self.session.put(url, data=json.dumps(data), headers={'Content-Type': 'application/json;charset=UTF-8'})
        return resp
       
