from config import config
from faker import Faker
from task import Task

import requests, json, os, random

def generate_tasks():
    path = config.text_tasks_folder

    if os.path.exists(path) and os.stat(path).st_size != 0:
        return

    else:
        url = 'https://opentdb.com/api.php?amount=50&type=multiple&encode=url3986'

        print('Generating tasks: ', end='')
        tasks = []
        for _ in range(20):
            print('.', end='', sep='', flush=True)
            resp = json.loads(requests.get(url).text)
            tasks += resp['results']
        
            with open(path, 'w') as f:
                f.write(json.dumps(tasks))
        print()

def generate_images():
    path = config.images_path

    if os.listdir(path):
        return

    print('Generating images: ', end='')
    
    url = "https://loremflickr.com/320/{}"
    
    for i in range(100):

        print('.', end='', sep='', flush=True)
        try:
            img_size = random.randint(200, 400)
            response = requests.get(url.format(img_size), stream=True, timeout=5)
            c = response.content
        except:
            continue
        with open(f'{path}/{i}.png', 'wb') as f:
                f.write(response.content)
    print()




def upload_images():
    from course_api import CourseApi
    from user import User
        
    u = User(config.cm_login, config.cm_password)
    course_api = CourseApi(u)

    json_path = config.images_json_path
    path = config.images_path
    images = os.listdir(path)

    images_list = []
    for image in images:
        resp = course_api.upload_file(path + '/' + image)
        images_list.append(resp)
        with open(json_path, 'w') as f:
            f.write(json.dumps(images_list))


#generate_images()
#generate_tasks()   
upload_images()