
import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import dotenv_values
from app_bot.speech import recognize


# Configure logging
logging.basicConfig(level=logging.INFO)


config =  dotenv_values(".env")
token = config["token"]
bot = Bot(token=token)
dp = Dispatcher(bot) 

button_start = KeyboardButton('/start')
start_kb = ReplyKeyboardMarkup()
start_kb.add(button_start)

greating = 'Привет!\n Я расшифрую твои голосовые сообщения.'
help_text = 'Просто перешли мне голосовое сообщение.'

@dp.message_handler(commands=['help']) 
async def send_welcome(message): 
    if os.path.exists("./voice_data"):
        os.system("rm -rf voice_data")
    await message.reply(help_text)

@dp.message_handler(commands=['start']) 
async def send_welcome(message):
    if os.path.exists("./voice_data"):
        os.system("rm -rf voice_data")
    await message.reply(greating)

@dp.message_handler(content_types=types.ContentType.ANY)
async def download(ms: types.Message):
    file_id = ms.voice.file_id
    file = await bot.get_file(file_id)
    logging.info(file.file_path)
    file_path = file.file_path
    if os.path.exists("./voice_data"):
        os.system("rm -rf voice_data")
    else:
        os.system("mkdir voice_data")
    await bot.download_file(file_path, "voice_data/123.ogg")
    os.system("ffmpeg -i voice_data/123.ogg voice_data/123.wav")
    try:
        recognized_text = recognize("voice_data/123.wav")
        if recognized_text:
            await bot.send_message(ms.chat.id, recognized_text)
        else:
            await bot.send_message(ms.chat.id, "Не удалось распознать")
    except Exception:
        await bot.send_message(ms.chat.id, "Не удалось распознать")
    os.system("rm -rf voice_data")


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
