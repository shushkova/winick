from collections import defaultdict

from aiogram import types

import keyboards
from init_table_info.intersections import get_suitable, get_intersection
from initial_checkbox import order
from messages import Message
from state import State, choose_dishes
from telbot import bot
from telbot import dp
from user_choice import UserChoice

status = 'not started'

res_order = {}
res_wine = {}

data = defaultdict(UserChoice)


def get_order_cat(order_id):
    return [k for k, v in order_id.items() if v]


def get_next_state(res_order: list, curr):
    return res_order[res_order.index(curr) + 1]


@dp.callback_query_handler(lambda c: c.data == 'finish', state=State.FINAL_STATE)
async def process_callback_next(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    # await callback_query.message.reply(text=data[user_id].__str__(), reply=False)
    await callback_query.message.reply(text=" \n".join(str(x) for x in get_intersection(data[user_id])), reply=False)
    state = dp.current_state(user=user_id)
    await state.set_state(State.FINISH)


@dp.callback_query_handler(lambda c: c.data.startswith('next'), state=choose_dishes)
async def process_callback_next(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id
    state = dp.current_state(user=user_id)
    if callback_query.data == 'next':
        res_order[user_id] = get_order_cat(order[user_id])
        await state.set_state(res_order[user_id][0])
    else:
        res = callback_query.data.split('_')
        if user_id not in data.keys():
            data[user_id] = UserChoice()
        data[user_id].set(res[1], res[2])

    state_type = await state.get_state()
    if state_type == f'{State.PRE_FINAL_STATE}':
        await callback_query.message.reply(text=Message['finish'], reply=False,
                                           reply_markup=keyboards.inline_kb_finish)
    else:
        buttons = get_suitable(data[user_id], state_type)
        await callback_query.message.reply(text=Message[state_type], reply=False,
                                               reply_markup=keyboards.get_keyboard_by_buttons(state_type, buttons))
        if not len(buttons):
            await callback_query.message.reply(text=Message['fail_finish'], reply=False,
                                               reply_markup=keyboards.inline_kb_fail_finish)
    await state.set_state(get_next_state(res_order[user_id], state_type))
