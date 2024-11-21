from dice_roller import dice_roller
import random

def test_dice_roller():
    random.seed(11021073)
    assert dice_roller(6, 3) == 10
