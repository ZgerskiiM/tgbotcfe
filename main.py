import telebot
from telebot import types


bot = telebot.TeleBot('5406393466:AAF3M57l-wuyP2v35gO3ERc76Hc8MEjmVjk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Записать остаток")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Что хочешь сделать?".format(message.from_user), reply_markup=markup)

milk = 0
slivki = 0
zerno = 0
water = 0
cacao = 0
hotchoc = 0
icec = 0
altmilk = 0

st018 = 0
st025 = 0
st035 = 0
st045 = 0
stpr = 0
kr75 = 0
kr80 = 0
kr90 = 0


product_name = 'Нет'
kolvo = ""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Записать остаток":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Продукты")
        btn3 = types.KeyboardButton("Упаковка")
        btn5 = types.KeyboardButton("Другое")
        btn6 = types.KeyboardButton("Показать текущий отчёт")
        btn4 = types.KeyboardButton("Отправить отчет Вове")
        markup.add(btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Что будем записывать?", reply_markup=markup)
    elif message.text == "Продукты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn21 = types.KeyboardButton("Молоко 3,2%, л")
        btn22 = types.KeyboardButton("Сливки 10%, л")
        btn23 = types.KeyboardButton("Зерно, кг")
        btn24 = types.KeyboardButton("Вода 0,5, шт")
        btn25 = types.KeyboardButton("Какао, кг")
        btn26 = types.KeyboardButton("Горячий шоколад, кг")
        btn27 = types.KeyboardButton("Мороженое, кг")
        btn28 = types.KeyboardButton("Альтернативное молоко, л")
        menubtn = types.KeyboardButton("Вернуться в меню")
        markup.add(btn21,btn22, btn23,btn24,btn25,btn26,btn27, btn28, menubtn)
        bot.send_message(message.chat.id, text="Выбери продукт", reply_markup=markup)
    elif message.text == "Упаковка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn31 = types.KeyboardButton("Стаканчики 0,180, шт")
        btn32 = types.KeyboardButton("Стаканчики 0,250 шт")
        btn33 = types.KeyboardButton("Стаканчики 0,350 шт")
        btn34 = types.KeyboardButton("Стаканчики 0,450 шт")
        btn35 = types.KeyboardButton("Стаканчики прозрачные 0,5, шт")
        btn36 = types.KeyboardButton("Крышки d75, рукав")
        btn37 = types.KeyboardButton("Крышки d80, рукав")
        btn38 = types.KeyboardButton("Крышки d90, рукав")
        menubtn=types.KeyboardButton("Вернуться в меню")
        markup.add(btn31, btn32, btn33, btn34, btn35, btn36, btn37, btn38, menubtn)
        bot.send_message(message.chat.id, text="Выбери вид упаковки", reply_markup=markup)
    elif message.text == "Вернуться в меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Продукты")
        btn3 = types.KeyboardButton("Упаковка")
        btn5 = types.KeyboardButton("Другое")
        btn6 = types.KeyboardButton("Показать текущий отчёт")
        btn4 = types.KeyboardButton("Отправить отчет Вове")
        markup.add(btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Вы вернулись в меню", reply_markup=markup)
    elif message.text == "Молоко 3,2%, л":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, milk1)
    elif message.text == "Альтернативное молоко, л":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, altmilk1)
    elif message.text == "Сливки 10%, л":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, slivki1)
    elif message.text == "Зерно, кг":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, zerno1)
    elif message.text == "Вода 0,5, шт":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, water1)
    elif message.text == "Какао, кг":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, cacao1)
    elif message.text == "Горячий шоколад, кг":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, hotchoc1)
    elif message.text == "Мороженое, кг":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, icec1)
    elif message.text == "Стаканчики 0,180, шт":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, stakan1)
    elif message.text == "Стаканчики 0,250 шт":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, stakan2)
    elif message.text == "Стаканчики 0,350 шт":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, stakan3)
    elif message.text == "Стаканчики 0,450 шт":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, stakan4)
    elif message.text == "Стаканчики прозрачные 0,5, шт":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, stakan5)
    elif message.text == "Крышки d75, рукав":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, krishka1)
    elif message.text == "Крышки d80, рукав":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, krishka2)
    elif message.text == "Крышки d90, рукав":
        bot.send_message(message.chat.id, "Введи остаток")
        bot.register_next_step_handler(message, krishka3)
    elif message.text == "Другое":
        bot.send_message(message.chat.id, "Что будем записывать?")
        bot.register_next_step_handler(message, another)
    elif message.text == "Показать текущий отчёт":
        otchet(message)
    elif message.text == "Отправить отчет Вове":
        going(message)
    else:
        bot.send_message(message.chat.id, text="Таких команд я не знаю..")

