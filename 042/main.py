"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

tri_nums = []


def add_tri_num():
    n = len(tri_nums) + 1
    num = n * (n+1) / 2
    tri_nums.append(num)


def word_score(word):
    letter_list = [ord(c) for c in word]
    letter_score = [c - ord("A") + 1 for c in letter_list]
    return sum(letter_score)


with open("p042_words.txt", mode="r") as f:
    contents = f.read()
    word_list = contents.replace('"', '')
    word_list = word_list.split(",")


scores = [word_score(word) for word in word_list]
while max(tri_nums, default=0) < max(scores):
    add_tri_num()

tri_words = [score for score in scores if score in tri_nums]
ans = len(tri_words)

print(f"ans == {ans}")


