import telebot
from configi import valut, TOKEN
from extensions import ApiException, Convertor


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n Название валюты - \
    В какую валюту перевести - \
    Количество переводимой валюты \
    \n<Увидеть список всех доступных валют команда /values>'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in valut.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split()
    values = list(map(str.lower, values))
    try:
        result = Convertor.get_price(values)
    except ApiException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать запрос \n{e}')
    else:
        text = f'Цена {values[0]} {values[1]} в {values[2]} -- {result} {valut[values[1]]}'


bot.polling()