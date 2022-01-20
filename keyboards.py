from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from init_table_info.food_and_wine_types import FoodWine
from state import State

inline_kb_choose_flow = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Текст', callback_data='text')],
        [InlineKeyboardButton(text='Схема', callback_data='schema')]
    ]
)

inline_kb_finish_text = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Заново', callback_data='text')],
        [InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back_to_menu')]
    ]
)

inline_kb_next = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да', callback_data='next')]
    ]
)

inline_kb_finish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да', callback_data='finish')],
        [InlineKeyboardButton(text='Подобрать заново', callback_data='schema')],
        [InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back_to_menu')]
    ]
)

inline_kb_fail_finish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Подобрать заново', callback_data='schema')],
        [InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back_to_menu')]
    ]
)


def generate_keyboard(dish_type: str) -> object:
    """
    Генерация клавиатуры
    :param dish_type: тип блюда питания
    :return: встреонная клавиатура для определенного типа
    """
    buttons = [[InlineKeyboardButton(text=i, callback_data=f'next_{dish_type}_{i}')]
               for i in FoodWine().return_options(dish_type)]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


inline_kb_meat = generate_keyboard('meat')
inline_kb_preparation = generate_keyboard('preparation')
inline_kb_dairy = generate_keyboard('dairy')
inline_kb_vegetable = generate_keyboard('vegetable')
inline_kb_starch = generate_keyboard('starch')
inline_kb_spice = generate_keyboard('spice')
inline_kb_sweet = generate_keyboard('sweet')


def get_keyboard_by_buttons(dish_type, buttons):
    keyboard_buttons = [[InlineKeyboardButton(text=i, callback_data=f'next_{dish_type}_{i}')]
                        for i in buttons]
    return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)


def get_keyboard_by(state):
    print(state == f'{State.VEGETABLE}')
    if state == f'{State.MEAT}':
        return inline_kb_meat
    elif state == f'{State.PREPARATION}':
        return inline_kb_preparation
    elif state == f'{State.VEGETABLE}':
        print(f'{State.VEGETABLE}')
        return inline_kb_vegetable
    elif state == f'{State.DAIRY}':
        return inline_kb_dairy
    elif state == f'{State.STARCH}':
        return inline_kb_starch
    elif state == f'{State.SPICE}':
        return inline_kb_spice
    elif state == f'{State.SWEET}':
        return inline_kb_sweet
