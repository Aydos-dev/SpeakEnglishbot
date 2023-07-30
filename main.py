import logging

from aiogram import Bot, Dispatcher, executor, types
from MerriamWebster import getDefinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = '6354506610:AAFIPwIFiJ9byMIiDWi_Wkk51wnLQV_JjAQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start`
    """
    await message.reply("This bot can translate and find definitions of words")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends`/help` command
    """
    await message.reply("Type search word\nIf word in english, it returns its definitions with audio(if it exits), otherwise Bot translate it into english,then returns its definitions with audio")

@dp.message_handler()
async def translate(message: types.Message):

    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = "ru" if lang == "en" else "en"
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == "en":
            word_id = message.text
        else:
            word_id = translator.translate(message.text, "en").text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get("audio"):
                await message.reply_voice(lookup["audio"])
        else:
            await message.answer("Not found")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)