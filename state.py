from aiogram.utils.helper import Helper, HelperMode, Item


class State(Helper):
    mode = HelperMode.snake_case

    INIT = Item()

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


choose_dishes = [State.INIT, State.MEAT, State.PREPARATION, State.VEGETABLE,
                 State.STARCH, State.DAIRY, State.SPICE, State.SWEET, State.PRE_FINAL_STATE]
