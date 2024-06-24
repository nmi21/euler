"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For
example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
possible secret passcode of unknown length.

---
Method:
- you can determine which numbers must come before others by storing them in a list (or set) with the key being the
last number seen
    - for example, if you have an entry 317 (from the example in the prompt):
        - you could have a dictionary with the following structure
            {
                7: {1, 3}
                1: {3}
                3: {}
            }
    - now, if the next successful entry was 518, the dictionary would like this:
            {
                7: {1, 3, 5}
                1: {3, 5}
                3: {}
                8: {1, 5}
                5: {}
            }
    - going through all entries, you would expect that the dictionary would like the following (formatted for
    readability here):
            {
                5: {},
                3: {5},
                1: {5, 3},
                2: {5, 3, 1},
                7: {5, 3, 1, 2},
                8: {5, 3, 1, 2, 7}
            }
    - from this, we can determine that 5 has no priors, and therefore must be first
        - passcode == 5_
    - after that, we can eliminate 5 from all existing sets
    - we will then note that 3 has no priors remaining, and therefore must be next
        - passcode == 53_
    - continuing on this pattern, we will find that the passcode == 531278

"""
import time
t = time.time()


def add_set_to_priors_dict(priors_dict, dict_key, list_of_priors):
    """
    function that will take in a priors_dict, a key, and a set. It will add elements from priors_set to priors_dict at
    key "dict_key". If the key does not exist, one will be created.
    """
    if dict_key in priors_dict:
        priors_dict[dict_key] += list_of_priors
    else:
        priors_dict[dict_key] = list_of_priors

    return priors_dict


def fill_dict_with_priors(priors_dict, code_entry):
    """
    function that will take in a data entry and a dictionary of priors and fill the dictionary with the priors from
    the entry
    """
    for i in range(len(code_entry)):
        key = code_entry[i]
        priors_list = [x for x in code_entry[:i]]
        priors_dict = add_set_to_priors_dict(priors_dict, key, priors_list)

    return priors_dict


def generate_passcode(priors_dict):
    passcode = ""

    while len(priors_dict) > 0:
        for key in priors_dict:
            if priors_dict[key] == set():
                next_char = key
        passcode += next_char
        priors_dict.pop(next_char)
        for k in priors_dict:
            priors_dict[k].discard(next_char)

    return passcode


def solve():
    # open the file and extract all entries
    with open(file="p079_keylog.txt", mode="r") as f:
        data = f.read().splitlines()

    # create a dictionary with priors and give each prior under each key
    priors = {}
    for entry in data:
        priors = fill_dict_with_priors(priors, entry)

    # convert lists to sets
    for key in priors:
        priors[key] = set(priors[key])

    passcode = generate_passcode(priors)

    return passcode


ans = solve()
print(ans)
print(f"{time.time() - t} sec")
