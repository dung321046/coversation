import re


class IntentRecognizer:

    def __init__(self, re_string, intent):
        self.re_string = re_string
        self.intent = intent

    def get_score(self, input_string, session):
        pattern = re.compile(self.re_string)
        m = pattern.match(input_string)
        if m:
            return 1
        return 0
    '''
    def getNumberEntities(self, input_string):
        p = re.compile(r'\d+')
        m = p.match(input_string)
        if m:
            print('Match found: ', m.group())
        else:
            print('No match')
    '''
    def get_variables(self, input_string):
        return {}

class OneEntitiesIntentRecognizer(IntentRecognizer):

    def __init__(self, dict_entities, intent):
        self.dict_entities = dict_entities
        self.variables_intent = {}
        self.intent = intent

    def get_score(self, input_string, session):
        string_entities = ''
        for key, value in self.dict_entities:
            string_entities += '|'+key
        print(string_entities)
        pattern = re.compile("("+string_entities+")")
        m = pattern.match(input_string)
        if m:
            return 1
        return 0

    def get_variables(self, input_string):
        return {}


class NameEntitiesIntentRecognizer(IntentRecognizer):

    def __init__(self, entities_recognizer, intent):
        self.entities_recognizer = entities_recognizer
        self.variables_intent = {}
        self.intent = intent

    def get_score(self, input_string, session):
        # values =  self.entities_recognizer.get_value(input_string)
        # print(values)
        # if len(values) == 1:
        return 1
        #return 0

    def get_variables(self, input_string):
        #values = self.entities_recognizer.get_value(input_string)
        values = [input_string]
        return {'name' : values[0]}
