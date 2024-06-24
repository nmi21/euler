"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for
Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
"halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the
password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The
balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original
text.

---
Knowns:
- we know that the encryption key, k, adheres to the following:
    'aaa' <= k <= 'zzz'
- the key repeats mod the len of the key if the key length is shorter than the string

Assumptions:
- we can assume that we are only using valid characters for this message
    - thus, looking at an ASCII table (https://www.asciitable.com/) we can limit valid characters to the following:
        - min == ASCII(32) == 'Space'
        - max == ASCII(125) == '}'
    - this min/max includes all upper and lower case English alphabet letters

"""

from itertools import product


def xor_converter(user_in, key):
    """
    :param user_in: a list of ints that are ASCII associated
    :param key: a string of anything length
    :return: xor return of user_in after repeating the key
    """

    # TODO convert user in to a list of ints
    # TODO convert key to a list of ints

    key = [ord(x) for x in key]
    res = [user_in[ind] ^ key[ind % len(key)] for ind, ele in enumerate(user_in)]
    return res


with open(file="p059_cipher.txt", mode="r") as f:
    letters = f.read().split(",")

encrypted_ints = [int(x) for x in letters]
# encrypted_chars = [chr(x) for x in encrypted_ints]
# encrypted_str = ''.join(encrypted_chars)

# get all available ints for ok ASCII chars
valid_ints = []
for i in range(ord(' '), ord('@')+1):
    valid_ints.append(i)
for i in range(ord('a'), ord('z')+1):
    valid_ints.append(i)
for i in range(ord('A'), ord('Z')+1):
    valid_ints.append(i)
valid_ints.append(ord('['))
valid_ints.append(ord(']'))
valid_ints.append(ord('{'))
valid_ints.append(ord('}'))
valid_ints.append(ord('^'))
valid_ints.sort()
# print(valid_ints)


valid_keys = []
for a, b, c in product(range(ord('a'), ord('z') + 1), repeat=3):
    s_key = chr(a) + chr(b) + chr(c)
    decrypted_ints = xor_converter(encrypted_ints, s_key)

    if all(x in valid_ints for x in decrypted_ints):
        valid_keys.append(s_key)

# print(valid_keys)
valid_key = valid_keys[0]

# decrypted_chars = [chr(x) for x in xor_converter(encrypted_ints, valid_key)]
# decrypted_str = "".join(decrypted_chars)
# print(decrypted_str)

ans = sum(xor_converter(encrypted_ints, valid_key))
print(f"ans == {ans}")
