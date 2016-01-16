"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # create dictionary with character keys and appearances (int) value
    working_string = input_string
    character_appearances = {}
    for index in range(len(working_string)):
        # ignore endline and space characters
        if working_string[index] != "\n" and working_string[index] != " ":
            if working_string[index] in character_appearances:
                character_appearances[working_string[index]] += 1
            else:
                character_appearances[working_string[index]] = 1

    # most common letter has "how_common" appearances
    how_common = max(character_appearances.values())
    most_common = []

    # find all letters with max appearances, add to list
    for char in character_appearances:
        if character_appearances[char] == how_common:
            most_common.append(char)

    # sort list alphabetically in case it has > 1 element
    return sorted(most_common)


# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
# [Kara] The above comment works for given input, see comment below
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
    # add each word to dictionary, where key = length, value = list of words
    words_with_lengths = {}
    for word in words:
        if len(word) in words_with_lengths:
            words_with_lengths[len(word)].append(word)
        else:
            words_with_lengths[len(word)] = [word]

    # loop through dictionary, sorting each value
    for word_length in words_with_lengths:
        words_with_lengths[word_length].sort()

    # from dictionary, build list with (length, word list) tuples
    ascending_length = []
    for key in words_with_lengths:
        ascending_length.append((key, words_with_lengths[key]))

    # interestingly, without sorting ascending_length, the test passed, and I
    #   didn't get a failure until I tested with a word longer than 12 letters.
    #   Research and discussion with Software Engineer Husband led me to believe
    #   this is related to the way dictionaries are implemented.
    return sorted(ascending_length)


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
