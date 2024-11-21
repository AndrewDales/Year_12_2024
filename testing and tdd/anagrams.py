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



def anagrams_it(initial_word):
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
    anagrams_ = anagrams_it("ADAM")
    print(anagrams_)
