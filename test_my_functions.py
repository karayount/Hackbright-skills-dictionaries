

def adv_sort_by_word_length(words):
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

    return ascending_length


def sort_by_word_length(words):
  # add each word to dictionary, where key = length, value = list of words
    words_with_lengths = {}
    for word in words:
        if len(word) in words_with_lengths:
            words_with_lengths[len(word)].append(word)
        else:
            words_with_lengths[len(word)] = [word]

    # from dictionary, build list with (length, word list) tuples
    ascending_length = []
    for key in words_with_lengths:
        ascending_length.append((key, words_with_lengths[key]))

    return ascending_length


words = ["ok", "an", "apple", "a", "day"]
another_list = ["onomatopoeia", "pastafarianis", "a", "fred"]

print sort_by_word_length(words)
print sorted(sort_by_word_length(another_list))

print adv_sort_by_word_length(words)
print sorted(adv_sort_by_word_length(another_list))
