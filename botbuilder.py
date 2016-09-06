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
            if respond.get_respond(self.session):
                return
        return

    def reply(self, string_input):
        cur_context = self.session['path'][-1]
        if cur_context in self.dict_intent_recognizer:
            list_ir = self.dict_intent_recognizer[cur_context]
            for ir in list_ir:
                if ir.get_score(string_input, self.session) > 0.5:
                    self.session['variables_intent'] = ir.get_variables(string_input)
                    if (not ir.intent in self.dict_respond):
                        print('Can not find respond according to '+ ir.intent)
                        continue
                    self.session['path'].append(ir.intent)
                    self.get_respond(self.dict_respond[ir.intent])
                    return
        else:
            print('Can not find intent recognizers')
        return

    def print_respond(self, path, tab_string):
        if not path[-1] in self.dict_respond:
            print(tab_string + '   Undefined')
            return
        for respond in self.dict_respond[path[-1]]:
            if respond.is_go_back:
                print(tab_string + '   <-' + respond.info)
                continue
            print(tab_string + '   ' + respond.info)
            if respond.is_continue:
                new_path = respond.get_new_path(path)
                self.print_dialog(new_path, tab_string + '      ')
        return

    def print_dialog(self, path, tab_string = ''):
        for intent_recognizer in self.dict_intent_recognizer[path[-1]]:
            path.append(intent_recognizer.intent)
            print(tab_string +"<>" + path[-1] + "<>")
            self.print_respond(path, tab_string+'   ')
            del path[-1]
        return


