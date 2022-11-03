"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

----
iterate over all possible valid combinations using all coins expect 2pound
add 1 to total solutions at end to cover value for 1x 2 pound coin


methodology:
-- we are going to calculate the number of possible ways that each total value of coins can be created given the 
types of coins that we have
-- "ways" will represent an array that each shows how many possibilities can be created for each coin
-- for example, we know that in order to have a total of 0 pence, there is only 1 possibility: 0x all coins
-- likewise, we can only create 1p in 1 way: 1x 1p coin and 0x everything else
-- 2p can be created in two ways: 2x 1p; 1x 2p
-- 3p can be created in two ways: 3x 1p; 1x 2p + 1x 1p
-- 4p can be created in three ways: 4x 1p; 2x 2p; 1x 2p + 2x 1p
-- 5p can be created in four ways: 5x 1p; 2x 2p + 1p; 1x 2p + 3x 1p; 1x 5p

-- it should be recognized that you can't change the number of possibilities for any value less than the coin being 
considered
-- that is to say, a 10p coin cannot affect the number of possibilities for how many ways you can get 7p

-- the trick here is to recognize that we have already done a fair bit of the calculation. Look at the ways to
get 5p again:

             Using coins that are...
target_val   <= 1p   <= 2p   <= 5p  
----------   -----   -----   -----  
    0p         1       1       1     
    1p         1       1       1
    2p         1       2       2
    3p         1       2       2
    4p         1       3       3
    5p         1       3       4

-- essentially, for each value multiple of the largest coin, we can add that many possibilities to the array
-- consider written in the following way:

             Using coins that are...
target_val   <= 1p      using only 2p    total possibilities <= 2p
----------   -----      -------------    -------------------------
    0p         1     +       0        =           1     
    1p         1     +       0        =           1
    2p         1     +       1        =           2
    3p         1     +       1        =           2
    4p         1     +       2        =           3
    5p         1     +       2        =           3
    6p         1     +       3        =           4
    7p         1     +       3        =           4
    8p         1     +       4        =           5
    9p         1     +       4        =           5
   10p         1     +       5        =           6
   
    Now we have the total possibilities for all values when adding coins <= 2p
    If we expand to 5p coins, we get the following:
    
             Using coins that are...
target_val   <= 2p      with 5p coins    
----------   -----      -------------    
    0p         1     +       0        
    1p         1     +       0        
    2p         2     +       0        
    3p         2     +       0        
    4p         3     +       0        
    5p         3     +       1        
    6p         4     +       1        
    7p         4     +       1        
    8p         5     +       1        
    9p         5     +       1        
   10p         6     +       2        
   
   On the following rows, we are deficient options: 
             Using coins that are...
target_val   <= 2p      with 5p coins    
----------   -----      -------------    
    6p         4     +       1        
    7p         4     +       1        
    8p         5     +       1        
    9p         5     +       1        
   10p         6     +       2        
   
    The reason is because we also have to consider all of the options for the difference as well:
        -- for the 6p target_val, adding 1x 5p means that we have to consider all of the ways to get 6p - 5p = 1p
        -- luckily we have already calculated that and we can find it at position [1] == 1
        -- for the 7p target_val, we also need to add the number of ways to be able to get 2p == 2
        -- for 8p, we also need ways to get 3p == 2
        -- for 9p, we also need ways to get 4p == 3
        
    Thus, we can rewrite the table in the following way:

             Using coins that are...
target_val   <= 2p      with 5p coins   ways to get...               total possibilities <= 5p
----------   -----      -------------   --------------              -------------------------
    0p         1     +       0                              =           1     
    1p         1     +       0                              =           1
    2p         2     +       0                              =           2
    3p         2     +       0                              =           2
    4p         3     +       0                              =           3
    5p         3     +       1                              =           4
    6p         4     +       1        +     (1p) == 1       =           5
    7p         4     +       1        +     (2p) == 2       =           6
    8p         5     +       1        +     (3p) == 2       =           7
    9p         5     +       1        +     (4p) == 3       =           8
   10p         6     +       2                              =           10


In essence, we start at the value of the next coin (e.g. 10p) and then add 1, then for 11p total, we recognize that we
already know how to make 1p with all coins <= 10p, and so we can add that to the value that we had previously.

"""

amount = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
# coins = [1, 2]

ways = [0] * (amount + 1)
ways[0] = 1
# print(ways)
# print()

for i in range(len(coins)):
    for j in range(coins[i], amount + 1):
        ways[j] = ways[j] + ways[j - coins[i]]
        # print(i, j)
        # print(ways)
        # print()

# print(ways)
print(ways[amount])


