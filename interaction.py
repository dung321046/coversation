import botbuilder as bb
import intent_recognizer as ir
import entities_recognizer as er
import respond as rp
from nltk.tag.stanford import StanfordNERTagger

#st = StanfordNERTagger('E:\english.all.3class.nodistsim.crf.ser.gz', 'E:\stanford-corenlp\stanford-english-corenlp-2016-01-10-models.jar')
#st.tag('Rami Eid is studying at Stony Brook University in NY'.split())


entities = {'yes no': {'yes': 1, 'absolutely': 1, 'not sure': 0.5, 'maybe': 0.5, 'no': 0, 'definitely not': 0}}
name_entities = er.PronounRecognizer()

hello_ir = ir.IntentRecognizer('(hi|hello)+', 'greeting')
idk_ir = ir.IntentRecognizer('\w', 'idk')
update_profile_ir = ir.IntentRecognizer('(update|profile)+', 'ensureProfile')
yes_no_ir = ir.OneEntitiesIntentRecognizer(entities['yes no'], 'respondToYesNoQuestion')
give_name_info_ir = ir.NameEntitiesIntentRecognizer(name_entities, "givePronounce")
update_calendar = ir.IntentRecognizer('(calendar|schedule)+', 'updateCalendar')
setup_meeting = ir.IntentRecognizer('\w', 'setup_meeting')
bot = bb.BotBuilder()
bot.add_intent_recognizer('', [hello_ir, update_profile_ir, update_calendar, setup_meeting])
bot.add_intent_recognizer('gettingPronoun', [give_name_info_ir, idk_ir])
bot.add_intent_recognizer('confirmation', [yes_no_ir, idk_ir])

hello_respond = rp.Responder("Hello to you, too", "Send hello back", False, True)
idk_respond = rp.Responder("Can you said it clearer? I am just stupid machine", "idk", False, True)
get_answer_respond = rp.GetAnswerRespond()
name_question_respond = rp.QuestionRespond("What is your name?", "Ask name", "person_name")
company_question_respond = rp.QuestionRespond("What company do you work for?", "Ask company", "company_name")

bot.add_responds('ensureProfile', [name_question_respond, company_question_respond])
bot.add_responds('givePronounce', [get_answer_respond])
bot.add_responds('greeting', [hello_respond])
bot.add_responds('idk', [idk_respond])

bot.print_dialog([''])
while True:
    msg = input("You> ")
    # Commands
    if msg == '/help':
        print("> Supported Commands:")
        print("> /help   - Displays this message.")
        print("> /show   - Displays current state of chat bot.")
        print("> /quit   - Exit the program.")
    elif msg == '/show':
        for key, value in bot.session.items():
            print("-----", key)
            print("+++++", value)
    elif msg == '/quit':
        exit()
    else:
        bot.reply(msg)
