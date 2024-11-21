from math import factorial
from anagrams import anagrams_it


def test_anagrams_it():
    assert anagrams_it('BAB') == {'ABB', 'BAB', 'BBA'}
    assert len(anagrams_it('REEVES')) == factorial(6) // factorial(3)
    assert len(anagrams_it('MISSISSIPPI')) == factorial(11) // (factorial(4) * factorial(4) * factorial(2))
