"""
The square root of 2 can be written as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + (1 / 2 + (1 / 2 + ...)))

The infinite continued fraction can be written, sqrt(2) = [1; (2)], (2) indicates that 2 repeats ad infinitum.

In a similar way, sqrt(23) = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational
approximations.

Let us consider the convergents for sqrt(2).

1 = 1
1 + 1/2 = 3/2
1 + 1/(2+1/2) = 7/5
1 + 1/(2+1(2+1/2)) = 17/12
1 + 1/(2+1(2+1/(2+1/2) = 41/29


Hence the sequence of the first ten convergents for sqrt(2) are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378


What is most surprising is that the important mathematical constant,
e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

---
Method:
- to unfold a continued fraction, we can use the shortcut that
    [ ... , a, b ] = [ ... , a + 1/b ]
- if we have b already as a fraction n/d, we can store it as a list; b = [n, d]
    thus...
    [ ... , a, b ] = [ ... , a, [n, d]]
    thus...
    [ ... , a + 1/b ] = [ ... , a + d/n]
    [ ... , a + 1/b ] = [ ... , (n*a + d)/n ]


- Alternatively, we can note that working left to right has the following properties:
    [a; b, c]
    thus...
    we note that the first two fractions will be:
    a/1 and (ab+1)/b
    then c becomes:
    (c(ab+1) + a)/(cb+1)

    if we generalize the continued fractions list:
    [a_0; a_1, a_2, ..., a_i]
    and if we then calculate convergents in terms of numerators (n) and denominators (d), we can see that
    convergent_n[i] = a_i*convergent_n[i-1] + convergent_n[i-2]
    convergent_d[i] = a_i*convergent_d[i-1] + convergent_d[i-2]

- Thus, to solve this problem, write a function that will convert a continued fraction into convergents

"""


def get_convergent(continued_fraction):
    """

    :param continued_fraction: list of form [a0, a1, a2, ... , ai]
    :return: list of form [[n0, d0], [n1, d1], [n2, d2], ... , [ni, di]]
    """

    l_cf = len(continued_fraction)

    convergents = [] * l_cf
    n = continued_fraction[0]
    d = 1
    convergents.append([n, d])

    if l_cf == 1:
        return convergents

    n = continued_fraction[0]*continued_fraction[1] + 1
    d = continued_fraction[1]
    convergents.append([n, d])

    for i in range(2, l_cf):
        n = continued_fraction[i]*convergents[i-1][0] + convergents[i-2][0]
        d = continued_fraction[i]*convergents[i-1][1] + convergents[i-2][1]
        convergents.append([n, d])

    return convergents


# create a continued fraction for e up to 100 fractions
limit = 100
e = [2]
for i in range(1, limit):
    if (i+1) % 3 == 0:
        f = 2*int((i+1) / 3)
        e.append(f)
    else:
        e.append(1)

cf_e = get_convergent(e)
last_convergent = cf_e[-1]
numerator = last_convergent[0]

ans = sum([int(x) for x in list(str(numerator))])
print(f"ans == {ans}")
