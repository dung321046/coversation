import bot_center as bc
import nltk
import ner
from nltk.tag.stanford import StanfordNERTagger
from pycorenlp import StanfordCoreNLP
import json
import pprint
from json import dumps
import time
import pyspell
def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            print(chunk)
            if type(chunk) is nltk.tree.Tree:
                print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()), type(chunk))

            # if hasattr(chunk, 'node'):
            #    print(chunk.node, ' '.join(c[0] for c in chunk.leaves()))


def loadTimeEntities(jsonfile):
    with open(jsonfile) as datafile:
        data = json.load(datafile)
    return data

nlp = StanfordCoreNLP('http://localhost:9000')
text = 'It happens next Friday evening'
text2 = 'Can I meet you on first of July'
text3 = 'Can I meet you at noon next Sunday'
text4 = 'I will go fishing first week of year'
text5 = 'I will go fishing next summer on July'
text6 = 'I will meet you in the next 3 hours'
text7 = 'I will meet you today at 5 p.m'
text8 = 'I will meet you in next morning'
text9 = 'I am free at tomorrow 2pm'
text10 = 'I will meet you on the first of next month'
text11 = 'I will meet you on the independence day'
text12 = 'I can meet you tomorrow 7 or 9 am'
text13 = 'I can meet you tomorrow from 7 a.m to 9 am'
text14 = 'I will be able on tomorrow or next Sunday.'
text15 = 'We can meet tomorrow or Friday morning from 9 am to 12 am.'
text16 = '23 will be the best, but this weekend also be fine'
text17 = 'from 2 to 4 in this afternoon can be managed; however, moving it to tomorrow will be the best option'
text18 = 'I will available from 2 to 5 on 23rd'
text19 = 'I will available from 2 to 5 in this month'
text20 = 'From 21st to the end of this month, I am going to be available between 2 am and 5 pm'
text21 = 'Need to meet at the end of next month'
text22 = 'I will meet at this time tomorrow'
text23 = 'I will be able on tomorrow or 3 pm Sunday.'
text24 = 'from 2pm to 3pm'
output = nlp.annotate(text24, properties={
    "annotators": "ner",
    "outputFormat": "json"
 })
print('T14:00-T15:00'.split('-'))
#output = json.dump(output)
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(output)
data = output
time_dict = {}
time_set = set()
for sentence in data['sentences']:
    for token in sentence['tokens']:
        if 'timex' in token:
            # print(token)
            timex = token['timex']
            if timex['type'] == 'DATE':
                time_dict['DATE'] = token['normalizedNER']
            elif timex['type'] == 'TIME':
                time_dict['TIME'] = token['normalizedNER']
        if 'normalizedNER' in token:
            if token['normalizedNER'] not in time_set:
                time_set.add(token['normalizedNER'])
                print(token['normalizedNER'], ' - ', token['word'])
print(time_dict)

#tagger = ner.HttpNER(host='localhost', port=8080)
#tagger.get_entities("University of California is located in California, United States")
#tagger.json_entities("Alice went to the Museum of Natural History.")
#extract_entities("Could I meet you at Hilton Hotel at 9:00 p.m on June")
"""
bot_center = bc.ChatBotCenter()
while True:
    msg = input("Admin> ")
    words = msg.split()
    # Commands
    if words[0] == '/help':
        print("> Supported Commands:")
        print("> /help   - Displays this message.")
        print("> /add user_id [user_role] - Add a user to a new chat bot")
        print("> /msg user_id message - User send message")
        print("> /dbm interview_id user_role message -\
            User send message and bot have to load from db to produce respond")
        print("> /show user_id  - Displays current state of chat bot which connects to user_id.")
        print("> /show_dialog  - Displays chat bot dialog")
        print("> /quit   - Exit the program.")
    elif words[0] == '/show':
        user_id = msg.split()[1]
        if user_id not in bot_center.bots:
            print('User ' + user_id + r" isn't connecting to any bot")
            continue
        for key, value in bot_center.bots[user_id].session.items():
            print("---", key)
            print("+++", value)
    elif words[0] == '/add':
        if len(words) == 1:
            print("Need user_id")
            continue
        user_id = words[1]
        if len(words) > 2:
            user_role = words[2]
            bot_center.add_user(user_id, user_role)
        else:
            bot_center.add_user(user_id)
    elif words[0] == '/msg':
        user_id = words[1]
        if user_id not in bot_center.bots:
            print('User ' + user_id + r" isn't connecting to any bot")
            continue
        bot_center.bots[user_id].reply(" ".join(words[2:]))
    elif words[0] == '/dbm':
        interview_id = words[1]
        user_role = words[2]
        bot_center.send_message(interview_id, user_role, " ".join(words[3:]))
    elif words[0] == '/show_dialog':
        if len(bot_center.bots) == 0:
            print(r"Don't have any bot now.")
            continue
        bot_center.bots[bot_center.user_id[0]].print_dialog([''])
    elif words[0] == '/quit':
        exit()
    else:
        print("Error message. Type /help for more information")
"""