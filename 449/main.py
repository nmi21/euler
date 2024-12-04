"""
https://projecteuler.net/problem=449
"""

import time
import math
import numpy as np 

t0 = time.time()


def vol_ellipsoid(a, b, c):
    # volume of ellipsoid with semi axes a, b, and c
    return (4/3) * math.pi * a * b * c


def volume_of_chocolate(a, b, num_slices=1_000_000):
    # given an ellipsoid with 1mm covering of chocolate

    # given the nature of the ellipse equation in this problem, 
    # we can simply double the result because it is mirrored across the yz plane

    # make an array from 0 --> pi/2
    t = np.linspace(0, np.pi/2, num_slices)

    # get x, y coordinates for the ellipse
    ex = a * np.cos(t)
    ez = b * np.sin(t)

    # get the normal vector directions
    nx = b * np.cos(t)
    nz = a * np.sin(t)

    # get the length of the normal vector
    l = np.sqrt(nx**2 + nz**2)

    # normalize the vectors to unit length
    nx_t = nx/l
    nz_t = nz/l

    # get the locations of the offset surfaces in x, y
    oex = ex + nx_t
    oez = ez + nz_t

    # essentially, we will divide the ellipsoid into a bunch of very thin disks
    # and then add those disks together to get the full volume
    # depending on how we add them (bottom up or top down), we will get two slightly 
    # different answers, which I will call the maximum and minimum material conditions.
    # One of the answers will be slightly smaller than the correct answer, and the 
    # other will be slightly larger. Averaging the two answers should give us enough 
    # resolution to answer the question to the requisite 8 decimal places.
    
    # maximum material
    x_rad_max = oex[:-1]
    z_h_max = np.diff(oez)
    vol_max = np.sum(np.pi * (x_rad_max**2) * z_h_max)

    # # minimum material
    x_rad_min = oex[::-1][:-1]
    z_h_min = -np.diff(oez[::-1])
    vol_min = np.sum(np.pi * (x_rad_min**2) * z_h_min)
    vol_centre = vol_ellipsoid(a, a, b)

    # double volume of candy per ealier comments
    # but 2* cancels out with averaging of min and max
    vol_choc = (vol_max + vol_min) - vol_centre

    return np.round(vol_choc, 8)


print(f"{volume_of_chocolate(1, 1)=}")
print(f"{volume_of_chocolate(2, 1)=}")
print(f"{volume_of_chocolate(3, 1)=}")

print(f"{time.time() - t0} sec")
