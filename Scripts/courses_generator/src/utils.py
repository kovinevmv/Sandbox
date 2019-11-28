from config import config
from faker import Faker
from task import Task

import random, json, os


def get_random_title():
    path = config.course_titles
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data[random.randint(0, len(data) - 1)]

def get_random_sentence(words=None):
    fake = Faker()
    return fake.sentence(ext_word_list=words)


def get_random_paragraph(words=None):
    count_sentences = random.randint(8, 15)    
    return ' '.join((get_random_sentence() for _ in range(count_sentences)))


def get_random_task():
    path = config.text_tasks_folder
    with open(path, 'r') as f:
        data = json.loads(f.read())
    
    task_raw = data[random.randint(0, len(data) - 1)]
    task = Task(response=task_raw)
    return task

def get_random_image():
    path = config.images_path
    images = os.listdir(path)

    return f"{path}/{images[random.randint(0, len(images) - 1)]}"


def get_random_subsection_full(index, type_):
    if type_ == "text-info":
        return {"text": get_random_text_form(), "id": index}
    elif type_ == 'text-test':
        t = get_random_task()
        t.set_task_id(index)
        return t.to_resp()



def get_random_subsection_text(index):
    return {"isAdded": True,
            "position": index,
            "title": f"Subsection {index}. {get_random_sentence()}",
            "type": "text-info",
            "isSelfTest": True}

def get_random_subsection_task_text(index):
    return {"isAdded": True,
            "position": index,
            "title": f"Subsection-task {index}. {get_random_sentence()}",
            "type": "text-test",
            "isSelfTest": True}
    
def get_random_subsection(index):
    type_task = random.randint(0, 1)

    if type_task == 0:
        return get_random_subsection_text(index)
    elif type_task == 1:
        return get_random_subsection_task_text(index)


def get_random_section(index):
    subsection_count = random.randint(*config.subsection_count)
    subsections = [get_random_subsection(i) for i in range(subsection_count)]

    return {"isAdded": True,
            "position": index,
            "title": f"Section {index}. {get_random_sentence()}",
            "subSections": subsections}

def get_random_structure(course_id):
    data = []
    theme_count = random.randint(*config.theme_count)
    isAdded = True

    for i in range(1, theme_count):
        theme_title = f'Theme {i}. {get_random_sentence()}'
        theme_position = i
    
        sections_count = random.randint(*config.section_count)
        sections = []
        for j in range(1, sections_count):
            sections.append(get_random_section(j))
        

        data.append({"isAdded": isAdded,
                     "position": theme_position, 
                     "title": theme_title, 
                     "sections": sections})
    return data    


def get_random_text_form():
    content_elements = random.randint(1, 10)
    
    from course_api import CourseApi
    from user import User
        
    u = User(config.cm_login, config.cm_password)
    course_api = CourseApi(u)

    text = ''
    for i in range(content_elements):
        if random.choice([True, False]):
            image = course_api.upload_file(get_random_image())
            image_url = image['url']

            text += f'<figure class=\"image image-style-align-center\"><img src=\"{image_url}\"><figcaption>{get_random_sentence()}</figcaption></figure><p>&nbsp;</p>'

        else:
            text += f'<p>{get_random_paragraph()}</p><p>&nbsp;</p>'
    return text



