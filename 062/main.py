"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

---
Method:
- create a list of cubed numbers
- start at the back of the list and work toward the front of the list
- with the largest element in the list, compare it against smaller elements and compare the sorted digits
- if equal, increment a count
- continue to search until the counter is the same as the COUNT_LIM, which is defined in the problem details

"""

COUNT_LIM = 5


def add_cube(cube_list):
    l = len(cube_list) + 1
    cube_list.append(l ** 3)
    return cube_list


def get_digit_list(num):
    digits = [d for d in str(num)]
    digits.sort()
    return digits


def is_permutation(list1, list2):
    # move the following code to loop to be able to break out earlier
    # if len(list1) != len(list2):
    #     return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


lowest_num = None
running = True
cube_list = []
cube_list = add_cube(cube_list)
while running:
    cube_count = 1
    cube_list = add_cube(cube_list)
    num1 = cube_list[-1]
    dig_list1 = get_digit_list(num1)  # get last item in cube list

    for i in range(len(cube_list) - 2, -1, -1):
        # start at the second to last number in the list and work backward
        num2 = cube_list[i]
        # print(f"{num1} vs {num2}")
        if len(str(num1)) != len(str(num2)):
            # this can't possibly work, and so move on
            break
        dig_list2 = get_digit_list(num2)
        if is_permutation(dig_list1, dig_list2):
            cube_count += 1
            lowest_num = num2

    if cube_count == COUNT_LIM:
        running = False

ans = lowest_num
print(f"ans == {ans}")
