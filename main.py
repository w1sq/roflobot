# coding=utf8
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputTextMessageContent, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import re
from aiogram.dispatcher.filters import Text
from aiogram.types.inline_query_result import InlineQueryResultArticle
from bs4 import BeautifulSoup
import requests
import random
import json 

with open('key.txt','r',encoding='utf-8') as f:
    API_KEY = str(f.readline())
logging.basicConfig(level=logging.INFO, filename='botlogs.log')
bot = Bot(token=API_KEY)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
acc = requests.get('https://www.instagram.com/privet_kak_zhizn/?__a=1')
with open('photos.json','r',encoding='utf8') as f:
    data = json.load(f)
    data = data['data']['user']['edge_owner_to_timeline_media']['edges']
print('Bot started')

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет, {message.from_user.username}!\n\nЭто смешнявка от анонимуза.')


@dp.inline_handler(text="", state="*")
async def inline_handler(query: types.InlineQuery):
    results=[
            InlineQueryResultArticle(
                id=999,
                title='Отправить Дашу',
                thumb_url= 'https://scontent-hel3-1.cdninstagram.com/v/t51.2885-15/e35/17332877_630544370469356_8849889635074048000_n.jpg?_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=108&_nc_ohc=UJIRnp_o9oYAX8FILjr&edm=AP_V10EBAAAA&ccb=7-4&oh=0148a9bb89ac93b9d1a20cf7e58a55aa&oe=61154475&_nc_sid=4f375e',
                input_message_content=InputTextMessageContent(
                   message_text=f'''ЛЯ какая<a href='{data[random.randint(0,len(data)-1)]['node']['display_url']}'>&#8205</a>''',
                   parse_mode='html'
                ),
            )
        ]
    await query.answer(
        results=results,
        cache_time=0,
        switch_pm_text="Перейти в бот",
        switch_pm_parameter="start",
    )

async def main():
    await dp.start_polling()

def download_pic(url):
    pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.run(main())