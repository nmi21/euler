"""
Attempt to solve 031 with recursion as opposed to dynamic programming


"""

COINS = [200, 100, 50, 20, 10, 5, 2, 1]
TARGET = 200

memo_dict = {}


def find_coin_ways(coin_sum, limit_val, coins_available, current_coin_pointer):
    # tup_key = (coin_sum, current_coin_pointer)
    
    num_ways = 0
    if current_coin_pointer >= len(coins_available):
        return num_ways
    while coin_sum < limit_val:
        num_ways += find_coin_ways(coin_sum, limit_val, coins_available, current_coin_pointer + 1)
        print(f"{'__' * current_coin_pointer} Adding {coins_available[current_coin_pointer]} cents")
        coin_sum += coins_available[current_coin_pointer]
        print(f"coin_sum == {coin_sum}")
    if coin_sum == limit_val:
        print(f"Solution found!")
        num_ways += 1
    return num_ways


print(find_coin_ways(0, TARGET, COINS, 0))
print(memo_dict)


# TODO implement memoization
