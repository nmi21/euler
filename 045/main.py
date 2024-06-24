import math
import pdb


tris = []
pents = []
hexs = []


def tri_num(n):
    return int(n*(n+1)/2)


def pent_num(n):
    return int(n*(3*n - 1)/2)


def hex_num(n):
    return int(n*(2*n - 1))


def add_nums():
    n = len(tris) + 1
    tris.append(tri_num(n))
    pents.append(pent_num(n))
    hexs.append(hex_num(n))


add_nums()

combo_nums = []
n = 1
while len(combo_nums) < 3:
    ind = n - 1
    if (tris[ind] in pents) and (tris[ind] in hexs):
        print(f"n == {n}")
        print(f"num == {tris[ind]}")
    n += 1
    add_nums()
