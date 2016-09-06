import bot_center as bc
bot_center = bc.ChatBotCenter()
while True:
    msg = input("Admin> ")
    words = msg.split()
    # Commands
    if words[0] == '/help':
        print("> Supported Commands:")
        print("> /help   - Displays this message.")
        print("> /add user_id [user_role] - Add a user to a new chat bot")
        print("> /msg user_id message - Send a bot message to user")
        print("> /show user_id  - Displays current state of chat bot which connects to user_id.")
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
    elif words[0] == '/quit':
        exit()
    else:
        print("Error message. Type /help for more information")
