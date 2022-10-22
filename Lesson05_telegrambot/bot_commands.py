from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    await update.message.reply_text(f'Добро пожаловать, {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    await update.message.reply_text(f'Время, {datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    await update.message.reply_text(f'/hello\n/time\n/sum\n/help\n')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_command(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()   #sum
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')