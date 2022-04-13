import telebot
from telebot import types

from src.platonus_selenium.check_marks import start_webdriver
from src.enums import UserDataKeys, SubjectBoxKeys

token = '5115413693:AAFlHsjG9D64RJkhN5JlUgBnT3bKwZTU4o8'
bot = telebot.TeleBot(token)

user_data: dict[UserDataKeys, str] = {}


@bot.message_handler(commands=['start'])
def send_login(message):
    bot.send_message(message.chat.id, 'Введите логин: ')
    bot.register_next_step_handler(message, send_password)


def send_password(message):
    user_data[UserDataKeys.LOGIN] = message.text
    bot.send_message(message.chat.id, 'Введите пароль: ')
    bot.register_next_step_handler(message, auth_user)


def auth_user(message):
    user_data[UserDataKeys.PASSWORD] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    journal_button = types.KeyboardButton('Журнал оценок')
    markup.add(journal_button)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    bot.register_next_step_handler(message, get_journal)


def get_journal(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    period_1 = types.KeyboardButton('1')
    period_2 = types.KeyboardButton('2')
    markup.add(period_1, period_2)
    bot.send_message(message.chat.id, 'Выберите семестр', reply_markup=markup)
    bot.register_next_step_handler(message, get_marks)


journal_info: list = [
    'Предмет', 'Преподователь', 'Ср. текущая',
    'РК 1', 'РК 2', 'Рейтинг', 'Экзамен'
]


def get_marks(message):
    user_data[UserDataKeys.PERIOD] = message.text
    subject_boxes: list[dict[SubjectBoxKeys, str]] = start_webdriver(user_data)
    for d in subject_boxes:
        i: int = 0
        for value in d.values():
            bot.send_message(message.chat.id, f'{journal_info[i]}:  {value}')
            i += 1
        bot.send_message(message.chat.id, '_' * 30)


if __name__ == '__main__':
    bot.polling(none_stop=True)
