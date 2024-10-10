def anagrams(word):
    if len(word) == 1:
        anagram_set = {word}
    else:
        first_letter, rest = word[0], word[1:]
        existing_words = anagrams(rest)

        anagram_set = {word[:i] + first_letter + word[i:]
                       for word in existing_words
                       for i in range(len(word) + 1)}
    return anagram_set


def add_one_letter(letter_tuple: tuple[str, str]):
    new_tuples = set()
    current_word, unused_letters = letter_tuple
    for i, letter in enumerate(unused_letters):
        new_unused_letters = unused_letters[:i] + unused_letters[i + 1:]
        for j in range(len(current_word) + 1):
            new_word = current_word[:j] + letter + current_word[j:]
            new_tuples.add((new_word, new_unused_letters))
    return new_tuples


def anagrams_it_old(initial_word):
    current_set = {('', initial_word)}
    for _ in range(1, len(initial_word) + 1):
        new_set = set()
        for word_tuple in current_set:
            new_set |= add_one_letter(word_tuple)
        current_set = new_set
    anagram_set = {word_tuple[0] for word_tuple in current_set}
    return anagram_set


def anagrams_it(initial_word):
    current_set = {''}
    for letter in initial_word:
        new_set = set()
        for word in current_set:
            for j in range(len(word) + 1):
                new_set.add(word[:j] + letter + word[j:])
        current_set = new_set
    return current_set

def anagrams_it_comp(initial_word):
    current_set = {''}

    for letter in initial_word:
        new_set = {word[:j] + letter + word[j:]
                   for word in current_set
                   for j in range(len(word) + 1)
                   }
        current_set = new_set
    return current_set


if __name__ == "__main__":
    # add_one_letter(('ab', 'cd'))
    anagrams_ = anagrams_it_comp("ADAM")
    print(anagrams_)
