from aiogram import types
import aiogram_dialog
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import DialogManager, DialogRegistry, StartMode
from asyncio import sleep

import keyboards
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


# todo
async def start_conversation(dialog_manager, user_id):
    state = dp.current_state(user=user_id)
    print('Start with ', await state.get_state())
    await init_order(user_id)
    data[user_id] = UserChoice()
    await dialog_manager.start(Initial_checkbox.main, mode=StartMode.NEW_STACK)
    await sleep(0.01)
    await bot.send_message(user_id, "Выбраны все категории?", reply_markup=keyboards.inline_kb_next)
    await state.set_state(State.INIT)


@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, dialog_manager: DialogManager):
    await start_conversation(dialog_manager, message.from_user.id)


@dp.callback_query_handler(lambda c: c.data == 'retry', state='*')
async def start_command(callback_query: types.CallbackQuery, dialog_manager: DialogManager):
    await bot.answer_callback_query(callback_query.id)
    await start_conversation(dialog_manager, callback_query.from_user.id)
