import random

def dice_roller(n_sides, num_dice):
    """
    roll several dice and add up the score
    Parameters
    ----------
    n_sides
    num_dice

    Returns
    -------

    """
    score = sum(random.randint(1, n_sides) for i in range(num_dice))
    return score