def going(message):
    bot.send_message(message.chat.id, "Отчет отправлен")
    bot.send_message(975670546, '\n <b>Остаток продуктов</b>:\n Молоко 3,2 % - ' + str(
        milk) + ' л\n Альтернативное молоко - ' + str(altmilk) + ' л\n Сливки 10% - ' + str(
        slivki) + ' л\n Зерно - ' + str(zerno) + ' кг\n '
                                                 'Вода - ' + str(water) + ' шт\n Какао - ' + str(
        cacao) + ' кг\n Горячий шоколад - ' + str(hotchoc) + ' кг\n Мороженное - ' + str(
        icec) + ' кг\n <b>Остаток упаковки</b>:\n Стаканы 0,18 - ' + str(st018) + ' шт\n Стаканчики 0,250 - ' + str(
        st025) + ' шт\n Стаканчики 0,350 - ' + str(st035) + ' шт\n '
                                                            'Стаканчики 0,450 - ' + str(
        st045) + ' шт\n Стаканчики прозрачные 0,5 - ' + str(
        stpr) + ' шт\n Крышки d75 - ' + str(kr75) + ' рукав\n Крышки d80 - ' + str(
        kr80) + ' рукав\n Крышки d90 - ' + str(kr90) + ' рукав\n <b>Другое:</b>\n  ' + product_name + '  ' + str(
        kolvo) + '', parse_mode='HTML')

def another(message):
    global product_name
    product_name = message.text
    bot.send_message(message.from_user.id, 'Введи остаток ' + product_name + '');

    bot.register_next_step_handler(message, kolvo1);

def kolvo1(message):
    global kolvo
    kolvo = str(message.text)
    while kolvo == 0:
        try:
            kolvo = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')

def altmilk1(message):
    global altmilk
    altmilk = str(message.text)
    while altmilk == 0:
        try:
            altmilk = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')

def milk1(message):
    global milk
    milk = str(message.text)
    while milk == 0:
        try:
            milk = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')

def slivki1(message):
    global slivki
    slivki = str(message.text)
    while slivki == 0:
        try:
            slivki = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')

def zerno1(message):
    global zerno
    zerno = str(message.text)
    while zerno == 0:
        try:
            zerno = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def water1(message):
    global water
    water = str(message.text)
    while water == 0:
        try:
            water = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def cacao1(message):
    global cacao
    cacao = str(message.text)
    while cacao == 0:
        try:
            cacao = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def hotchoc1(message):
    global hotchoc
    hotchoc = str(message.text)
    while hotchoc == 0:
        try:
            hotchoc = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def icec1(message):
    global icec
    icec = str(message.text)
    while icec == 0:
        try:
            icec = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def stakan1(message):
    global st018
    st018 = str(message.text)
    while st018 == 0:
        try:
            st018 = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def stakan2(message):
    global st025
    st025 = str(message.text)
    while st025 == 0:
        try:
            st025 = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def stakan3(message):
    global st035
    st035 = str(message.text)
    while st035 == 0:
        try:
            st035 = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def stakan4(message):
    global st045
    st045 = str(message.text)
    while st045 == 0:
        try:
            st045 = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def stakan5(message):
    global stpr
    stpr = str(message.text)
    while stpr == 0:
        try:
            stpr = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def krishka1(message):
    global kr75
    kr75 = str(message.text)
    while kr75 == 0:
        try:
            kr75 = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def krishka2(message):
    global kr80
    kr80 = str(message.text)
    while kr80 == 0:
        try:
            kr80 = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')


def krishka3(message):
    global kr90
    kr90 = str(message.text)
    while kr90 == 0:
        try:
            kr90 = str(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.chat.id, text="Остаток записан", parse_mode='Markdown')




def otchet(message):
        bot.send_message(message.chat.id,
                         '<b>Остаток продуктов</b>:\n Молоко 3,2 % - ' + str(milk) + ' л\n Альтернативное молоко - '+str(altmilk)+' л\n Сливки 10% - ' + str(
                             slivki) + ' л\n Зерно - ' + str(zerno) + ' кг\n '
                                                                      'Вода - ' + str(water) + ' шт\n Какао - ' + str(
                             cacao) + ' кг\n Горячий шоколад - ' + str(hotchoc) + ' кг\n Мороженное - ' + str(
                             icec) +  'кг\n <b>Остаток упаковки</b>:\n Стаканы 0,18 - ' + str(st018) + ' шт\n Стаканчики 0,250 - ' + str(
                             st025) + ' шт\n Стаканчики 0,350 - ' + str(st035) + ' шт\n '
                                                                      'Стаканчики 0,450 - ' + str(st045) + ' шт\n Стаканчики прозрачные 0,5 - ' + str(
                             stpr) + ' шт\n Крышки d75 - ' + str(kr75) + ' рукав\n Крышки d80 - ' + str(
                             kr80) + ' рукав\n Крышки d80 - '+ str(kr80) +' рукав\n <b>Другое:</b>\n '+product_name+' - '+str(kolvo)+'\n  '  ,parse_mode='HTML')


bot.polling(none_stop=True, interval=0)


