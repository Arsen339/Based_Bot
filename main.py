import telebot
import os
import config
from telebot import types
from update_date_base_processing import currency_update_time_check, crypto_update_time_check, metal_update_time_check
from values_bases_processing import get_currency, get_crypto, get_metal
from currency_parser import menue
from crypto_parser import main
from metal_parser import menu
from user_database_processing import find_person


f = open("user_status.txt", "w")
f.write("00")
f.close()


def file_check():
    """Проверяем состояние пользователя"""
    f = open("user_status.txt", "r")
    status = f.read(2)
    f.close()
    return status


print(file_check())

bot = telebot.TeleBot("5125732372:AAGhls63drN8aAMUoPSbX0FysbuWshXLeZ8")


@bot.message_handler(commands=['start'])
def welcome(message):
    try:
        os.remove("USER_STATE.db")
    except FileNotFoundError:
        print("No file to remove: USER_STATE.db")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("валюта")
    item2 = types.KeyboardButton("криптовалюта")
    item3 = types.KeyboardButton("металлы")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Здравствуйте!Для регистрации введите имя, фамилию и год рождения с меткой reg "
                                      "как в образце:"
                                      "reg Name, Surname, 2001"
                                      "Для получения информации о курсах металлов, криптовалют и "
                                      "валют введите me, cr и cur соответственно ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def instr(message):

    if (message.text == 'USD' or message.text == 'JPY' or message.text == 'SGD' or message.text == 'EUR' or \
            message.text == 'CNY') and (file_check() == '10' or file_check() == '11'):
        if currency_update_time_check() == 1:
            answering, img_src = get_currency(message.text)
            for i in range(0, 30):
                bot.send_message(message.chat.id, answering[i])
            print(img_src)

        #    bot.send_photo(message.chat.id, "C:/Users/Admin/PycharmProjects/Based_BotV2/tmp_img/export_img.png")
            bot.send_photo(message.chat.id, open(img_src, "rb"))
        else:
            bot.send_message(message.chat.id, "Повторите запрос позже, идет загрузка данных")

            menue(message.text, 30)

    elif message.text in ["BTC", "ETH", "LTC", "BCH", "XMR", "DASH", "ZEC", "VTC", "BTS", "FTC", "XEM", "DOGE", "MAID",
                          "DBG", "CLAM", "SC", "DCR", "EMC2"] and (file_check() == '10' or file_check() == '11'):
        if crypto_update_time_check() == 1:
            answering, img_src = get_crypto(message.text)
            for i in range(0, 30):
                bot.send_message(message.chat.id, answering[i])
            bot.send_photo(message.chat.id, img_src)
        else:
            bot.send_message(message.chat.id, "Повторите запрос позже, идет загрузка данных")
            main(message.text, 30)
    elif message.text in ["au", "ag", "pt", "pd"] and file_check() == '11':
        if metal_update_time_check() == 1:
            answering, img_src = get_metal(message.text)
            for i in range(0, 30):
                bot.send_message(message.chat.id, answering[i])
            bot.send_photo(message.chat.id, img_src)
        else:
            bot.send_message(message.chat.id, "Повторите запрос позже, идет загрузка данных")
            menu(message.text, 30)
    elif "reg" in message.text:

        reg_inf = message.text.split()
        print(reg_inf)
        access_level = find_person(reg_inf)
        print(access_level)
        if access_level[0] == 1 and access_level[1] == 1:
            bot.send_message(message.chat.id, "Вы вип-пользователь")
            f = open("user_status.txt", "w")
            f.write("11")
            f.close()

        elif access_level[0] == 1 and access_level[1] == 0:
            bot.send_message(message.chat.id, "Вы обычный пользователь. просмотр курса металлов не доступен")
            f = open("user_status.txt", "w")
            f.write("10")
            f.close()
        else:
            bot.send_message(message.chat.id, "Вход не выполнен. опробуйте еще раз")
            f = open("user_status.txt", "w")
            f.write("00")
            f.close()

    elif message.text not in ["валюта", "криптовалюта",
                              "металлы"]:
        bot.send_message(message.chat.id, "В запросе ошибка!")

    if message.chat.type == 'private':
        if message.text == "валюта":
            bot.send_message(message.chat.id, "Выберите валюту: USD-доллар, EUR-евро, SGD-сингапурский доллар, "
                                              "JPY-йена, CNY-юань ")
        elif message.text == "металлы":
            bot.send_message(message.chat.id, "Выберите металл: au-золото, ag-серебро, pt-платина, pd-палладий (только для VIP)")
        elif message.text == "криптовалюта":
            bot.send_message(message.chat.id, "Выберите криптовалюту: Bitcoin, Ethereum, Litecoin, BitcoinCash, Monero, "
                                              "Dash, Zcash, Vertcoin, Bitshares,"
                                              " Factom, XEM, Dogecoin, MaidSafeCoin, "
                                              "Digibyte, Clams, Siacoin, Decred, Einsteinium")


# RUN
bot.polling(none_stop=True)
