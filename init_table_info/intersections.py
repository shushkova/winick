from user_choice import UserChoice

from .food_and_wine_matches import foodWineMatches
from .food_and_wine_types import foodWine


def get_inter_for_category(category, category_value, wines):
    return foodWineMatches.return_match(category, [category_value], wines).columns.values


def get_intersection(choice: UserChoice):
    wines = foodWine.wine

    for prop in choice.get_properties():
        if choice.get_category_value(prop):
            possible_wines = get_inter_for_category(prop, choice.get_category_value(prop), wines)
            wines = set(wines) & set(possible_wines)
    return wines


def get_suitable(choice: UserChoice, category):
    wines = get_intersection(choice)
    return foodWineMatches.get_suitable_items_for_category(category, wines).index.values
