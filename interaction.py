import bot_center as bc
from nltk.tag.stanford import StanfordNERTagger

# st = StanfordNERTagger('E:\english.all.3class.nodistsim.crf.ser.gz',
# 'E:\stanford-corenlp\stanford-ner.jar')
# st.tag('Rami Eid is studying at Stony Brook University in NY'.split())

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
        print("> /dbm interview_id user_role message - User send message and bot have to load from db to produce respond")
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
        if (len(bot_center.bots) == 0):
            print(r"Don't have any bot now.")
            continue
        bot_center.bots[bot_center.user_id[0]].print_dialog([''])
    elif words[0] == '/quit':
        exit()
    else:
        print("Error message. Type /help for more information")
