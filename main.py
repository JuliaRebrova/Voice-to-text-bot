
import logging 
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.executor import start_webhook
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from speech import recognize


# Configure logging
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

os.system("sudo apt update")
os.system("sudo apt install ffmpeg")

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()

button_start = KeyboardButton('/start')
start_kb = ReplyKeyboardMarkup()
start_kb.add(button_start) 

greating = 'Привет!\n Я расшифрую твои голосовые сообщения.'
help_text = 'Просто перешли мне голосовое сообщение.'

@dp.message_handler(commands=['help']) 
async def send_welcome(message): 
    await message.reply(help_text)

@dp.message_handler(commands=['start']) 
async def send_welcome(message): 
    await message.reply(greating)

@dp.message_handler(content_types=types.ContentType.ANY)
async def download(ms: types.Message):
    file_id = ms.voice.file_id
    file = await bot.get_file(file_id)
    logging.info(file.file_path)
    file_path = file.file_path
    os.system("mkdir voice")
    await bot.download_file(file_path, "voice/123.ogg")
    os.system("ffmpeg -i voice/123.ogg voice/123.wav")
    # abs_path = os.path.abspath("voice/123.ogg")
    # convert_ogg_to_wav(abs_path)
    recognized_text = recognize("voice/123.wav")
    await bot.send_message(ms.chat.id, recognized_text)
    os.system("rm -rf voice")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )