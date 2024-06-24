"""
Consider quadratic Diophantine equations of the form:

x^2 – D*y^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

---
Method:
- this appears to be Pell's equation: https://en.wikipedia.org/wiki/Pell%27s_equation
- get all values of D by removing the set of squares in the limit

- Solving Pell's equation:
    - let h_i / k_i denote the sequence of convergents for the regular continued fraction sqrt(n)
    - then the pair (x1, y1) solving Pell's equation AND minimizing x satisfies x1 = h_i and y1 = k_i for some i
    - this pair is called the fundamental solution

- thus, unfold the convergents until it satisfies Pell's equation

"""

import math


def contfract(N):
    if int(math.sqrt(N)) ** 2 == N:
        return [int(math.sqrt(N)), ()]

    """
    fraction of the form x_i = r / (sqrt(N) - p)
    transforms into (sqrt(N) + p) / ((N - p**2)/r)

    we can redefine r to be the denominator of the previous: r = (N - p**2)/r
    we can then extract the integer portion and call that a_i
    then we can rewrite the equation as 
        x_i = a_i + (sqrt(N) + (p - a_i*r))/r
    we can redefine p as
        p = p - a_i*r

    then we know that x_(i+1) can be written as r / (sqrt(N) - p) and continue to calculate!
    """

    a_list = [int(math.sqrt(N))]
    r = 1
    p = a_list[0]

    while a_list[-1] != 2 * a_list[0]:
        # print(f"x_i == {r} / (sqrt({N}) - {p})")
        r = int((N - p ** 2) / r)
        # print(f"x_i == (sqrt({N}) + {p}) / {r}")
        a_i = int((math.sqrt(N) + p) / r)
        p = abs(p - a_i * r)
        a_list.append(a_i)

    return [a_list[0], tuple(a_list[1:])]


def fundamental_pells_equation(D):
    """
    Pell's equation of the form x^2 - Dy^2 = 1
    :param D: as shown in equation
    :return: fundamental solution pair x, y
        that is, first h, k that satisfy the equation
    """

    # check if number is a perfect square
    if int(math.sqrt(D))**2 == D:
        return [1, 0]

    cf = contfract(D)
    repeat = cf[1]
    period = len(repeat)

    h = cf[0]
    k = 1
    convergents = [[1, 0], [h, k]]

    i = 0
    while h**2 - D*(k**2) != 1:
        a_i = repeat[i % period]

        h = a_i*h + convergents[0][0]
        k = a_i*k + convergents[0][1]

        convergents[0] = convergents[1]
        convergents[1] = [h, k]

        i += 1

    return h, k


limit = 1000
d_list = [fundamental_pells_equation(x)[0] for x in range(1, limit + 1)]

ans = d_list.index(max(d_list)) + 1
print(f"ans == {ans}")
