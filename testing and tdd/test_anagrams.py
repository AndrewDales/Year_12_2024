from math import factorial
from anagrams import add_one_letter, anagrams, anagrams_it, anagrams_it_comp


def test_add_one_letter():
    assert add_one_letter(('ab', 'cd')) == {('cab', 'd'),
                                            ('acb', 'd'),
                                            ('abc', 'd'),
                                            ('dab', 'c'),
                                            ('adb', 'c'),
                                            ('abd', 'c'),
                                            }


def test_anagrams_it():
    assert anagrams_it('BAB') == {'ABB', 'BAB', 'BBA'}
    assert len(anagrams_it('REEVES')) == factorial(6) // factorial(3)
    assert len(anagrams_it('MISSISSIPPI')) == factorial(11) // (factorial(4) * factorial(4) * factorial(2))


def test_anagrams_it_comp():
    assert anagrams_it_comp('BAB') == {'ABB', 'BAB', 'BBA'}
    assert len(anagrams_it_comp('REEVES')) == factorial(6) // factorial(3)
    assert len(anagrams_it_comp('MISSISSIPPI')) == factorial(11) // (factorial(4) * factorial(4) * factorial(2))


def test_anagrams():
    assert anagrams('BAB') == {'ABB', 'BAB', 'BBA'}
    assert len(anagrams('REEVES')) == factorial(6) // factorial(3)
    assert len(anagrams('MISSISSIPPI')) == factorial(11) // (factorial(4) * factorial(4) * factorial(2))