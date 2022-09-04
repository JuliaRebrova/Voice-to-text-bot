
import logging 
import os
from aiogram import Bot, Dispatcher, executor, types
from token_bot import tok

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from speech import recognize

# Configure logging
logging.basicConfig(level=logging.INFO)
          

bot = Bot(token=tok)
dp = Dispatcher(bot) 


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
    executor.start_polling(dp,skip_updates=True)

