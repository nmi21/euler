"""
https://projecteuler.net/problem=710

--

Method:
- In order to get the value for t(n), we can bifurcate the answer
into two separate cases:
    - n % 2 == 0
    - n % 2 == 1
    That is, is n odd or even?
- Since we are interested in palindrome sequences, we don't need to 
generate both sides. We only need to generate one side, and then we 
know that we can mirror the side in order to get a palindrome
- The next part to concern ourselves with is: where does the '2' fit?
but we will deal with that later
- Palindrome sequences will have a value at least 2*(sum(sequence))
This means that it will ALWAYS be even. 
- In order for the palindrome to sum to be odd, there MUST be an odd
number of total elements. This is because the left side sequence plus
the right side sequence will always be even. Then the middle element 
must be odd because even + odd is how we will get an odd total sum
- If the palindrome is even, there are two possible cases
    - the number of elements in the full sequence is even
    - the number of elements in the full sequence is odd
        - the middle number will be even

- First we will concern ourselves with the compositions; that is, how
many different ways can you write the sum of a number
    - c(0) = 0
        n/a
    - c(1) = 1
        (1)
    - c(2) = 2
        (1, 1)
        (2)
    - c(3) = 4
        (1, 1, 1)
        (1, 2), (2, 1)
        (3)
    - c(4) = 8
        (1, 1, 1, 1)
        (1, 1, 2), (1, 2, 1), (2, 1, 1)
        (1, 3), (3, 1), (2, 2)
        (4)
    - c(5) = 16
        (1, 1, 1, 1, 1)
        (1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (2, 1, 1, 1)
        (1, 1, 3), (1, 3, 1), (3, 1, 1), (1, 2, 2), (2, 1, 2), (2, 2, 1)
        (1, 4), (4, 1), (2, 3), (3, 2)
        (5)

    We can see that c(n) = 2**(n-1)

- How many of those compositions contain a '2'?
    - We can look at our compositions and select from those to start
    - let f(x) be the number of 2-containing compositions for a number 'x'

    f(0) = 0
        n/a
    f(1) = 0
        n/a
    f(2) = 1
        (2)
    f(3) = 2
        (1, 2), (2, 1)
    f(4) = 4
        (1, 1, 2), (1, 2, 1), (2, 1, 1)
        (2, 2)
    f(5) = 9
        (1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (2, 1, 1, 1)
        (1, 2, 2), (2, 1, 2), (2, 2, 1)
        (2, 3), (3, 2)

- It's straightforward to realize that there are no compositions that contain
a '2' when n < 2
- As a sanity check, there will always be fewer than 2**(n-1) compositions that
contain a '2' because 2**(n-1) is the total number of compositions for n

~~~~~~~~~~~~~~~

- Let n = 5

- If we know the total number of compositions for a number n-2, then we simply
have to append a '2' to the sequence and the sum will be n; in this way we can
guarantee that there will be a '2' in it and it is a twopal

    c(x) = 2**(x - 1)
    c(n-2) = 2**((n-2) - 1)
    c(n-2) = 2**(n - 2 - 1)
    c(n-2) = 2**(n - 3)

    Thus, looking at compositions for n-2 = 5-2 = 3

    c(3) = 
        (1, 1, 1)
        (1, 2)
        (2, 1)
        (3)

    Each one of those just needs a '2' added to the sequence in order
    to create a twopal
    
    c2(3) = 
        (2, 1, 1, 1)
        (2, 1, 2)
        (2, 2, 1)
        (2, 3)

- What about for numbers that are not n-2? How many contain a '2' already?
    - in this case, we are trying to find f(n). We ideally have already
    calculated f(k) for all k < n. Let's look at those numbers:

        f(0) = 0
            n/a
        f(1) = 0
            n/a
        f(2) = 1
            (2)
        f(3) = 2
            (1, 2)
            (2, 1)
        f(4) = 4
            (1, 1, 2)
            (1, 2, 1)
            (2, 1, 1)
            (2, 2)

    - Let's add the requesite number to each of these (ignoring k = 0, 1)

        f2(2)
            (3, 2)
        f2(3)
            (2, 1, 2)
            (2, 2, 1)
        f2(4)
            (1, 1, 1, 2)
            (1, 1, 2, 1)
            (1, 2, 1, 1)
            (1, 2, 2)

- Now we can combine all of the terms from c2(x) and f2(x)

    2 terms: 2x
        (2, 3)
        (3, 2)
    3 terms: 
        (2, 1, 2) ***
        (2, 2, 1) ***
        (2, 1, 2)
        (2, 2, 1)
        (1, 2, 2)
    4 terms:
        (2, 1, 1, 1)
        (1, 1, 1, 2)
        (1, 1, 2, 1)
        (1, 2, 1, 1)

    From this, we can see that there are some duplicate sequences;
    The duplicates are all from f2(3). Note that 3 is n-2!

    Removing duplicates, we reach a total of 9 total compositions for n=5

        (2, 3)
        (3, 2)
        (2, 1, 2)
        (2, 2, 1)
        (1, 2, 2)
        (2, 1, 1, 1)
        (1, 1, 1, 2)
        (1, 1, 2, 1)
        (1, 2, 1, 1)

    Ultimately what does this mean?
    - recall that we let f(x) be the number of 2-containing compositions for a 
    number 'x'
    - f(x) can potentially be calculated via a recurrance relation

        f(x) = c(x-2) + sum{from k=0 to n-1}[f(x)] - f(x-2)

~~~~~

Let's verify that!

Let x = 6

- Compositions for c(x-2) --> c(4)

    Recall that there should be 2**(4-1) = 2**3 = 8 compositions of '4'

    c(4)
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (2, 1, 1)
        (1, 3)
        (3, 1)
        (2, 2)
        (4)

    c2(4)
        (2, 1, 1, 1, 1)
        (2, 1, 1, 2)
        (2, 1, 2, 1)
        (2, 2, 1, 1)
        (2, 1, 3)
        (2, 3, 1)
        (2, 2, 2)
        (2, 4)

- We now need to sum f(k) from k=0 to n-1

    Recall that f(x) contains a '2' in its sequence

    We can ignore k = 0 and k = 1

        f(2)
            (2)
        f(3)
            (1, 2)
            (2, 1)
        f(4)
            (1, 1, 2)
            (1, 2, 1)
            (2, 1, 1)
            (2, 2)
        f(5)
            (2, 3)
            (3, 2)
            (2, 1, 2)
            (2, 2, 1)
            (1, 2, 2)
            (2, 1, 1, 1)
            (1, 1, 1, 2)
            (1, 1, 2, 1)
            (1, 2, 1, 1)

    Get f2(x) by adding the requesite number

        f2(2)
            (4, 2)
        f2(3)
            (3, 1, 2)
            (3, 2, 1)
        f2(4)
            (2, 1, 1, 2)
            (2, 1, 2, 1)
            (2, 2, 1, 1)
            (2, 2, 2)
        f2(5)
            (1, 2, 3)
            (1, 3, 2)
            (1, 2, 1, 2)
            (1, 2, 2, 1)
            (1, 1, 2, 2)
            (1, 2, 1, 1, 1)
            (1, 1, 1, 1, 2)
            (1, 1, 1, 2, 1)
            (1, 1, 2, 1, 1)

- Let's combine and remove duplicates        

        (4, 2)
        (2, 4)
        (3, 1, 2)
        (3, 2, 1)
        (1, 2, 3)
        (1, 3, 2)
        (2, 1, 3)
        (2, 3, 1)
        (2, 2, 2)
        (1, 2, 1, 2)
        (1, 2, 2, 1)
        (1, 1, 2, 2)
        (2, 1, 1, 2)
        (2, 1, 2, 1)
        (2, 2, 1, 1)
        (1, 2, 1, 1, 1)
        (1, 1, 1, 1, 2)
        (1, 1, 1, 2, 1)
        (1, 1, 2, 1, 1)
        (2, 1, 1, 1, 1)
        (2, 1, 1, 2) ***
        (2, 1, 2, 1) ***
        (2, 2, 1, 1) ***
        (2, 2, 2) ***

    There are 20x non duplicate ways to form f(6)

- What happens if we calculate it from our equation?

    f(x) = c(x-2) - f(x-2) + sum{from k=0 to n-1}[f(k)]

    f(6) = c(6-2) - f(6-2) + sum{from k=0 to 6-1}[f(k)]
    f(6) = c(4) - f(4) + sum{from k=0 to 6-1}[f(k)]
    f(6) = c(4) - f(4) + [f(2) + f(3) + f(4) + f(5)]
    f(6) = c(4) + f(2) + f(3) + f(5)
    f(6) = (2^(4-1)) + 1 + 2 + 9
    f(6) = 2^3 + 1 + 2 + 9
    f(6) = 8 + 1 + 2 + 9
    f(6) = 20

These are consistent!

~~~~~

Now let's try to figure out the twopals!

We can use each of the sequences from f(n) and get sums of 2*f(n)

For any palindromic sequence, we can observe the following

- Case 1: the sum of the sequence is even
    - Case 1a: there are an even number of total terms
    - Case 1b: there are an odd number of total terms
- Case 2: the sum of the sequence is odd
    - There must be an odd number of terms

~~~~~

Logic: Case 1a

If there are even terms, it will only be 2x the sequence from f(k)

~~~~~

Math: Case 1a

For t(2n), there will be f(n) possible ways to create a twopal

We want to find t(6), and so...

    t(6) = t(2n)

    ==> 6 = 2n
    ==> n = 3

How many even numbered terms exist for t(6)?

    f(3) = 2
        (1, 2)
        (2, 1)

    thus, even terms for t(6):
        (1, 2) + reverse((1, 2)) = (1, 2, 2, 1)
        (2, 1) + reverse((2, 1)) = (2, 1, 1, 2)

    There are 2x even terms for t(6)
        (1, 2, 2, 1)
        (2, 1, 1, 2)

    This is consistent with the example given.

    **************
    Case 1a = f(n)
    **************

~~~~~

Logic: Case 1b

If there are odd terms, there will be 2x the sequence from f(k) PLUS
an additional term.

Since we have an odd number of terms, there will be a "middle" term.

Since we have a set of numbers that sums to be even (because 2x f(k) is
always even), the middle number must also be even.

Within this particular case, we can further subdivide into two seperate cases:

    Case 1b.1: the center element is '2'
    Case 1b.2: the center element is not '2'

In both of these case, we can let one side of the palindrome have 'm' elements.
Then, the total sequence will have 2*m + 1 total elements. 

Case 1b.1:
- we know that the middle is a '2', thus the whole thing is a twopal,
regardless of other elements
- we know that compositions can be determined by
    c(x) = 2^(x-1)
- if we are trying to reach t(6), for example, we want to know how many
compositions exist c(2) because we will have (left side) + (right side) + 2
- since this is t(2n), we care about
    c((2n - 2) / 2))
    c(n-1) = 2^((n-1) - 1)
    c(n-1) = 2^(n-2)
- Thus, there are 

    ********************
    Case 1b.1 == 2^(n-2)
    ********************

Case 1b.2:
- The middle is not a '2', thus we need the sides to contain a '2'
    - thus we are dealing with f(n)
- We can start at a middle of '4' and go all the way to '2n'
- we need to sum all values from k = 4 until 2n
- this becomes a sum of f(n - k/2) for k from 4:2n (step == 2)
- alternatively, f(n - j) for j from 2:n

    **************************************
    Case 1b.2 == sum{j from 2:n}(f(n - j))
    **************************************

Case 1 in total:

    **********************************************************
    **  t(2n) = f(n) + 2^(n-2) + sum{j from 2:n}(f(n - j))  **
    **********************************************************

~~~~~

Logic: Case 2

If the sequence is odd, there must be odd number of terms and the
middle term must be odd.

2*f(k) will always be even, and for the sequence to be odd, we must add
an odd number to it.

We need a '2' in the palindromic sides. Thus, we need f(n).

Similar to 1b.2, we will have a middle element, and that element will not be '2'.

We can use the same logic and find that we need a sum of a bunch of values of f(x)
sum f(x) for each value of k from 1:(2n+1), step == 2

Subtract 1 from both sides
j from 0:2n, step == 2

Divide by 2 and make the step == 1
sum(j from 0:n, step == 1){f(n - j)}

Since we are looping through each element, this is the same as
sum{j from 0:n}(f(j))

Case 2 in total:

    *****************************************
    **  t(2n + 1) = sum{j from 0:n}(f(j))  **
    *****************************************

~~~~~

    ************************************************************
    **  f(x) = 2^(x-3) + sum{from k=0 to x-1}[f(k)] - f(x-2)  **
    ************************************************************

    **********************************************************
    **  t(2n) = f(n) + 2^(n-2) + sum{j from 2:n}(f(n - j))  **
    **********************************************************

    *****************************************
    **  t(2n + 1) = sum{j from 0:n}(f(j))  **
    *****************************************

~~~~~

So that is what we have so far. After coding it up the first time, 
it looks like the t(2n) takes too much time.

I then noticed that I could use some of the same simplification tricks from Case 2
on t(2n)

Let's focus on this portion:
    sum{j from 2:n}(f(n - j))

We can rewrite it as 

This means that t(2n) can now be rewritten
    t(2n) = f(n) + 2^(n-2) + sum{j from 0:n-2}[f(j)]

By itself, that isn't particularly interesting or useful, but it does
look quite similar to 
    f(x) = 2^(n-3) + sum{from k=0 to x-1}[f(k)] - f(x-2)

Let's rearrange!
    t(2n) = 2^(n-2) + sum{j from 0:n-2}[f[j]] + f(n)

Let's add a term f(n-1) to all the sum to go from 0:n
    t(2n) = 2^(n-2) + sum{j from 0:n-2}[f[j]] + f(n) + f(n-1) - f(n-1)
    t(2n) = 2^(n-2) + sum{j from 0:n-2}[f[j]] + f(n-1) + f(n) - f(n-1)
    t(2n) = 2^(n-2) + [sum{j from 0:n-2}[f[j]] + f(n-1) + f(n)] - f(n-1)
    t(2n) = 2^(n-2) + [sum{j from 0:n}[f[j]]] - f(n-1)
    t(2n) = 2^(n-2) + sum{j from 0:n}[f(j)] - f(n-1)

Now compare the two equations:
    t(2n) = 2^(n-2) + sum{j from 0:n}[f(j)] - f(n-1)
    f(x) = 2^(x-3) + sum{from k=0 to x-1}[f(k)] - f(x-2)

What is f(x+1)?
    f(x+1) = 2^((x+1)-3) + sum{from k=0 to (x+1)-1}[f(k)] - f((x+1)-2)
    f(x+1) = 2^(x+1-3) + sum{from k=0 to (x+1-1)}[f(k)] - f(x+1-2)
    f(x+1) = 2^(x-2) + sum{from k=0 to (x)}[f(k)] - f(x-1)

Compare t(2n) vs. f(x+1):
    t(2n) = 2^(n-2) + sum{j from 0:n}[f(j)] - f(n-1)
    f(x+1) = 2^(x-2) + sum{from k=0 to (x)}[f(k)] - f(x-1)

So now we can say that t(2n) = f(x+1)

That's huge!

It should speed us up significantly!!!

    ************************************************************
    **  f(x) = 2^(x-3) + sum{from k=0 to x-1}[f(k)] - f(x-2)  **
    ************************************************************

    ************************
    **  t(2n) = f(n + 1)  **
    ************************

    *****************************************
    **  t(2n + 1) = sum{j from 0:n}(f(j))  **
    *****************************************

"""

