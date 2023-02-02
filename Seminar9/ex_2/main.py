from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot_commands import *
from model import *

token1 = '6021502705:AAHW7IzQktCoATVVjglRH8K4mt3LDDZiWpY'

bot = Bot(token=token1)
updater = Updater(token=token1)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
game_handler = MessageHandler(Filters.text, game)
restart_handler = MessageHandler(Filters.text, restart_game)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={STATES[0]: [game_handler],
                                   STATES[1]: [restart_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()