"""
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that
211 = 2048 < 37 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three
million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

---

Method:
- use logarithms since they will maintain <, >, == relationships
- if the typical line is supposed to be calculated as A ^ B, we can take the log10 of that and compute as follows:
    A ^ B
    log10(A ^ B)
    B * log10(A)
- these numbers should be within a range that we can calculate
"""

import math


with open(file="p099_base_exp.txt", mode="r") as f:
    data = f.read().splitlines()


pairs = [d.split(",") for d in data]
# convert to ints
pairs = [[int(x[0]), int(x[1])] for x in pairs]

res = [x[1] * math.log10(x[0]) for x in pairs]

# add 1 to adjust for 0 index
ans = res.index(max(res)) + 1
print(f"ans == {ans}")
