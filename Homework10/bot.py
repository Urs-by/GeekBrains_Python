import telebot
import datetime

my_token ="5663035159:AAG7NbFtjo9FAyCramt5lLrj6i_SQAA50UI"
# t.me/gb_homework9_bot
bot = telebot.TeleBot(my_token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ " + message.from_user.first_name)
    bot.send_message(message.chat.id, "Я сервис бот, \n"
                                      "Для связи с сервесной службой задайте свой вопрос: ")
    bot.send_message(message.chat.id, 'Введите  Ваш номер телефона в цифровом формате без тире и пробелов:')

def writeQuestion(message):
    text = message.text
    data = f"{datetime.datetime.today()} {message.from_user.id} {message.from_user.first_name} {message.from_user.last_name}:  {text} \n"
    with open("question.txt", "a", encoding='utf-8') as file:
        file.writelines(data)


@bot.message_handler(content_types=["text"])
def function_text(message):
    text = message.text
    if text.isdigit():
        writeQuestion(message)
        bot.send_message(message.chat.id, 'Ваш номер сохранен, введите вопрос:')
    elif text.lower() == 'да':
        bot.send_message(message.chat.id, 'Введите Ваш вопрос:')
    elif text.lower() == 'нет':
        bot.send_message(message.chat.id,
                         "Спасибо за вопросы, наш специалист в ближайшее время обязательно ответит Вам")
        bot.send_message(message.chat.id,
                         "Для новых вопросов нажмите /start")
    else:
        bot.send_message(message.chat.id, 'У Вас еще остались вопросы? :')
        writeQuestion(message)

bot.polling(none_stop=True, interval=0)