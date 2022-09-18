import telebot
my_token = "5663035159:AAG7NbFtjo9FAyCramt5lLrj6i_SQAA50UI"

bot = telebot.TeleBot(my_token, parse_mode=None)

with open("question.txt", "r", encoding='utf-8') as file:
    data = file.readlines()
    if len(data) == 0:
        print("В настоящий момент вопросов нет")
    else:
        newdata = list(i.split() for i in data)
        for i in newdata:
            if not i[5].isdigit():
                textmessage1 = f"{i[3]} {i[4]}, {i[0]} в {i[1]} Вы спрашивали: "
                textmessage2 = ''
                print(i[2])
                for j in range(5, len(i)):
                    textmessage2 = textmessage2 + i[j] + ' '
                print(textmessage1)
                print(textmessage2)
                bot.send_message(i[2], textmessage1)
                bot.send_message(i[2], textmessage2)
                yourAnswer = 'Ответ специалистов  :  ' + input('Ваш ответ: ')
                bot.send_message(i[2], yourAnswer)
        with open("question.txt", "w", encoding='utf-8') as file:
            data = file.write("")