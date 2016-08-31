import botbuilder as bb
import intent_recognizer as ir
import entities_recognizer as er


def hello_respond(session):
    session['path'] = ['']
    print('Hello to you, too!')
    return True


def idk_respond(session):
    # session['path'] = ['']
    del session['path'][-1]
    print('Can you said it clearer? I am just stupid machine')
    return True


def name_question_respond(session):
    if 'user.name' in session:
        return False
    print("What's you name?")
    session['path'].append('gettingPronoun')
    session['attribute_type'] = ['person_name']
    return True


def company_question_respond(session):
    if 'user.company' in session:
        return False
    print("What company do you work for?")
    session['path'].append('gettingPronoun')
    session['attribute_type'] = ['company_name']
    return True


def get_answer_respond(session):
    print("I understand that your " + session['attribute_type'][-1] + " is " + session['variables_intent']['name'])
    session[session['attribute_type'][-1]] = session['variables_intent']['name']
    del session['path'][-1]
    del session['path'][-1]
    del session['path'][-1]
    print(session)
    # session['path'].append('confirmation')
    return True


def confirmation_respond(session):
    print("I understand that your " + session['attribute_type'][-1] + " is " + session['variables_intent']['name']
          + "\nIs that correct?")
    session[session['attribute_type'][-1]] = session['variables_intent']['name']
    session['path'].append('confirmation')
    print(session)
    # session['path'].append('confirmation')
    return True

entities = {'yes no': {'yes':1, 'absolutely':1, 'not sure':0.5, 'maybe':0.5, 'no': 0, 'definitely not': 0}}
name_entities = er.PronounRecognizer()

hello_ir = ir.IntentRecognizer('(hi|hello)+','greeting')
idk_ir = ir.IntentRecognizer('\w','idk')
update_profile_ir = ir.IntentRecognizer('(update|profile)+','ensureProfile')
yes_no_ir = ir.OneEntitiesIntentRecognizer(entities['yes no'], 'respondToYesNoQuestion')
give_name_info_ir = ir.NameEntitiesIntentRecognizer(name_entities, "givePronounce")

bot = bb.BotBuilder()
bot.add_intent_recognizer('', [hello_ir, update_profile_ir, idk_ir])
bot.add_intent_recognizer('gettingPronoun', [give_name_info_ir, idk_ir])
bot.add_intent_recognizer('confirmation', [yes_no_ir, idk_ir])


bot.add_responds('ensureProfile', [name_question_respond, company_question_respond])
bot.add_responds('givePronounce', [get_answer_respond])
bot.add_responds('greeting', [hello_respond])
bot.add_responds('idk', [idk_respond])
while True:
    msg = input("You> ")
    # Commands
    if msg == '/help':
        print("> Supported Commands:")
        print("> /help   - Displays this message.")
        print("> /quit   - Exit the program.")
    elif msg == '/quit':
        exit()
    else:
        bot.reply(msg)