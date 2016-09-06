import re
from nltk.tag.stanford import StanfordNERTagger

# st = StanfordNERTagger('E:\english.all.3class.nodistsim.crf.ser.gz',
# 'E:\stanford-corenlp\stanford-english-corenlp-2016-01-10-models.jar')
# st.tag('Rami Eid is studying at Stony Brook University in NY'.split())


class EntitiesRecognizer:
    entities_with_value = {'yes no': {'yes': 1, 'absolutely': 1, 'not sure': 0.5,
                                      'maybe': 0.5, 'no': 0, 'definitely not': 0},
                           'day_of_week': {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5,
                                           'saturday': 6, 'sunday': 7}}

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
