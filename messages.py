from state import State

#         This is WineBot. Outputs a wine recommendation based on gastronomic preferences\n
help_message = """
        I'm your personal helper. Outputs a wine recommendation based on gastronomic preferences\n
        My commands:
        /start - start selecting recommendations
        /help  - see help"""
# This is WineBot
schema_message = 'Hi! I\'m your personal helper. Select the categories to which you want to match the wine\n\n' + help_message

init_checkbox_message = 'Select categories'

finish_message = 'Show selected wines?'
fail_finish_message = 'There are no suitable wines for the current selection'

choose_message = 'Choose what\'s next'
suitable_vine_message = 'Suitable wines: '
processing_text_message = 'Processing the text'
input_text_message = 'Enter the text'
all_cat_message = 'Are all categories selected?'

Message = {
    'schema': schema_message,
    'init_checkbox': init_checkbox_message,
    'finish': finish_message,
    'fail_finish': fail_finish_message,
    'help': help_message,
    'suitable_vine': suitable_vine_message,
    'processing_text': processing_text_message,
    'choose': choose_message,
    'input_text': input_text_message,
    'all_cat': all_cat_message,

    f'{State.MEAT}': 'Choose meat',
    f'{State.PREPARATION}': 'Choose preparation',
    f'{State.STARCH}': 'Choose starch',
    f'{State.SPICE}': 'Choose spice',
    f'{State.SWEET}': 'Choose sweet',
    f'{State.VEGETABLE}': 'Choose vegetables',
    f'{State.DAIRY}': 'Choose dairy',
}
