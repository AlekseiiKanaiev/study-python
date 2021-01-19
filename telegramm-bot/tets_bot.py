import telebot
import sqlite3
from sqlite3 import Error
import json
from config import Configurations

print(Configurations.bot_name)
bot_name = Configurations.bot_name
db_path = Configurations.db_path
bot_id = Configurations.bot_id

bot = telebot.TeleBot(bot_id)

commands = ['/start', '/commands', '/help', '/show', '/change']

def create_table():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS reputation (members TEXT, data TEXT)')
    con.commit()
    con.close()
create_table()

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
    bot.send_message(message.chat.id, 'You are not register yet!')
    bot.send_message(message.chat.id, 'Please, enter command:')
    bot.send_message(message.chat.id, '/start')

def wrong_command(message):
    bot.send_message(message.chat.id, 'Wrong command')
    bot.send_message(message.chat.id, 'Please enter:')
    bot.send_message(message.chat.id, '/change <user> <sign><number>(or it will be 1 as by default)')

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

def change_reputation_command(message, users, messanger, members, con):
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
                msg = 'Increased reputation\n@{}: {}'.format(user, data[user])
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
                msg = 'Decrease reputation\n@{}: {}'.format(user, data[user])
                bot.send_message(message.chat.id, msg)
                # bot.send_message(message.chat.id, '@{}: {}'.format(user, data[user]))
            else:
                bot.send_message(message.chat.id, 'No such member "@{}", that join this reputation raiting in the chat'.format(user))
    else:
        wrong_command(message)

def show_reputation_command(con, message, messanger):
    data = json.loads(get_reputation_for_member(con, messanger)[0][1])
    msg = ''
    users = [item for item in message.text.split(' ') if item.startswith('@')]
    print(users)
    if users:
        for user in users:
            msg += '{}: {}\n'.format(user, data[user[1:]])
    else:
        for key,val in data.items():
            msg += '@{}: {} \n'.format(key, val)
    if not msg:
        msg = 'You are alone in this raiting yet'
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

            # add_column_to_DB(con, messanger)

        # print(members)
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
    elif '/show' in message.text:
        if messanger in members:
            show_reputation_command(con, message, messanger)
        else:
            no_register(message)
    elif '/change' in message.text:
        if messanger in members:
            users = [item for item in message.text.split(' ') if item.startswith('@')]
            if users:
                change_reputation_command(message, users, messanger, members, con)
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
            change_reputation_command(message, users, messanger, members, con)
        else:
            no_register(message)
    con.close()

bot.polling(none_stop = True)
