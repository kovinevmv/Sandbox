import numpy as np    

class Task:
    def __init__(self, id_task=None, response=None):
        self.id_task = -1
        if response:
            self.title = response['category']
            self.task = response['question']
            self.variants = response['incorrect_answers'] + [response['correct_answer']]
            self.correct_answer = response['correct_answer']
            self.correct_answer_id = len(self.variants)
            
            #self.shuffle_variants()
        
        if id_task:
            self.id_task = id_task

    def set_task_id(self, id_task):
        self.id_task = id_task

    def shuffle_variants(self):
        np.random.shuffle(self.variants)
        for i, var in enumerate(self.variants):
            if var == self.correct_answer:
                self.correct_answer_id = i
                break


    def to_resp(self):
        return {"id":self.id_task,
                "title":self.title,
                "text":f"<p>{self.task}</p>",
                "type":"text-test",
                "qstruct": {
                    "variants": [f"<p>{v}</p>" for v in self.variants],
                    "answer": f"{self.correct_answer_id}",
                "isSelfTest": False,
                "file": 'null',
                "fileId":'null'
        }}