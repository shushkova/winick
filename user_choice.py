class UserChoice(object):
    def __init__(self):
        self.meat = None
        self.preparation = None
        self.dairy = None
        self.vegetable = None
        self.spice = None
        self.starch = None
        self.sweet = None

    def __str__(self):
        return f'UserChoice( meat: {self.meat}, preparation: {self.preparation}, dairy: {self.dairy}, ' \
               f'vegetable: {self.vegetable}, spice: {self.spice}, starch: {self.starch}, ' \
               f'sweet: {self.meat}, sweet: {self.meat})'

    def set(self, dish_type, value):
        setattr(self, dish_type, value)

    def get_category_value(self, category):
        return self.__getattribute__(category)

    def get_properties(self):
        return [i for i in self.__dict__.keys() if i[:1] != '_']
