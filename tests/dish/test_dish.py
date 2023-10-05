from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    '''Teste da Classe Dish (dish.py)'''
    ovo = Ingredient('ovo')
    carne = Ingredient('carne')
    camarao = Ingredient('camarão')

    prato_1 = Dish('omelete', 10.0)  # prato de ovo + carne
    prato_1.add_ingredient_dependency(ovo, 3)
    prato_1.add_ingredient_dependency(carne, 2)

    prato_2 = Dish('carmarão', 20.0)  # prato de carne + camarão
    prato_2.add_ingredient_dependency(camarao, 5)
    prato_2.add_ingredient_dependency(carne, 2)

    prato_3 = Dish('omelete', 10.0)  # prato de ovo + carne
    prato_3.add_ingredient_dependency(ovo, 3)
    prato_3.add_ingredient_dependency(carne, 2)

# a classe pode ser instanciada corretamente com a assinatura esperada
    assert prato_1.name == 'omelete'
    assert prato_1.price == 10.0
    assert prato_1 == prato_3

# os métodos mágicos funcionam conforme esperado
    assert repr(prato_1) == "Dish('omelete', R$10.00)"
    assert prato_1.__eq__(prato_2) is False
    assert hash(prato_1) != hash(prato_2)
    assert hash(prato_1) == hash(prato_3)
    assert prato_1.recipe == {ovo: 3, carne: 2}
    assert len(prato_1.get_restrictions()) == 2
    assert len(prato_1.get_ingredients()) == 2
    with pytest.raises(
        ValueError, match='Dish price must be greater then zero.'
    ):
        Dish('omelete', 0)
    with pytest.raises(TypeError, match='Dish price must be float.'):
        Dish('peixe com carne', 'farofa')
