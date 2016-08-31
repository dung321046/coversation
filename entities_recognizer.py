import re


class EntitiesRecognizer:
    entities_with_value = {'yes no': {'yes': 1, 'absolutely': 1, 'not sure': 0.5,
                                      'maybe': 0.5, 'no': 0, 'definitely not': 0}}

    @staticmethod
    def get_value(self, string):
        return
    '''
    def get_value_of_single_entity(self, string, type):
        dict_value = {}
        if type in self.entities_with_value:
            self.entities_with_value
    '''


class PronounRecognizer:
    @staticmethod
    def get_value(string):
        title_search = re.search(r'([A-Z][a-z]*)[\s-]([A-Z][a-z]*)', string, re.IGNORECASE)
        if title_search:
            return title_search.group()
        return ()