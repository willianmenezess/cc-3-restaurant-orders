# from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print('Linha CSV: ', row)
                instance_dish = Dish(row["dish"], float(row["price"]))
                if instance_dish not in self.dishes:
                    instance_dish.add_ingredient_dependency(
                        Ingredient(row["ingredient"]),
                        int(row["recipe_amount"]),
                    )
                    self.dishes.add(instance_dish)
                else:
                    for dish in self.dishes:
                        if dish == instance_dish:
                            dish.add_ingredient_dependency(
                                Ingredient(row["ingredient"]),
                                int(row["recipe_amount"]),
                            )


if __name__ == "__main__":
    menu_data = MenuData("tests/mocks/menu_base_data.csv")
    print(menu_data)
    print('Pratos do menu:', menu_data.dishes)
    # ingredientes do prato 0
    print(list(menu_data.dishes)[0].recipe)
    # ingredientes do prato 1
    print(list(menu_data.dishes)[1].recipe)
