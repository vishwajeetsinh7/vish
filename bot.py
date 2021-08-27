import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

FIRST, SECOND = range(2)

ONE, TWO, THREE, SOVER = range(4)



def start(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    keyboard = [
        [
            InlineKeyboardButton("bot 1", callback_data=str(ONE)),
        ],
        [
            InlineKeyboardButton("bot 2", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("bot 3", callback_data=str(TWO)),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("choose bot", reply_markup=reply_markup)
    return FIRST


def start_over(update: Update, context: CallbackContext) -> int:

    query = update.callback_query 
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("bot 1", callback_data=str(ONE)),
        ],
        [
            InlineKeyboardButton("bot 2", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("bot 3", callback_data=str(THREE)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    query.edit_message_text(text="choose bot", reply_markup=reply_markup)
    return FIRST


def one(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("<< back <<", callback_data=str(SOVER)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="@vish34_bot", reply_markup=reply_markup
    )
    return SECOND


def two(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("<< BACK <<", callback_data=str(SOVER)),
           
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="bot2", reply_markup=reply_markup
    )
    return SECOND


def three(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("<< BACK <<", callback_data=str(SOVER)),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="BOT 3 ", reply_markup=reply_markup
    )
    return SECOND


def help_command(update: Update, context: CallbackContext) -> None:

    """Send a message when the command /help is issued."""

    update.message.reply_text('Hey!')





def echo(update: Update, context: CallbackContext) -> None:

    """Echo the user message."""

    update.message.reply_text(update.message.text)







def main() -> None:
    """Run the bot."""
    updater = Updater("fadsfasdkfjds enter token nu 2")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))




    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(SOVER) + '$'),
                CallbackQueryHandler(start_over, pattern='^' + str(SOVER) + '$'),
                CallbackQueryHandler(start_over, pattern='^' + str(SOVER) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

 
    updater.idle()


if __name__ == '__main__':
    main()
