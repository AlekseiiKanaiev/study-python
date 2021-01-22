


from flask import Flask, request
import telebot
import json
import sqlite3
# from sqlite3 import Error
from config import Configurations

bot_name = Configurations.bot_name
db_path = Configurations.db_path
secret = Configurations.secret
token = Configurations.bot_id
url = 'https://alexeykanaev.pythonanywhere.com/' + secret
bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    # print(update, flush=True)
    return "OK", 200

commands = [
    '/start',
    '/commands',
    '/help',
    '/show',
    '/change',
    '/showmyrep',
    '/showmytotalrep',
    '/showmypairings',
    '/showtoppairings'
    ]

# def create_table():
#     con = sqlite3.connect(db_path)
#     cur = con.cursor()
#     cur.execute('CREATE TABLE IF NOT EXISTS reputation (members TEXT, data TEXT)')
#     con.commit()
#     con.close()
#     # print('DB created')
# create_table()

def get_members_from_DB(con):
    cur = con.cursor()
    cur.execute("SELECT members FROM reputation")
    results = cur.fetchall()
    # print(results)
    return results

def add_new_member_to_DB(con, name, data):
    cur = con.cursor()
    cur.execute('INSERT INTO reputation VALUES (?, ?)', (name, json.dumps(data),))
    con.commit()

def update_table(con, member, data):
    cur = con.cursor()
    cur.execute('UPDATE reputation SET data = ? WHERE members = ?', (json.dumps(data), member,))
    con.commit()

def get_reputation_for_member(con, member):
    cur = con.cursor()
    cur.execute("SELECT * FROM reputation WHERE members = ?", (member,))
    results = cur.fetchall()
    return results

def no_register(message):
    msg = 'You are not register yet!\nPlease, enter command:\n/start'
    bot.send_message(message.chat.id, msg)

def wrong_command(message):
    msg = 'Wrong command!\nPlease enter:\n/change <user> <sign><number>(or it will be 1 as by default)'
    bot.send_message(message.chat.id, msg)

def check_sign_position(message, sign):
    msgArr = [w for w in message.text.split(' ') if w]
    signW = [i for i in msgArr if i.startswith(sign)]
    nameW = [i for i in msgArr if i.startswith('@')]
    if (signW and nameW):
        return msgArr.index(signW[0]) - msgArr.index(nameW[0]) == 1
    else:
        return False

def check_number_position(message, number, sign):
    msgArr = [w for w in message.text.split(' ') if w]
    signW = [i for i in msgArr if i.startswith(sign)]
    numW = [i for i in msgArr if i.startswith(number)]
    if signW:
        if not numW:
            if number in signW[0]:
                return True
        else:
            return msgArr.index(numW[0]) - msgArr.index(signW[0]) == 1
    return False

def change_reputation_command(message, users, messanger, members, con, m_type):
    filterNumber = ''.join(c for c in message.text if c.isdigit())
    # print(filterNumber)
    number = 1
    if filterNumber:
        number = int(filterNumber)
        if not check_number_position(message, filterNumber, '+') and not check_number_position(message, filterNumber, '-'):
            return
    data = json.loads(get_reputation_for_member(con, messanger)[0][1])
    # print(number)
    if check_sign_position(message, '+'):
        for user in users:
            user = user[1:]
            if (user in data.keys()):
                data[user] += number
                update_table(con, messanger, data)
                msg = '@{} increased reputation with @{}: {} 😀 \n'.format(messanger, user, data[user])
                bot.send_message(message.chat.id, msg)
                # bot.send_message(message.chat.id, '@{}: {}'.format(user, data[user]))
            else:
                bot.send_message(message.chat.id, 'No such member "@{}", that join this reputation raiting in the chat'.format(user))
    elif check_sign_position(message, '-'):
        for user in users:
            user = user[1:]
            if (user in data.keys()):
                data[user] -= number
                update_table(con, messanger, data)
                msg = '@{} decrease reputation with @{}: {}'.format(messanger, user, data[user])
                bot.send_message(message.chat.id, msg)
                # bot.send_message(message.chat.id, '@{}: {}'.format(user, data[user]))
            else:
                bot.send_message(message.chat.id, 'No such member "@{}", that join this reputation raiting in the chat'.format(user))
    elif m_type == 'command':
        wrong_command(message)

def show_reputation_command(con, message, messanger):
    data = json.loads(get_reputation_for_member(con, messanger)[0][1])
    msg = 'Reputation raiting of @{}:\n'.format(messanger)
    users = [item[1:] for item in message.text.split(' ') if item.startswith('@')]
    # print(users)
    if users:
        for user in users:
            msg += '{}: {}\n'.format(user, data[user])
    else:
        for key,val in data.items():
            msg += '{}: {} \n'.format(key, val)
    if not msg:
        msg = '@{}, you are alone in this raiting yet('.format(messanger)
    bot.send_message(message.chat.id, msg)

def show_my_reputation(con, message, messanger):
    users = [item[1:] for item in message.text.split(' ') if item.startswith('@')]
    # print(users)
    if users:
        members = [item[0] for item in get_members_from_DB(con) if item[0] in users]
    else:
        members = [item[0] for item in get_members_from_DB(con) if item[0] != messanger]
        if '/showmytotalrep' in message.text:
            num = 0
            for m in members:
                m_data = json.loads(get_reputation_for_member(con, m)[0][1])
                num += m_data[messanger]
            bot.send_message(message.chat.id, '@{}, your total reputation is: {}'.format(messanger, num))
            return
    msg = '@{}, your reputation from:\n'.format(messanger)
    for m in members:
        m_data = json.loads(get_reputation_for_member(con, m)[0][1])
        if m_data:
            msg += '{}: {}\n'.format(m, m_data[messanger])
    bot.send_message(message.chat.id, msg)

