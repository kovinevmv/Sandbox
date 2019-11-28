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
    
    url = "https://placekitten.com/{}/{}/"
    
    for i in range(40):

        print('.', end='', sep='', flush=True)
        try:
            img = random.randint(200, 400)
            response = requests.get(url.format(img, img), stream=True, timeout=5)
            c = response.content
        except:
            continue
        with open(f'{path}/{i}.png', 'wb') as f:
            for block in response.iter_content(1024):
                if not block:
                    break
                f.write(block)
    print()

generate_images()
generate_tasks()   
