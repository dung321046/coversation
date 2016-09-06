class Responder:

    def __init__(self, respond_sentence, info, is_continue, is_go_back, new_intent = ''):
        self.respond_sentence = respond_sentence
        self.info = info
        self.is_continue = is_continue
        self.is_go_back = is_go_back
        self.new_intent = new_intent
        return

    def get_respond(self, session):
        """"
            if session satisfies the condition
                update session and give appropriate respond
                return true
            else
                return false
        """
        if self.is_go_back:
            if len(session['path']) > 1:
                del session['path'][-1]
        if self.is_continue:
            session['path'].append(self.new_intent)
        print(self.respond_sentence)
        return True

    def get_new_path(self, path):
        """
            Give new path after this respond is triggered
        """
        if self.is_go_back:
            if len(path) > 1:
                del path[-1]
            return path
        if self.is_continue:
            path.append(self.new_intent)
        return path


class QuestionRespond(Responder):

    def __init__(self, respond_sentence, info, attribute_name):
        self.respond_sentence = respond_sentence
        self.info = info
        self.attribute_name = attribute_name
        self.is_continue = True
        self.is_go_back = False
        self.new_intent = 'gettingPronoun'
        return

    def get_respond(self, session):
        if self.attribute_name in session:
            return False
        print(self.respond_sentence)
        session['path'].append(self.new_intent)
        session['attribute_type'] = [self.attribute_name]
        return True

    def is_continue(self):
        return True


class GetAnswerRespond(Responder):

    def __init__(self):
        self.is_continue = False
        self.is_go_back = False
        self.info = 'Rephrase what it understand and wait to get an correction or continue flow'
        return

    def get_respond(self, session):
        print("I understand that your " + session['attribute_type'][-1] + " is " + session['variables_intent']['name'])
        session[session['attribute_type'][-1]] = session['variables_intent']['name']
        del session['path'][-1]
        del session['path'][-1]
        del session['path'][-1]
        # session['path'].append('confirmation')
        return True


class ConfirmationRespond(Responder):

    def __init__(self):
        self.is_continue = True
        self.is_go_back = False
        self.info = 'Rephrase what it understand and wait for a confirmation'
        return

    def get_respond(self, session):
        print("I understand that your " + session['attribute_type'][-1] + " is " + session['variables_intent']['name']
              + "\nIs that correct?")
        session[session['attribute_type'][-1]] = session['variables_intent']['name']
        session['path'].append('confirmation')
        print(session)
        # session['path'].append('confirmation')
        return True

