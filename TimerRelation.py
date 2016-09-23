

def getTimerRelation(data):
    for sentence in data['sentences']:
        tokens = sentence['tokens']
        length = len(tokens)
        for i in range(length-1):
            if tokens[i]['word'] == 'between':

class EntityInfo:
    word = ""
    wType = ""

    def __init__(self, word, wtype):
        self.word = word
        self.wType = wtype
