import logging
from re import X
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

_TOKEN_ = "1874974266:AAGHFcmkSrjBP4OxySmxvAxZRTC0xaxzgY"

updater = Updater(token=_TOKEN_, use_context=True)
dispatcher = updater.dispatcher

import sqlite3
con = sqlite3.connect('add_sqlite3.db',check_same_thread = False)
cur = con.cursor()

# cur.execute('''CREATE TABLE stocks
#                (name, url)''')

# cur.execute("INSERT INTO stocks VALUES ('麻豆区块链','https://t.me/madouqukuailian')")
# cur.execute("INSERT INTO stocks VALUES ('币圈项目维权群','https://t.me/weiquanqunz')")
# cur.execute("INSERT INTO stocks VALUES ('区块链大佬交流群','https://t.me/dalaojiaoliu')")
# cur.execute("INSERT INTO stocks VALUES ('币圈盘子交流群','https://t.me/biqunpanzi')")


def text_url_fun(chaxun):
    sql = "SELECT name,url FROM stocks"
    sql2 = "SELECT * FROM stocks WHERE name LIKE '%{0}%'".format(chaxun)
    cur.execute(sql2)
    # print(cur.fetchall())
    # print(cur.fetchone())
    text_url = cur.fetchall()
    x = ""
    # for i in text_url:
    #     text_url_demo = r"<a href='{0[1]}'>{0[0]}</a>".format(i)+"\n"
    #     x = x + text_url_demo
    # return x
    
    for i in range(10):
        y = text_url[i]
        # print(y)
        text_url_demo = r"<a href='{0[1]}'>{0[0]}</a>".format(y)+"\n"+"\n"
        x = x + text_url_demo

    return r"<a href='https://t.me/xxx'>👉--广告位招租中--👈</a>"+"\n"+"\n" + x + r"<a href='https://t.me/xxx'>👉--👮‍♂️举报恶意链接--👈</a>"+"\n"
    # print(text_url[0])
    # return text_url

# 判断数据库返回是否过长



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="你好")  

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id,
    text=text_url_fun(), parse_mode=ParseMode.HTML)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    context.bot.send_message(chat_id=update.effective_chat.id,
    text=text_url_fun(update.message.text), parse_mode=ParseMode.HTML,reply_to_message_id=update.message.message_id)

help_handler = CommandHandler('help', help_command)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(CommandHandler("start", start))
# on non command i.e message - echo the message on Telegram
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


updater.start_polling()