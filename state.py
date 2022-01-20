from aiogram.utils.helper import Helper, HelperMode, Item


class State(Helper):
    mode = HelperMode.snake_case

    INIT = Item()

    TEXT = Item()

    SCHEMA = Item()
    MEAT = Item()
    PREPARATION = Item()
    VEGETABLE = Item()
    STARCH = Item()
    DAIRY = Item()
    SPICE = Item()
    SWEET = Item()

    PRE_FINAL_STATE = Item()
    FINAL_STATE = Item()

    FINISH = Item()

    NOTHING = Item()


choose_dishes = [State.SCHEMA, State.MEAT, State.PREPARATION, State.VEGETABLE,
                 State.STARCH, State.DAIRY, State.SPICE, State.SWEET, State.PRE_FINAL_STATE]
