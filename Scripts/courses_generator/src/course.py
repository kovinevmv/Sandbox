import random

class Course:
    def __init__(self, response=None, id=None):
        self.avatar_id = random.randint(60, 100)
        if response:
            self._parse_resp(response)
        else:
            self.course_id = course_id
            self.fill_course_by_id(self.id)

    def get_id(self):
        return self.course_id

    def _parse_resp(self, response):
        self.course_id = response["id"]
        self.title = response["contentObject"]["title"]
        self.short_description = response["contentObject"]["shortDescription"]

    def set_avatar_id(self, avatar_id):
        self.avatar_id = avatar_id

    def set_title(self, title):
        self.title = title

    def set_short_description(self, info):
        self.short_description = info
    
    def fill_course_from_server_by_id(self, course_id):
        from course_api import CourseApi

        response = CourseApi().get_data_by_course_id(course_id)
        self.parse_resp(response)

    def to_info(self):
        return {"title" : self.title ,
                "shortInfo" : f"<p>{self.short_description}</p>",
                "avatar":  self.avatar_id}


    def __str__(self):
        return f"Course:  {self.course_id}:{self.title}"