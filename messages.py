from state import State

# This is WineBot
schema_message = 'Select the categories to which you want to match the wine\n'

init_checkbox_message = 'Select categories'

finish_message = 'Show selected wines?'
fail_finish_message = 'There are no suitable wines for the current selection'

suitable_vine_message = 'Suitable wines: '
processing_text_message = 'Processing the text'
input_text_message = 'Enter the text'

# -----------------------

start_command_message = """
            Hi! I'm your personal wine helper. I can work in two modes.
            
            First, you select the types of prefered dishes and I give you the wine recommendation.
            The second one - you send me a text description of wine and I will give a sutiable situation for it
            (text examples you can get from this chanel : https://t.me/winick_examples)
            
            
            My commands:
            /start - start selecting recommendations
            /help - see help
"""

#         This is WineBot. Outputs a wine recommendation based on gastronomic preferences\n
help_message = """
        I'm your personal helper. Outputs a wine recommendation based on gastronomic preferences\n
        My commands:
        /start - start selecting recommendations
        /help  - see help"""
select_mode_message = 'Select the mode'
all_cat_message = 'Are you done with choosing categories?'

Message = {
    'start_command': start_command_message,
    'help': help_message,
    'select_mode': select_mode_message,
    'all_cat': all_cat_message,

    'schema': schema_message,
    'init_checkbox': init_checkbox_message,
    'finish': finish_message,
    'fail_finish': fail_finish_message,
    'suitable_vine': suitable_vine_message,
    'processing_text': processing_text_message,
    'input_text': input_text_message,

    f'{State.MEAT}': 'Choose meat',
    f'{State.PREPARATION}': 'Choose preparation',
    f'{State.STARCH}': 'Choose starch',
    f'{State.SPICE}': 'Choose spice',
    f'{State.SWEET}': 'Choose sweet',
    f'{State.VEGETABLE}': 'Choose vegetables',
    f'{State.DAIRY}': 'Choose dairy',
}
