"""
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though
the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular
number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

---
Method:
For each line in the file, do the following:
- convert the number from Roman numerals to base10
- convert that number from base 10 into smallest version of Roman numerals
- compare the lengths of the original vs the double convert

Then, add the difference from each line.
"""
import time
t = time.time()

# convert from base 10 to roman numeral
def convert_to_roman_numerals(num: int):
    """
        output a string that contains a valid minimal Roman numeral
        """

    thousands = num // 1000
    hundreds = (num // 100) % 10
    tens = (num // 10) % 10
    ones = int(str(num)[-1])

    # initialize output string, out
    out = ""

    # deal with thousands
    out += 'M' * thousands

    # deal with hundreds
    if 0 <= hundreds <= 3:
        out += 'C' * hundreds
    elif hundreds == 4:
        out += 'CD'
    elif 5 <= hundreds <= 8:
        out += 'D' + 'C'*(hundreds - 5)
    else:
        out += 'DM'

    # deal with tens
    if 0 <= tens <= 3:
        out += 'X' * tens
    elif tens == 4:
        out += 'XL'
    elif 5 <= tens <= 8:
        out += 'L' + 'X'*(tens - 5)
    else:
        out += 'XC'

    # deal with ones
    if 0 <= ones <= 3:
        out += 'I' * ones
    elif ones == 4:
        out += 'IV'
    elif 5 <= ones <= 8:
        out += 'V' + 'I' * (ones - 5)
    else:
        out += 'IX'

    # ones_list = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    # tens_list = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    # hundreds_list = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    # thousands_list = ['', 'M', 'MM', 'MMM', 'MMMM']
    # numerals_list = [ones_list, tens_list, hundreds_list, thousands_list]
    #
    # # create a list of the numbers in position starting at ones, then tens, etc
    # num_list = [int(x) for x in list(str(num))]
    # num_list.reverse()
    #
    # out = ""
    # for i in range(len(num_list)):
    #     out = numerals_list[i][num_list[i]] + out

    return out


# convert each line to base 10
def convert_to_base10(roman_num: str):

    """
    look in your string for 6 different combinations
        CM CD XL XC IV IX
    take each of those a value and remove them from the string
    go through your string and multiply each letter by its value and add that together
    add the value of the fancy strings
    """

    subtracted_nums = {
        "CM": 900,
        "CD": 400,
        "XL": 40,
        "XC": 90,
        "IV": 4,
        "IX": 9
    }

    standard_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    out = 0

    for s in subtracted_nums:
        if s in roman_num:
            out += subtracted_nums[s]
            roman_num = roman_num.replace(s, "")

    for n in standard_nums:
        if n in roman_num:
            out += standard_nums[n] * roman_num.count(n)
            roman_num = roman_num.replace(n, "")

    return out


# compare length of strings
def compare_lengths(roman1, roman2):
    return abs(len(roman1) - len(roman2))


def solve():
    # read the file line by line
    with open(file="p089_roman.txt", mode="r") as f:
        data = f.read().splitlines()

    sum = 0
    for d in data:
        sum += compare_lengths(d, convert_to_roman_numerals(convert_to_base10(d)))

    return sum


ans = solve()
print(ans)
print(time.time() - t)
