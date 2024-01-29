"""
By counting carefully it can be seen that a rectangular grid measuring 2 x 3 contains eighteen rectangles:

    x 0 0       x x 0       x x x
    0 0 0       0 0 0       0 0 0
      6           4           2

    x 0 0       x x 0       x x x
    x 0 0       x x 0       x x x
      3           2           1

Although there exists no rectangular grid that contains exactly two million rectangles, 
find the area of the grid with the nearest solution.

-- 
Method:
- To see how this works, let's find all of the solutions for the 2x3 grid and how a 1x1 square and a 1x2 square fit
    - 1x1 square
        1.
            x 0 0
            0 0 0
        2. 
            0 x 0
            0 0 0
        3. 
            0 0 x
            0 0 0
        4. 
            0 0 0
            x 0 0
        5. 
            0 0 0
            0 x 0
        6.
            0 0 0
            0 0 x
    - 1x2 square
        1. 
            x x 0
            0 0 0
        2. 
            0 x x
            0 0 0
        3. 
            0 0 0
            x x 0
        4. 
            0 0 0
            0 x x
    Ultimately you could use these to find how any size square could fit

- Let's see how this expands to a 3x3 grid

    x 0 0       x x 0       x x x
    0 0 0       0 0 0       0 0 0
    0 0 0       0 0 0       0 0 0
      9           6           3

    x 0 0       x x 0       x x x
    x 0 0       x x 0       x x x
    0 0 0       0 0 0       0 0 0
      6           4           2

    x 0 0       x x 0       x x x
    x 0 0       x x 0       x x x
    x 0 0       x x 0       x x x
      3           2           1
So the total for a 3x3 grid = 36

For a m x n grid, the first pattern that emerges looks like

    m*n         m*(n-1)         ...     m*2         m

    (m-1)*n     (m-1)*(n-1)     ...     (m-1)*2     (m-1)

    ...         ...             ...     ...         ...      
    
    2*n         2*(n-1)         ...     4           2
    
    n           n - 1           ...     2           1

So for a 3x4 grid, we see the following numbers

    12  9   6   3
    8   6   4   2
    4   3   2   1

This totals to 60.


Writing out the first few:
    m   n   total
    2   3   18
    3   3   36
    3   4   60

What we can notice is that the bottom row will be summed and then multiplied by a number
Using the 3x4 example, we can notice that
    sum = 4 + 3 + 2 + 1 = 1 + 2 + 3 + 4
    sum = i from i=1 to m
    this is also the triangle number for m!

As we then go through the various rows, we can see that it goes as follows:
    sum = 3 + 2 + 1 = 1 + 2 + 3
    sum = j from j=1 to n
    this is the triangle number for n!

Thus, the total number of rectangles for any m x n grid is given by the product of the triangle numbers for m and n:
    total rectangles = triangle(m) x triangle(n)        {triangle(k) = k(k + 1)/2}
    total rectangles = (m(m + 1) / 2) * (n(n+1) / 2)
    total rectangles = m(m+1) * n(n+1) / 4
    
Continue to search in one dimension until that number exceeds the target (2,000,000), then go on to the next dimension.
    
"""

import time


t = time.time()
TARGET = 2_000_000


def triangle(num: int):
    return ((num ** 2) + num) // 2


closest_rects = 0
closest_size = (0, 0)
m = 2
while True:
    # start n at the value for m
    n = m

    # increment values of n and determine if we should replace the closest_rects
    while True:

        # calculate the total number of rectangles to be able to fit in that grid
        num_rects = triangle(m) * triangle(n)

        # check to see if the newly calculated num_rects is closer to the target than previous entries
        # if yes, save those entries
        if abs(TARGET - num_rects) < abs(TARGET - closest_rects):
            closest_rects = num_rects
            closest_size = (m, n)
        
        # if the number of rectangles is greater than our target, break out and go to next value for m
        if num_rects > TARGET:
            break
        
        # otherwise, increment n and try again!
        n += 1

    # check to see if square is too big; if yes, abort search
    if num_rects > TARGET and m == n:
        print(f"Aborted search at {m=}, {n=}, {num_rects=}.")
        print()
        break

    # else, increment value of m
    m += 1

print(f"{closest_rects=}")
print(f"{closest_size=}")

ans = closest_size[0] * closest_size[1]
print(f"{ans=}")


print(f"{time.time() - t} sec")
