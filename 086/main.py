"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. 
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

https://projecteuler.net/problem=86

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions,
up to a maximum size of M x M x M, for which the shortest route has integer length when M = 100.
This is the least value of M for which the number of solutions first exceeds 2,000;
the number of solutions when M = 99 is 1,975.

Find the least value of M such that the number of solutions first exceeds 1,000,000.

-- 
Method:
- We can imagine that the box is composed of lengths: x, y, z
- We can let f(M) be the number of cuboids that have integer solutions
    - so we know f(99) = 1975
    - we also know f(100) = 2060
- From this, we can determine that f(M) - f(M - 1) = 
    number of cuboids with at least one wall length M
- we can check integer solutions with pythagorean theorem
    - and we never have to take the sqrt
    - simply see if the number is a perfect square

"""

import time
import itertools
from math import sqrt

t = time.time()

def num_integral_paths(max_len):
    count = 0
    cuboids = []
    squares = set(i * i for i in range(1, 3 * max_len))

    for x in range(1, max_len + 1):
        for y in range(x, max_len + 1):
            for z in range(y, max_len + 1):
                diag1sq = x*x + (y+z)*(y+z)
                diag2sq = y*y + (x+z)*(x+z)
                diag3sq = z*z + (x+y)*(x+y)

                min_diagsq = min(diag1sq, diag2sq, diag3sq)
                if min_diagsq in squares:
                    count += 1
                    cuboids.append((x, y, z))

    return count, cuboids



def num_integer_paths(max_wall_length):

    def add_perfect_square(matrix):
        n = len(matrix) + 1
        matrix.append(n**2)
        return matrix
    
    perfect_squares = [1]
    count = 0

    for x in range(1, max_wall_length + 1):
        for y in range(x, max_wall_length + 1):
            for z in range(y, max_wall_length + 1):
                p1_sq = x**2 + (y + z)**2
                p2_sq = y**2 + (x + z)**2
                p3_sq = z**2 + (x + y)**2

                max_path = max(p1_sq, p2_sq, p3_sq)
                while max_path >= perfect_squares[-1]:
                    add_perfect_square(perfect_squares)
                
                min_path = min(p1_sq, p2_sq, p3_sq)
                if min_path in perfect_squares:
                    count += 1
    
    return count






def cuboids_over_threshold(limit):

    # perfect_squares = [1]
    # def add_square():
    #     n = len(perfect_squares)
    #     n += 1
    #     perfect_squares.append(n**2)

    # # it would be faster to pick an absurdly large number and get all of the squares
    perfect_squares = set([i**2 for i in range(1, 10_000)])
    
    def wall_size_solutions(max_wall_size):
        """
        Assume you have a wall of size M. 
        We can determine that f(M) - f(M - 1) = 
            number of cuboids with at least one wall length M
        This function returns that value.
        """
        solutions = 0
        z = max_wall_size
        for x in range(1, max_wall_size + 1):
            for y in range(x, max_wall_size + 1):
                p1 = x**2 + (y + z)**2
                p2 = y**2 + (x + z)**2
                p3 = z**2 + (x + y)**2

                # max_path = max(p1, p2, p3)
                # while max_path >= perfect_squares[-1]:
                #     add_square()

                min_path = min(p1, p2, p3)
                if min_path in perfect_squares:
                    solutions += 1
        
        return solutions
    
    counter = 0
    cuboids = []
    while counter <= limit:
        next_size = len(cuboids) + 1
        sols = wall_size_solutions(next_size)
        counter += sols
        cuboids.append(sols)

        if len(cuboids) % 100 == 0:
            print(f"{len(cuboids)=}")
            print(f"{counter=}")
            print(f"{time.time() - t} sec")
            print()

    M = len(cuboids)

    return M, counter, cuboids

M, count, cubes = cuboids_over_threshold(1_000_000)
print(f"{M=}")
print(f"{count=}")
# print(f"{cubes=}")
print(len(cubes))



print(f"{time.time() - t} sec")
