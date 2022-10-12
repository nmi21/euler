"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""

num_dict = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

# count letters in a word
def letter_count(word):
    word_list = [len(x) for x in word.split()]
    return sum(word_list)


# map from integer to word
def num_to_word(num_list):
    if len(num_list) > 1:
        num_list[1] *= 10
        teen_check = num_list[1] + num_list[0]
        if (teen_check > 10) and (teen_check < 20):
            num_list[1] = teen_check
            num_list[0] = 0
    word_list = [num_dict[x] for x in num_list]
    if len(word_list) > 2:
        if word_list[2]:
            word_list[2] += " hundred"
        if len(word_list[0]) > 0 or len(word_list[1]) > 0:
            word_list[2] += " and"
    if len(word_list) > 3:
        word_list[3] += " thousand"
    word_list.reverse()
    word = ""
    for x in word_list:
        if x:
            word += x + " "
    return word[:-1]


def num_split(num):
    num_size = len(str(num))
    num_list = []
    for exp in range(num_size):
        num_list.append(num // pow(10, exp) % 10)
    return num_list


def num_to_count(num):
    return letter_count(num_to_word(num_split(num)))


stop = 1000
count_list = [num_to_count(x) for x in range(1, stop + 1)]
ans = sum(count_list)
print(ans)

# start = 999
# stop = 1000
# for num in range(start, stop + 1):
#     print(num_to_word(num_split(num)))
#     print(num_to_count(num))
#
#
# num = 1000
# print(num_split(num))
# print(num_to_word(num_split(num)))