import time
import itertools

t0 = time.time()


# first let's make some long form ways to calculate t(x)
def generate_partitions(n):

    # this will give all of the partitions that sum to a number n

    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in generate_partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


def is_palindrome(x):
    # go thru each element
    # determine if it matches the element in the opposite position
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            return False
    
    # if all are the same, is palindrome
    return True   


def twopal_longform(x):
    # the first thing we need to do is generate all of the 
    # partitions that sum to the input number x
    partitions = [tuple(l) for l in generate_partitions(x)]

    # get only the partitions with a 2 in them
    parts_with_2 = [y for y in partitions if 2 in y]

    # get all of the permutations for each of the tuples
    perms = set()
    for part in parts_with_2:
        perm_subset = set(itertools.permutations(part))
        perms.update(perm_subset)

    palins = set()
    for perm in perms:
        if is_palindrome(perm):
            palins.add(perm)      

    return len(palins)


# get a list of twopals for numbers 0:10 that we can compare a recurrance relation against
twopal_vals_longhand = []
for i in range(11):
    twopal_vals_longhand.append(twopal_longform(i))
print(twopal_vals_longhand)


# let's also generate longform values for f(x) to make sure we are on the right track
def f_longhand(num):
    """
    Get the number of compositions of k that contain a 2
    """

    parts = [tuple(x) for x in generate_partitions(num) if 2 in x]

    comps = set()
    for part in parts:
        perms = itertools.permutations(part)
        comps.update(perms)
        
    return len(comps)


f_vals_longhand = []
for i in range(11):
    f_vals_longhand.append(f_longhand(i))
print(f_vals_longhand)

# solve it via recurrance!
ans = None
mod_num = 10**6

n = 3
f_minus_2 = 0
f_minus_1 = 1
f_sum = 1

while True:

    if n % 10000 == 0:
        print(f"{n=}")

    f = 2**(n-3) + f_sum - f_minus_2
    f %= mod_num

    t_2n = f
    # if n == (6 // 2)+1:
    #     print(f"t(6): {t_2n}")
    # elif n == (20 // 2) + 1:
    #     print(f"t(20): {t_2n}")
    # elif n == (42 // 2) + 1:
    #     print(f"t(42): {t_2n}")
    if t_2n % mod_num == 0:
        ans = 2*n
        break

    t_2n_plus_1 = f_sum
    if t_2n_plus_1 % mod_num == 0:
        ans = 2*n + 1
        break

    n += 1
    f_minus_2 = f_minus_1
    f_minus_1 = f
    f_sum += f
    f_sum %= mod_num

print(f"{ans=}")

print(f"{time.time() - t0} sec")
