"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    no_duplicates = set(words)
    return list(no_duplicates)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    item_set_1 = set(items1)
    item_set_2 = set(items2)
    return list(item_set_1 & item_set_2)

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    # stores a set of numbers, which removes duplicate numbers even if they are
    # negative numbers, and then stores those numbers as a list in a variable
    unique_numbers = list(set(numbers))
    # The goal is to find a pair of numbers that sums to zero. This variable is
    # set to zero fo the equation in the while loop.
    sum_to_zero = 0
    # This sets an empty list to be appended to later.
    total = []

    while unique_numbers:
        # removes a number from the unique_numbers list & stores it in variable
        number = unique_numbers.pop()
        # subtracts the number above from 0 and stores it in a variable.
        difference = sum_to_zero - number
        # if that number is in the unique_number list, add it to the total list
        if difference in unique_numbers:
            total.append([number, difference])
        # if the number is zero, include it as well!
        elif number == 0:
            total.append([0, 0])
    return total



def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    #sets an empty dictionary to set letters as keys and counts as values
    letter_counts = {}
    #sets an empty list for the final result of the function
    result = []
    # This for loop checks whether a character is in the dictionary. If the 
    # character is not in the dictionary, it adds the character as a key and adds
    # one (1) as its value. If the character is already a key in the dictionary,
    # it updates the value count by adding one.
    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    # deletes the space key in the letter_counts dictionary
    del letter_counts[" "]
    # sorts the values of the sorted_counts dictionary in numerical order, from
    # least to greatest and stores them in the variable "sorted_values"
    sorted_values = sorted(letter_counts.values())
    # determines whether there is a tie by taking the last (greatest) number 
    # from the variable, sorted_values, and counts how many times it appears in 
    # the sorted_values list and stores that number in the variable 
    # number_of_largest
    number_of_largest = sorted_values.count(sorted_values[-1])
    # stores all the keys and their associated values in the variable tuples
    tuples = letter_counts.items()
    # sorts the tuples in the variable tuples by the second item in the tuple, 
    # from greatest to least and stores them in sorted_tuples
    sorted_tuples = sorted(tuples, key = lambda a:-a[1])
    # stores the tuple(s) with the letter(s) that appear most frequently in the
    # phrase in a variable
    largest_tuples = sorted_tuples[:number_of_largest]
    # unpacks the key(s) (the letter(s)) with the highest count(s) and adds them
    # to the empty list, result
    for item in largest_tuples:
        result.append(item[0])
    #returns the result
    return result



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
