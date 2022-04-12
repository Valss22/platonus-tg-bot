import telebot

from src.main import token

a = 0

bot = telebot.TeleBot(token)


def inline():
    inl_key = telebot.types.InlineKeyboardMarkup()
    but1 = telebot.types.InlineKeyboardButton(text="1", callback_data="test")
    #   inl_key.add(but1)

    but2 = telebot.types.InlineKeyboardButton(text="2", callback_data="asa")
    inl_key.add(but1, but2)
    return inl_key


def qwerty():
    markup1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup1.add('Yes', 'No')
    return markup1


def asdfgh():
    markup2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup2.add('Timetable', 'Platonus')
    return markup2


@bot.callback_query_handler(func=lambda c: True)
def inline_net(c):
    if c.data == "test":
        bot.edit_message_text(text="Ok",
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              parse_mode='Markdown')
    elif c.data == "asa":
        bot.edit_message_text(text="None",
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              parse_mode='Markdown')


@bot.message_handler(commands=['start', 'go'])
def rowsing(message):
    print(str(message.chat.id))
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('Timetable', 'Platonus')
    message = bot.reply_to(message, 'Выберите', reply_markup=markup)
    # bot.register_next_step_handler(message, process_step)
    # rows.row("Журнал оценок")
    # rows.row("Расписание")


@bot.message_handler(content_types=["text"])
def row(message):
    global a
    global Log
    global Prl
    global Sms
    if message.text == "pil":
        bot.send_message(message.chat.id, 'qwertyasdfghjklzxcvbnm,.sdfghjkl', reply_markup=inline())
    if message.text == "Platonus":
        try:
            v = parser("Қабдолла_Аңсаған", "1106", "2", "2019")
        except:
            print(12)
            v = parser("Қабдолла_Аңсаған", "1106", "2", "2019")
        # img = open('{}.PNG'.format(Log+Prl+"1"), 'rb')
        bot.send_message(message.chat.id, v)
        # a=0
        # bot.send_message(message.chat.id,"Введите логин")
        # a+=1
    elif a == 1:
        Log = message.text
        bot.send_message(message.chat.id, "Введите пароль")
        a += 1
    elif a == 2:
        Prl = message.text
        bot.send_message(message.chat.id, "Семестр")
        a += 1
    elif a == 3:
        Sms = message.text
        bot.send_message(message.chat.id, "Ваш логин: {}\nВаш пароль: {}\nСеместр: {}".format(Log, Prl, Sms),
                         reply_markup=qwerty())
        a += 1
    # message= bot.reply_to(message, 'Выберите', reply_markup=qwerty())
    elif a == 4 and message.text == "Yes":
        v = parser(Log, Prl, Sms, '2019')
        img = open('{}.PNG'.format(Log + Prl + "1"), 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, v)
        a = 0
    elif a == 4 and message.text == "No":
        bot.send_message(message.chat.id, "Попробуйте сначала", reply_markup=asdfgh())

        a = 0


if __name__ == '__main__':
    bot.polling(none_stop=True)
