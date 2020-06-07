from stepik_api import StepikAPI, dump_json, read_json


class StepikGrabber:
    def __init__(self, course_id, save_temp_json='dump.json'):
        self.stepik_api = StepikAPI(course=course_id)
        self.temp_json_path = save_temp_json
    
    def grab_answers(self):
        sections = self.stepik_api.get_sections_of_course()
        units = self.stepik_api.get_units_by_sections(sections)

        # Indexing titles of sections
        for index, section in enumerate(sections, start=1):
            units[section]['title'] = '{}. {}'.format(index, units[section]['title'])

        self.main_json = units

        for index_section, (section_id, unit_data) in enumerate(units.items(), start=1):
            lessons = self.stepik_api.get_lessons_from_units(unit_data['units'])
            self.main_json[section_id]['units'] = lessons

            steps = self.stepik_api.get_steps_from_lessons(lessons)
            for lesson_id, lesson_info in steps.items():
                index_of_l = self.main_json[section_id]['units'].index(lesson_id)
                lesson_info['title'] = '{}. {}'.format(index_of_l + 1, lesson_info['title'])
                lesson_info.update({'num': index_of_l + 1})
                self.main_json[section_id]['units'][index_of_l] = {lesson_id: lesson_info}
            
            for lesson_id, lesson_data in steps.items():
                steps_list = lesson_data['steps']
                for i, el in enumerate(self.main_json[section_id]['units']):
                    if lesson_id in el.keys():
                        index_of_l = i
                        break
                
                self.main_json[section_id]['units'][index_of_l][lesson_id]['steps'] = []
                for index_step, step in enumerate(steps_list, start=1):
                    print(f'Current step: {step}. Section: {index_section}/{len(units)}')
                    attempts = self.stepik_api.get_attempts_of_step(step)
                    if attempts is not None:
                        sub = self.stepik_api.get_submissions_of_step(step)
                        answer = self.stepik_api.convert_solution(attempts, sub)
                        self.main_json[section_id]['units'][index_of_l][lesson_id]['steps'].append({
                                    'num': '{}-{}-{}'.format(index_section, index_of_l + 1, index_step), 
                                    'answer': answer})
                            
                    dump_json(self.main_json, self.temp_json_path)

    def dump_course(self, json_=None):
        if not json_:
            json_ = self.main_json
        else:
            json_ = read_json(json_)
        self.stepik_api.dump_course(json_)
        print('Course dumped')



