from stepik_grabber import StepikGrabber

course_id = '3693'
grabber = StepikGrabber(course_id)
grabber.grab_answers()
grabber.dump_course()




