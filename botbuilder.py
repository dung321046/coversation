import intent_recognizer as iz


class BotBuilder:

    def __init__(self):
        self.session = {'path':['']}
        self.dict_intent_recognizer = {}
        self.dict_respond = {}
        self.dict_path = {}
        self.count = 0

    def add_responds(self, intent, responds):
        self.dict_respond[intent] = list(responds)
        return

    def set_count(self, num):
        self.count = num
        return

    def add_intent_recognizer(self, path, irs):
        self.dict_intent_recognizer[path] = list(irs)
        return

    def get_respond(self, responds):
        for respond in responds:
            if respond(self.session):
                return
        return

    def reply(self, string_input):
        cur_context = self.session['path'][-1]
        if cur_context in self.dict_intent_recognizer:
            list_ir = self.dict_intent_recognizer[cur_context]
            for ir in list_ir:
                if ir.get_score(string_input) > 0.5:
                    self.session['variables_intent'] = ir.get_variables(string_input)
                    self.session['path'].append(ir.intent)
                    self.get_respond(self.dict_respond[ir.intent])
                    return
        else:
            print('Can not find intent recognizers')
        return