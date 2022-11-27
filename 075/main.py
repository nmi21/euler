"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle
in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other
lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three
different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle
triangle be formed?

---

Method:
- Use Euclid's formula to determine the primitive pythagorean triple solution to the Diophantine equation
    - cycle through values of m and n to find values for a, b, and c
    - sum a, b, and c to find the length L, and add the tuple (a, b, c) to a list of tuples in a dictionary with key L
    - for every (a, b, c), get k*(a, b, c) to get all other triples related to the primitive set
- to get the limit of searching...
    - we know that the longest side, c, is given by m^2 + n^2
    - since m > n, we know letting m == n gives us superfluous search terms
    - thus if we say c == LIMIT and m == n, we can find that
            c = m^2 + n^2
        LIMIT = m^2 + n^2
        LIMIT = m^2 + m^2
        LIMIT = 2*m^2
          m^2 = LIMIT / 2
            m = sqrt(LIMIT/2)
    this should provide a maximum value for m
- "Every primitive triple arises (after the exchange of a and b, if a is even) from a unique pair of coprime numbers m,
n, one of which is even."
    - since coprime, only one of m and n can be even
    - thus, can skip if m + n is even

"""

import math

LIMIT = 1500000
L_dict = {}

# Euclid's formula is valid for m > n > 0
for m in range(2, int(math.sqrt(LIMIT / 2)) + 1):
    # print(f"m == {m}")
    for n in range(1, m):

        # skip instance if both are even or both are odd
        # skip instance if not coprime
        if m + n % 2 == 0 or math.gcd(m, n) != 1:
            continue

        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        perimeter = a + b + c

        if perimeter > LIMIT:
            continue

        sides = [min(a, b), max(a, b), c]

        for k in range(1, (LIMIT // perimeter) + 1):

            k_sides = [k * x for x in sides]
            k_perimeter = k * perimeter

            if k_perimeter not in L_dict:
                L_dict[k_perimeter] = []

            if k_sides not in L_dict[k_perimeter]:
                L_dict[k_perimeter].append(k_sides)

# count all instances where there is only 1 item in the list
counter = 0
for key in L_dict:
    if len(L_dict[key]) == 1:
        counter += 1

ans = counter
print(f"ans == {ans}")
