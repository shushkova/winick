from aiogram.dispatcher.filters.state import StatesGroup, State as StateG
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ChatEvent, Window, Dialog, DialogRegistry, StartMode
from aiogram_dialog.widgets.kbd import Checkbox, ManagedCheckboxAdapter, Button
from aiogram_dialog.widgets.text import Const

#
import callback_query_handler
from messages import Message

from state import State

order = {}
base_types = {
    f'{State.MEAT}': False,
    f'{State.PREPARATION}': False,
    f'{State.DAIRY}': False,
    f'{State.VEGETABLE}': False,
    f'{State.SPICE}': False,
    f'{State.STARCH}': False,
    f'{State.SWEET}': False,
    f'{State.PRE_FINAL_STATE}': True,
    f'{State.FINAL_STATE}': True
}


class Initial_checkbox(StatesGroup):
    main = StateG()
    button = StateG()


async def init_order(user_id):
    order[user_id] = base_types.copy()


def change_type(user_id, type, is_checked):
    order[user_id][type] = is_checked
    if type == f'{State.MEAT}':
        order[user_id][f'{State.PREPARATION}'] = is_checked


async def check_changed(event: ChatEvent, checkbox: ManagedCheckboxAdapter, manager: DialogManager):
    user_id = event.from_user.id
    change_type(user_id, checkbox.widget.widget_id, checkbox.is_checked(manager))


def create_checkbox(name, id):
    return Checkbox(
        Const(f'{name}'),
        Const(f'✓  {name}'),
        id=id,
        default=True,  # so it will be checked by default,
        on_state_changed=check_changed,
    )


async def go_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    await c.message.answer("Going on!")


dialog = Dialog(
    Window(
        Const(Message['init_checkbox']),
        create_checkbox('Meat', State.MEAT),
        create_checkbox('Dairy', State.DAIRY),
        create_checkbox('Vegetable', State.VEGETABLE),
        create_checkbox('Spice', State.SPICE),
        create_checkbox('Starch', State.STARCH),
        create_checkbox('Sweet', State.SWEET),
        state=Initial_checkbox.main,  # state is used to identify window between dialogs
    )
)
