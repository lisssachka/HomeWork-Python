from os import getenv

from telegram import Bot, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)


token1 = '6021502705:AAHW7IzQktCoATVVjglRH8K4mt3LDDZiWpY'

bot = Bot(token=token1)
updater = Updater(token=token1)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет!\nПришли мне сообщение, и я удалю из него слова,\nв которых содежится "абв"')


def delete_words(update, context):
    text = update.message.text.split()
    send_text = filter(lambda word:'абв' not in word.lower(), text)
    if len(text) !=0:
        context.bot.send_message(update.effective_chat.id,f"{' '.join(send_text)}")
    else:
        context.bot.send_message(update.effective_chat.id,'Все слова были удалены')
    


start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text, delete_words)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)


updater.start_polling()
updater.idle()