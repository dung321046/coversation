import botbuilder as bb
import intent_recognizer as ir
import entities_recognizer as er
import respond as rp
import sys, os
import mysql.connector


class ChatBotCenter:

    def __init__(self):
        entities = {'yes no': {'yes': 1, 'absolutely': 1, 'not sure': 0.5, 'maybe': 0.5, 'no': 0, 'definitely not': 0}}
        name_entities = er.PronounRecognizer()

        hello_ir = ir.IntentRecognizer('(hi|hello)+', 'greeting')
        idk_ir = ir.IntentRecognizer('\w', 'idk')
        update_profile_ir = ir.IntentRecognizer('(update|profile)+', 'ensureProfile')
        yes_no_ir = ir.OneEntitiesIntentRecognizer(entities['yes no'], 'respondToYesNoQuestion')
        give_name_info_ir = ir.NameEntitiesIntentRecognizer(name_entities, "givePronounce")
        update_calendar = ir.IntentRecognizer('(calendar|schedule)+', 'updateCalendar')
        bot_intent = ir.BotIntentRecognizer()
        self.intent_recognizers = {'hello_ir': hello_ir, 'idk_ir': idk_ir, 'update_profile_ir': update_profile_ir,
                                   'yes_no_ir': yes_no_ir, 'give_name_info_ir': give_name_info_ir,
                                   'update_calendar': update_calendar, 'bot_intent': bot_intent}
        hello_respond = rp.Responder("Hello to you, too", "Send hello back", False, True)
        idk_respond = rp.Responder("Can you said it clearer? I am just stupid machine", "idk", False, True)
        get_answer_respond = rp.GetAnswerRespond()
        name_question_respond = rp.QuestionRespond("What is your name?", "Ask name", "person_name")
        company_question_respond = rp.QuestionRespond("What company do you work for?", "Ask company", "company_name")
        self.responds = {'hello_respond': hello_respond, 'idk_respond': idk_respond,
                         'get_answer_respond': get_answer_respond, 'name_question_respond': name_question_respond,
                         'company_question_respond': company_question_respond}

        self.bots = {}
        self.user_id = []
        # self.cnx = mysql.connector.connect(host='localhost',database='mysql',user='root',password='')

    def get_intent(self, intent_name):
        return self.intent_recognizers[intent_name]

    def get_respond(self, respond_name):
        return self.responds[respond_name]

    def add_user(self, user_id, role='client'):
        if role == 'client':
            bot = bb.BotBuilder(user_id)
            bot.add_intent_recognizer('', [self.get_intent('hello_ir'), self.get_intent('update_profile_ir'),
                                           self.get_intent('update_calendar'), self.get_intent('bot_intent')])
            bot.add_intent_recognizer('gettingPronoun', [self.get_intent('give_name_info_ir'),
                                                         self.get_intent('idk_ir')])
            bot.add_intent_recognizer('confirmation', [self.get_intent('yes_no_ir'), self.get_intent('idk_ir')])

            bot.add_responds('ensureProfile', [self.get_respond('name_question_respond'),
                                               self.get_respond('company_question_respond')])
            bot.add_responds('givePronounce', [self.get_respond('get_answer_respond')])
            bot.add_responds('greeting', [self.get_respond('hello_respond')])
            bot.add_responds('idk', [self.get_respond('idk_respond')])
            self.bots[user_id] = bot
            self.user_id.append(user_id)
        else:
            print(r"We don't have any chat bot for " + role)

    def send_message(self, interview_id, role, msg):
        '''
        :param user_id:
        :param msg:
        :return:
        '''
        return
