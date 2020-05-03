from telegram import Bot
from telegram import Update
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram import KeyboardButton
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Filters

from TelegramBot.config import TEL_TOKEN
from TelegramBot.config import TEL_API_URL

button_help = 'Help me!'
def help_button_handler(update:Update,context:CallbackContext):
    update.message.reply_text(
        text = 'This is Help Button',
        reply_markup= ReplyKeyboardRemove()
    )

def message_handler(update:Update,context:CallbackContext):
    text = update.message.text
    if text == button_help:
        return help_button_handler(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
     keyboard=[
            [
                #keyboard painting 1 row and 1 column
                KeyboardButton(text=button_help),
            ],
        ],
        resize_keyboard=True, #in case if we  are painting some buttons
    )
    update.message.reply_text(
        text = 'Hi press the button!',
        reply_markup = reply_markup
    )

def main():
    print('Start')
    bot = Bot(
        token= TEL_TOKEN,

        #uncomment this in case if your provider is blocking Telegram API
        #base_url=TEL_API_URL,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all,callback=message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()