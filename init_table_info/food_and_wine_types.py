class FoodWine(object):
    """
    Доступные для выбора типы еды, а также возможные типы вин
    """

    def __init__(self):
        self.wine = [
            'bold red', 'medium red', 'light red', 'rose', 'rich wine', 'light white',
            'sparkling', 'sweet wine', 'dessert'
        ]
        self.meat = ['red meat', 'cured meat', 'fork', 'poultry', 'mollusk', 'fish', 'lobster']
        self.preparation = ['grilled', 'sauted or fired', 'smoked', 'roasted', 'steamed']
        self.dairy = ['soft cheese', 'pungent cheese', 'hard cheese']
        self.vegetable = [
            'alliums', 'green vegetables', 'root vegetables', 'nightshades', 'funghi', 'nuts and seeds', 'bean and peas'
        ]
        self.spice = [
            'black pepper', 'red pepper', 'hot and spicy', 'herbs', 'backing spices', 'exotic and aromatic spices'
        ]
        self.starch = ['white starches', 'whole wheat grains', 'sweet starchy vegetables', 'potato']
        self.sweet = ['fruit and berries', 'vanilla and caramel', 'chocolate and coffee']

    def return_options(self, dish_name: str):
        return getattr(self, dish_name)


foodWine = FoodWine()
