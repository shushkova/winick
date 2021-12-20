from state import State

help_message = ''
start_message = 'Привет! Это WineBot. Выберите категории, к которым необходимо подобрать вино\n\n' + help_message

init_checkbox_message = 'Выберите категории'

finish_message = 'Показать подобранные вина?'
fail_finish_message = 'Для текущего выбора нет подходящих вин'

Message = {
    'new_user': start_message,
    'init_checkbox': init_checkbox_message,
    'finish': finish_message,
    'fail_finish': fail_finish_message,

    f'{State.MEAT}': 'Выберите основное блюдо',
    f'{State.PREPARATION}': 'Выберите тип приготовления',
    f'{State.STARCH}': 'Выберите цельнозлаквые',
    f'{State.SPICE}': 'Выберите специи',
    f'{State.SWEET}': 'Выберите дессерт',
    f'{State.VEGETABLE}': 'Выберите овощи',
    f'{State.DAIRY}': 'Выберите молочные продукты',
}
