from aiogram import types
import aiogram_dialog
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import DialogManager, DialogRegistry, StartMode
from asyncio import sleep

import keyboards
import model
from callback_query_handler import data
from telbot import dp
from telbot import bot
from initial_checkbox import Initial_checkbox, dialog, init_order, order
from state import State
from user_choice import UserChoice

status = 'not started'
registry = DialogRegistry(dp)
registry.register(dialog)
bot.id


# todo
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    """отправиь список команд бота"""
    await message.reply(
        text="""
        Это WineBot. Выводит рекоммендацию по винам исходя из гастрономических предпочтений\n
        Мои команды: 
        /start - начать подбор рекоммендации
        /help -- увидеть помощь"""
    )


@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(State.INIT)
    await message.reply("Выберите что дальше", reply_markup=keyboards.inline_kb_choose_flow, reply=False)


@dp.message_handler(state=State.TEXT)
async def text_handling(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(State.INIT)
    await message.reply("Обрабатываем текст", reply=False)
    result = await model.predict(message.text)
    await message.reply('Подходящие вина: ' + result, reply=False, reply_markup=keyboards.inline_kb_finish_text)
