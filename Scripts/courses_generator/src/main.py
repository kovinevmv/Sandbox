from config import config
from user import User
from course_api import CourseApi
from course import Course
from utils import *

import sys
u = User(config.cm_login, config.cm_password)
course_api = CourseApi(u)



def generate_courses():
    courses_count = 1 #random.randint(*config.courses_count())
    for i in range(courses_count):
        course = Course(course_api.create_course())

        course.set_title(get_random_title())
        course.set_short_description(get_random_paragraph())
        image = course_api.upload_file(get_random_image_path())
        course.set_avatar_id(image['id'])

        course_api.update_info(course.get_id(), course.to_info())

        structure = get_random_structure(course.get_id())
        resp = course_api.update_structure(course.get_id(), structure)

        print(resp)

        structure = course_api.get_structure_by_course_id(course.get_id())
        data = structure['topics']
        print('Created structure')
        print('Fill Tasks')

        print(data)
        for theme in data:
            for section in theme['sections']:
                for subsection in section['subSections']:
                    subsection_id = subsection['id']
                    course_api.update_task(course.get_id(), subsection_id, get_random_subsection_full(subsection_id, subsection['type']))



if __name__ == "__main__":
    try:
        arg = sys.argv[1]
        if arg == "gen_courses":
            generate_courses()
        else:
            print('No such option')
    except:
        print('Pass args')