def show_my_pairings_command(con, message, messanger):
    data = json.loads(get_reputation_for_member(con, messanger)[0][1])
    members = [item[0] for item in get_members_from_DB(con) if item[0] != messanger]
    msg = '@{}, your pairings list: \n'.format(messanger)
    pairings = {}
    for m in members:
        m_data = json.loads(get_reputation_for_member(con, m)[0][1])
        if m_data and data[m] + m_data[messanger] > 0:
            pairings[m] = data[m] + m_data[messanger]
    if pairings:
        for (key, value), index in zip(sorted(pairings.items(), key=lambda item: item[1], reverse=True), range(len(pairings.keys()))):
            # print("{}: {}".format(key, value))
            msg += "{}. {}: {}\n".format(index+1, key, value)
    else:
        msg += 'you have no pairings :('
    bot.send_message(message.chat.id, msg)

def show_top_pairings(con, message, messanger):
    top_pairings = {}
    members = [item[0] for item in get_members_from_DB(con) if item[0]]
    for member in members:
        top_pairings[member] = {}
        member_data = json.loads(get_reputation_for_member(con, member)[0][1])
        if member_data:
            for m, val in member_data.items():
                if m not in top_pairings:
                    m_data = json.loads(get_reputation_for_member(con, m)[0][1])
                    # all_pairings[member][m] = val + m_data[member]
                    top_pairings['{} / {}'.format(member, m)] = val + m_data[member]

    # print(sorted({k:v for k,v in top_pairings.items() if k not in members}.items(), key=lambda item: item[1], reverse=True)[0:3])
    msg = 'Top pairings: \n'
    sorted_top = sorted({k:v for k,v in top_pairings.items() if k not in members and v and v > 0}.items(), key=lambda item: item[1], reverse=True)[0:5]
    if sorted_top:
        for item, index in zip(sorted_top, range(5)):
            msg += '{}. {}: {}\n'.format(index+1, item[0], item[1])
    else:
        msg += 'Currently no pairings here :( \nIncrease someone’s reputation to create a pairing.'
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=[c[1:] for c in commands])
def start_message(message):
    print(message.text)
    con = sqlite3.connect(db_path)
    messanger = '{}_{}'.format(message.from_user.first_name, message.from_user.last_name) if message.from_user.username == None else '{}'.format(message.from_user.username)
    members = [item[0] for item in get_members_from_DB(con)]
    if message.text == '/start' or message.text == '/start@{}'.format(bot_name):
        # if members.get(messanger):
        if messanger in members:
            bot.send_message(message.chat.id, 'You already joined this reputation raiting')
            show_reputation_command(con, message, messanger)
        else:
            bot.send_message(message.chat.id, 'Hello, you joined reputation raiting bot.\nThis bot is showing your reputation raiting with others members in the chat')
            data = {}
            for item in members:
                print(item)
                data[item] = 0
                itemData = json.loads(get_reputation_for_member(con, item)[0][1])
                itemData[messanger] = 0
                print(itemData)
                update_table(con, item, itemData)
            add_new_member_to_DB(con, messanger, data)
    elif message.text == '/commands' or message.text == '/commands@{}'.format(bot_name):
        if messanger in members:
            msg = 'List of all commands:\n'
            for item in commands:
                msg += '{}\n'.format(item)
            bot.send_message(message.chat.id, msg)
        else:
            no_register(message)
    elif message.text == '/help' or message.text == '/help@{}'.format(bot_name):
        description = 'With this bot you can change reputation status with everyone who joined ti this raiting (when typed command /start). \n You can type /change <user_name> <sign>(<number>) to change reputation.\n '
        bot.send_message(message.chat.id, description)
    elif '/showmyrep' in message.text or '/showmytotalrep' in message.text:
        if messanger in members:
            show_my_reputation(con, message, messanger)
        else:
            no_register(message)
    elif '/showmypairings' in message.text:
        if messanger in members:
            show_my_pairings_command(con, message, messanger)
        else:
            no_register(message)
    elif '/showtoppairings' in message.text:
        if messanger in members:
            show_top_pairings(con, message, messanger)
        else:
            no_register(message)
    elif '/show' in message.text:
        if messanger in members:
            show_reputation_command(con, message, messanger)
        else:
            no_register(message)
    elif '/change' in message.text:
        if messanger in members:
            users = [item for item in message.text.split(' ') if item.startswith('@')]
            if users:
                change_reputation_command(message, users, messanger, members, con, 'command')
            else:
                wrong_command(message)
        else:
            no_register(message)
    con.close()

@bot.message_handler(content_types=['text'])
def send_text(message):
    con = sqlite3.connect(db_path)
    members = [item[0] for item in get_members_from_DB(con)]
    messanger = '{}_{}'.format(message.from_user.first_name, message.from_user.last_name) if message.from_user.username == None else '{}'.format(message.from_user.username)

    users = [item for item in message.text.split(' ') if item.startswith('@')]
    if users and ('+' in message.text or '-' in message.text):
        if messanger in members:
            change_reputation_command(message, users, messanger, members, con, 'text')
        else:
            no_register(message)
    con.close()
