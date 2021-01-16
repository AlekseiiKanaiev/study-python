import telebot
import sqlite3
from sqlite3 import Error
import json

# def create_connection():
#     connection = None
#     try:
#         connection = sqlite3.connect('/home/oleksii/VSCode/Study-python/telegramm-bot/Chinook_Sqlite.sqlite')
#         print('Connection succesfull')
#     except Error as e:
#         print(f'Error {e} occured')
#     return connection

# conn = create_connection()
# # Создаем курсор - это специальный объект который делает запросы и получает их результаты
# cursor = conn.cursor()
# # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
# cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
# # Получаем результат сделанного запроса
# results = cursor.fetchall()
# print(results)
# member = {'@rob': {'@helen':0}}
# print(json.dumps(member))
# # Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
# cursor.execute("INSERT into Artist values (Null, ?) ", json.dumps(member))
# # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
# conn.commit()
# # Проверяем результат
# cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
# results = cursor.fetchall()
# print(results)

def create_table():
    # Connect to a DB
    # if there is no file, it will create it
    con = sqlite3.connect('telegramm-bot/reputationBot.db')

    # Create a cursor object
    cur = con.cursor()

    # Write an SQL query (create table with 3 columns)
    # if you run code twice, you will get an error
    # to avoid this you shoud and a condition to SQL code
    # cur.execute('CREATE TABLE IF NOT EXISTS reputation (members TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS reputation (members TEXT, data TEXT)')


    # Commit a changes
    con.commit()

    # Close DB connection
    con.close()
create_table()

# con = sqlite3.connect('telegramm-bot/reputationBot.db')
def get_members_from_DB(con):
    cur = con.cursor()
    cur.execute("SELECT members FROM reputation")
    results = cur.fetchall()
    # print(results)
    return results
# get_members_from_DB(con)
# con.close()

def add_new_member_to_DB(con, name, data):
    cur = con.cursor()
    # cur.execute('INSERT INTO reputation DEFAULT VALUES')
    # con.commit()
    # cur.execute('UPDATE reputation SET members = ? WHERE members IS NULL', (name,))
    # con.commit()
    cur.execute('INSERT INTO reputation VALUES (?, ?)', (name, json.dumps(data),))
    con.commit()

# def add_column_to_DB(con, name):
#     cur = con.cursor()
#     command = f'ALTER TABLE reputation ADD COLUMN {name} INT DEFAULT 0'
#     cur.execute(command)

def update_table(con, member, data):
    cur = con.cursor()
    command = f'UPDATE reputation SET data = ? WHERE members = ?'
    cur.execute(command, (json.dumps(data), member,))
    con.commit()

def get_reputation_for_member(con, member):
    cur = con.cursor()
    cur.execute("SELECT * FROM reputation WHERE members = ?", (member,))
    results = cur.fetchall()
    return results

bot = telebot.TeleBot('1519220860:AAH4nvuot8wSaDemwxmo0mYy1MDFmMPY3jA')

commands = ['/start', '/commands', '/help', '/show', '/change', '/test']
# members = {'@helen': {'@rob':0}, '@rob': {'@helen':0}}

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
                bot.send_message(message.chat.id, 'Increased reputation ')
                bot.send_message(message.chat.id, f'@{user}: {data[user]}')
            else:
                bot.send_message(message.chat.id, f'No such member "@{user}", that join this reputation raiting in the chat')
    elif check_sign_position(message, '-'):
        for user in users:
            user = user[1:]
            if (user in data.keys()):
                data[user] -= number
                update_table(con, messanger, data)
                bot.send_message(message.chat.id, 'Decrease reputation ')
                bot.send_message(message.chat.id, f'@{user}: {data[user]}')
            else:
                bot.send_message(message.chat.id, f'No such member "@{user}", that join this reputation raiting in the chat')
    else:
        wrong_command(message)

def show_reputation_command(con, message, messanger):
    data = json.loads(get_reputation_for_member(con, messanger)[0][1])
    # print(data)
    for key,val in data.items():
        # print(f'{key}:{val}')
        bot.send_message(message.chat.id, f'@{key}: {val}')

@bot.message_handler(commands=[c[1:] for c in commands])
def start_message(message):
    # global members
    # print(message)
    con = sqlite3.connect('telegramm-bot/reputationBot.db')

    messanger = f'{message.from_user.first_name}_{message.from_user.last_name}' if message.from_user.username == None else f'{message.from_user.username}'
    # print(messanger)
    members = [item[0] for item in get_members_from_DB(con)]
    # print(members)
    if message.text == '/test':
        print(json.loads(get_reputation_for_member(con, messanger)[0][1]))
    if message.text == '/start' or message.text == '/start@test_mytest_isnottaken_bot':
        # if members.get(messanger):
        if messanger in members:
            bot.send_message(message.chat.id, 'You already joined this reputation raiting')
            show_reputation_command(con, message, messanger)
        else:
            bot.send_message(message.chat.id, 'Hello, this bot is showing your reputation raiting with others members in the chat')
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
    elif message.text == '/commands':
        # if members.get(messanger):
        if messanger in members:
            bot.send_message(message.chat.id, 'List of all commands')
            for item in commands:
                bot.send_message(message.chat.id, item)
        else:
            no_register()
    elif message.text == '/help':
        description = 'With this bot you can change reputation status with everyone who joined ti this raiting (when typed command /start). /n You can type /change <user_name> <sign>(<number>) to change reputation./n '
        bot.send_message(message.chat.id, description)
    elif message.text == '/show':
        if messanger in members:
            show_reputation_command(con, message, messanger)
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
    con = sqlite3.connect('telegramm-bot/reputationBot.db')
    members = [item[0] for item in get_members_from_DB(con)]
    # print(members)

    messanger = f'{message.from_user.first_name}_{message.from_user.last_name}' if message.from_user.username == None else f'{message.from_user.username}'

    users = [item for item in message.text.split(' ') if item.startswith('@')]
    if users and ('+' in message.text or '-' in message.text):
        if messanger in members:
            change_reputation_command(message, users, messanger, members, con)
        else:
            no_register(message)
    con.close()

bot.polling()
