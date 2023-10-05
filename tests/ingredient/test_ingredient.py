from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
# from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    """Teste da Classe Ingredient (ingredient.py)"""
    ingredient_1 = Ingredient("ovo")
    ingredient_2 = Ingredient("ovo")
    ingredient_3 = Ingredient("carne")
# teste passa com a implementação correta da classe Ingredient
    assert ingredient_1 == ingredient_2
    assert ingredient_1 != ingredient_3
    assert ingredient_1.name == "ovo"

# teste falha se a classe retorna hashes diferentes p/ ingredientes iguais
    assert hash(ingredient_1) == hash(ingredient_2)
    assert hash(ingredient_1) != hash(ingredient_3)


# teste falha se a comparação de igualdade de dois ingred iguais seja False
    assert ingredient_1 == ingredient_2

# teste falha se a comparação de iguald de dois ingred diferentes seja True
    assert ingredient_1 != ingredient_3

# Garante que o atributo "restrictions" é preenchido corretamente
    assert len(ingredient_1.restrictions) == 1

#  teste falha caso o método __repr__ retorne um valor inadequado
    assert repr(ingredient_1) == "Ingredient('ovo')"
    assert repr(ingredient_3) == "Ingredient('carne')"
