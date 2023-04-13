# -*- coding: utf-8 -*-
import html
import datetime
import time
import telegram
from telegram import Poll, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, PollAnswerHandler, ConversationHandler, MessageHandler, Filters
import pytz
import json
import functools
kiev_tz = pytz.timezone('Europe/Kiev')


TOKEN = '1825772332:AAHONa_ixa4fKQLkjwl9NlsopwPBj0J22rE' #https://t.me/avaplace_bot
# TOKEN = '6253704444:AAGci_sXfi-iYBX3KE7kHiCRRAlQCrPMA00'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
bot = updater.bot
chat_id = '-1001816489018'


Full_data = []


def reading_file():
    with open("data.json", encoding='utf-8') as infile:
        data = json.load(infile)
        data_bytes = json.dumps(data).encode('utf-8')

    # i = 1
    print(data)
    # print(data_bytes)
    for chat in data:
        # print(i)
        Full_data.append(chat)
        # print(chat)
        # i += 1


reading_file()


def daily_poll(chatID, questionID, answers):
    # Your poll details
    chat_id_e = chatID
    question = questionID
    options = answers

    is_anonymous = False

    # Send poll to specific chat ID

    bot.send_poll(chat_id=chat_id_e, question=question, options=options, is_anonymous=is_anonymous, close_date=(datetime.datetime.now() + datetime.timedelta(minutes=1)))
    print("Poll send at:", datetime.datetime.now().time())



def command_to_resent_poll(update, context, question, options):

    is_anonymous = False

    chat_id = update.effective_chat.id

    context.bot.send_poll(chat_id=chat_id, question=question, options=options, is_anonymous=is_anonymous, close_date=(datetime.datetime.now() + datetime.timedelta(minutes=1)))
    print("Poll send at:", datetime.datetime.now().time())



def start(update, context):
    keyboard = [[InlineKeyboardButton("Доступні команди", callback_data='commands')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Вітаю! Я бот. Я допоможу тобі з ...', reply_markup=reply_markup)


def commands(update, context):
    update.callback_query.answer()

    update.callback_query.edit_message_text(text="Список команд: \n Торги - /poll1,\n Скарги -/poll2,\n Технолог - /poll3,\n Начальник виробництва - /poll4")


start_handler = CommandHandler('start', start)
commands_handler = CallbackQueryHandler(commands, pattern='^commands$')

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(commands_handler)


resend_poll1 = functools.partial(command_to_resent_poll, question=Full_data[0]["Question"], options=Full_data[0]["Answer"])
print(Full_data[0]["Question"])
poll_handler = CommandHandler('poll2', resend_poll1)
updater.dispatcher.add_handler(poll_handler)

resend_poll2 = functools.partial(command_to_resent_poll, question=Full_data[1]["Question"], options=Full_data[1]["Answer"])
poll_handler = CommandHandler('poll1', resend_poll2)
updater.dispatcher.add_handler(poll_handler)

resend_poll3 = functools.partial(command_to_resent_poll, question=Full_data[2]["Question"], options=Full_data[2]["Answer"])
poll_handler = CommandHandler('poll3', resend_poll3)
updater.dispatcher.add_handler(poll_handler)

resend_poll4 = functools.partial(command_to_resent_poll, question=Full_data[3]["Question"], options=Full_data[3]["Answer"])
poll_handler = CommandHandler('poll4', resend_poll4)
updater.dispatcher.add_handler(poll_handler)


# Start the bot

now = datetime.datetime.now().time()

updater.start_polling()

while True:
    now = datetime.datetime.now().time()

    for elm in Full_data:
        if now.hour == elm["Hour"] and now.minute == elm["Minutes"]:
            daily_poll(elm["Chat_ID"], elm["Question"], elm["Answer"])

    time.sleep(60)

updater.idle()
