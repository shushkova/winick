import pandas as pd
import numpy as np

from init_table_info.food_and_wine_types import foodWine


class FoodWineMatches(object):
    """
    Содержит инфоормацию о мэтчах между типом еды и вина
    """

    def __init__(self):
        food_wine = foodWine

        self.wine = food_wine.wine
        self.meat = food_wine.meat
        self.preparation = food_wine.preparation
        self.dairy = food_wine.dairy
        self.vegetable = food_wine.vegetable
        self.spice = food_wine.spice
        self.starch = food_wine.starch
        self.sweet = food_wine.sweet

        self.meat_match = pd.DataFrame([
            [2, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 2, 1, 0, 0, 1, 2, 1],
            [1, 2, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 2, 1, 2, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 0, 0],
            [0, 0, 0, 0, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 2, 1, 0, 1, 0],
            #     [0, 0, 0, 0, 0, 0, 0, 0, 0 ]
        ], index=self.meat, columns=self.wine)

        self.preparation_match = pd.DataFrame([
            [2, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 2, 1, 1, 1, 1, 0, 0],
            [1, 2, 1, 1, 0, 0, 1, 0, 1],
            [2, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 4, 1, 1, 0]
        ], index=self.preparation, columns=self.wine)

        self.dairy_match = pd.DataFrame([
            [0, 1, 4, 1, 4, 1, 1, 1, 1],
            [1, 4, 0, 1, 0, 1, 1, 1, 4],
            [4, 1, 0, 1, 1, 0, 1, 0, 0]
        ], index=self.dairy, columns=self.wine)

        self.vegetable_match = pd.DataFrame([
            [1, 4, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 4, 1, 0, 0],
            [0, 0, 0, 4, 1, 0, 0, 1, 0],
            [1, 4, 0, 1, 0, 0, 0, 1, 0],
            [1, 4, 4, 0, 4, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 4, 0],
            [0, 1, 0, 1, 0, 4, 1, 0, 0]
        ], index=self.vegetable, columns=self.wine)

        self.spice_match = pd.DataFrame([
            [4, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 4, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 4, 0],
            [0, 1, 1, 1, 1, 4, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 4],
            [0, 4, 1, 1, 0, 0, 1, 4, 0]
        ], index=self.spice, columns=self.wine)

        self.starch_match = pd.DataFrame([
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 0, 4, 0],
            [0, 0, 0, 1, 0, 0, 0, 4, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0]
        ], index=self.starch, columns=self.wine)

        self.sweet_match = pd.DataFrame([
            [0, 0, 0, 0, 0, 0, 1, 4, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 4]
        ], index=self.sweet, columns=self.wine)

    def get_category_match(self, category) -> pd.DataFrame:
        return self.__getattribute__(f'{category}_match')

    def return_match(self, category, category_values, wines) -> pd.DataFrame:
        df = self.get_category_match(category).loc[category_values, wines]
        df = df.replace(0, np.nan)
        return df.dropna(how='all', axis=1)

    def get_suitable_items_for_category(self, category, wines):
        df = self.get_category_match(category)[wines]
        df = df.replace(0, np.nan)
        return df.dropna(how='all', axis=0)


foodWineMatches = FoodWineMatches()

if __name__ == '__main__':
    print(foodWineMatches.get_category_match('sweet'))
    print(foodWineMatches.return_match('sweet', ['fruit and berries', 'vanilla and caramel', 'chocolate and coffee'],
                                       ['bold red', 'sweet wine', 'dessert']).columns.values)
    print(foodWineMatches.return_match('sweet', ['chocolate and coffee'],
                                       ['bold red', 'sweet wine', 'dessert']).columns.values)
    print(
        foodWineMatches.get_suitable_items_for_category('sweet', ['bold red', 'sweet wine']).index.values)
