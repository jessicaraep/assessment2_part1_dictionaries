"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    word_dict = {}
    phrase = phrase
    each_word = phrase.split(" ")

    for word in each_word:
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_name = melon_name.lower()
    price = None

    melons = {}
    melons["watermelon"] = 2.95
    melons["cantaloupe"] = 2.50
    melons["musk"] = 3.25
    melons["christmas"] = 14.25

    if melons.get(melon_name, 0) == 0:   
        return 'No price found'
    else: 
        return melons[melon_name]


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    word_length = {}
    length_word = []

    for word in words:
         length_word.append([len(word), word])

    sorted_length_word = sorted(length_word)

    for item in sorted_length_word:
        word_length[item[0]] = word_length.get(item[0], []) 
        word_length[item[0]].append(item[1])

    return word_length.items()


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
        
    english_pirate = {}
    english_pirate["sir"] = "matey"
    english_pirate["hotel"] = "fleabag inn"
    english_pirate["student"] = "swabbie"
    english_pirate["man"] = "matey"
    english_pirate["professor"] = "foul blaggart"
    english_pirate["restaurant"] = "galley"
    english_pirate["your"] = "yer"
    english_pirate["excuse"] = "arr"
    english_pirate["students"] = "swabbies"
    english_pirate["are"] = "be"
    english_pirate["restroom"] = "head"
    english_pirate["my"] = "me"
    english_pirate["is"] = "be"

    phrase = phrase.lower().split(" ")
    new_phrase = []

    for word in phrase:
        if english_pirate.get(word) == None:
            new_phrase.append(word)
        else:
            new_phrase.append(english_pirate[word])

    return ' '.join(new_phrase)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    output_words = []
    markov = {}
    new_word = None
    current_word = names[0]
    first_word_first_letter = names[0][0]
    output_words.append(current_word)

    for i in range(len(names)-1):
        markov[names[i][0]] = markov.get(names[i][0], [])
        markov[names[i][0]].append(names[i])

    markov[first_word_first_letter].remove(current_word)

    while True:
        if markov[current_word[-1]] == []:
            break
        values = markov[current_word[-1]]
        new_word = values[0]
        markov[current_word[-1]].remove(new_word)
        output_words.append(new_word)
        current_word = new_word

    return output_words

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
