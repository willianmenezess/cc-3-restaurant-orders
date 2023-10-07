from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        dishes = list(self.menu_data.dishes)
        if not restriction:
            filtered_dishes = dishes
        else:
            filtered_dishes = [
                dish
                for dish in dishes
                if restriction not in dish.get_restrictions()
            ]
        list_dish_dict = []
        for filt_dish in filtered_dishes:
            dish_dict = {
                "dish_name": filt_dish.name,
                "ingredients": filt_dish.get_ingredients(),
                "price": filt_dish.price,
                "restrictions": filt_dish.get_restrictions(),
            }
            if self.inventory.check_recipe_availability(filt_dish.recipe):
                list_dish_dict.append(dish_dict)

        return list_dish_dict


if __name__ == "__main__":
    # sem restrição
    menu_builder = MenuBuilder()
    print(menu_builder.get_main_menu())
    # com restrição
    print(menu_builder.get_main_menu("GLUTEN"))
