import subprocess
import json

class LL1Parser:
    def __init__(self, text):
        self.text = text.replace('\n', "\\n")
        
        self.generate_rules(self.text)
        self.result_raw = self.call_js_ll1(self.text)

        j = json.loads(self.result_raw)
        self.first = j['first']
        self.follow = j['follow']
        self.ruleTable = j['ruleTable']

               

    
    def call_js_ll1(self, text):
        return subprocess.check_output('node ll_js_source.js', stderr=subprocess.PIPE,
                                                   stdin=subprocess.PIPE, shell=True).decode()

    def __str__(self):
        return str(self.first)

    def generate_rules(self, text):
        string = 'module.exports = {returnRules: function() {return "' + text + '";}}'
        with open("rules.js", 'w') as f:
            f.write(string)



text = '''E -> T E'
E' -> + T E'
E' -> ''
T -> F T'
T' -> * F T'
T' -> ''
F -> ( E )
F -> i
'''

ll1 = LL1Parser(text)
print(ll1)
