"""
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number:
1296 = 36^2.

What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number:
9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not
permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.

---
Method:
- we know that the largest square number will have the most digits
    - so start with the most digits and work toward fewer digits
    - compare everything within the same number of digits and determine the max
    - if a max is found, we can exit (because the next one with fewer digits will not be larger)
- starting with a list of all words of a length, L, find all anagram pairs
- get a set of squares with the same number of digits as L
- for each anagram pair, get the relative indices for the second in the pair
- compare against each square and generate a new number based on the indices from above
- if that new number is in the list, verify that the anagram fits the unique letter rule and add to a list
- find the max value of the values generated
"""
import math


def is_anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()
    return str1_list == str2_list


def get_squares(num_digits):
    base_min = math.ceil(10 ** (0.5 * (num_digits - 1)))
    base_max = math.ceil(10 ** (0.5 * num_digits)) - 1
    return [x ** 2 for x in range(base_min, base_max + 1)]


def get_anagram_indices(str1, str2):
    """
    Takes in 2 strings that are anagrams and returns the indices of string 2 in terms of string

    For example, if
        str1 == EAST
        str2 == SEAT
    EAST will have the following assignments for letters:
        E == 0
        A == 1
        S == 2
        T == 3
    Thus, SEAT will return
        S --> 2
        E --> 0
        A --> 1
        T --> 3
    """
    if not is_anagram(str1, str2):
        return None
    str2_indices = []
    for letter in str2:
        str2_indices.append(str1.index(letter))
    return str2_indices


def generate_anagram_from_indices(str1, indices):
    str2 = ""
    for ind in indices:
        str2 += str1[ind]
    return str2


def find_number_anagrams(anagram_list):
    """
    Takes in a list of anagrams and returns a dictionary of all anagram number squares that are possible with the same
    anagram order as the anagram pair.
    """

    def verify_anagram(indices, num1, num2):
        return indices == get_anagram_indices(num1, num2)

    anagram_dict = {}

    # for an anagram , search the list of squares and add all anagrams that exist in the same order as the pair
    # generate a list of squares based on digit length
    squares = get_squares(len(anagram_list[0][0]))
    squares_str = [str(x) for x in squares]

    for anagram_pair in anagram_list:
        # get the index list from the anagram pair
        indices = get_anagram_indices(anagram_pair[0], anagram_pair[1])

        num_anagrams = []
        # check against all the squares, generate the new number, and add it to a list if the number anagram exists
        for i in range(len(squares_str) - 1):
            num = squares_str[i]
            new_num = generate_anagram_from_indices(num, indices)
            if (new_num in squares_str[(i+1):]) and verify_anagram(indices, num, new_num):
                num_anagrams.append((int(num), int(new_num)))

        # if there exist number anagram pairs matching the word anagram pairs, add it to a dictionary
        if len(num_anagrams) > 0:
            anagram_dict[anagram_pair] = num_anagrams

    return anagram_dict


with open(file="p098_words.txt", mode="r") as f:
    data = f.read()
    data = data.replace('"', '')
    data = data.split(",")

largest_square = None
word_lengths = [len(x) for x in data]
word_length = max(word_lengths)
while word_length > 0:
    print(word_length)

    # extract words only of a certain length
    words = [x for x in data if len(x) == word_length]

    # determine anagram pairs
    anagrams = []
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagrams.append((words[i], words[j]))
    print(anagrams)

    # get all possible number combinations associated with the anagram pairs
    anagram_dict = {}
    if len(anagrams) > 0:
        anagram_dict = find_number_anagrams(anagrams)
        # print(anagram_dict)

    anagram_values = []
    if len(anagram_dict) > 0:
        # grab all the values and then flatten out the lists such that it is just the values
        anagram_values = list(anagram_dict.values())
        flat_tups = [item for sublist in anagram_values for item in sublist]
        flat_values = [item for sublist in flat_tups for item in sublist]
        largest_square = max(flat_values)
        print(anagram_dict)

        # finish the while loop early
        # break

    # look to the next smallest word length
    print()
    word_length -= 1

ans = largest_square
print(f"ans == {ans}")
