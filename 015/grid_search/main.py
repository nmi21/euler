# attempt to solve 015 using grid search
"""
we can expect that this will take a long time as the grid gets very large, but the exercise is likely still valuable
"""

def lattice_paths(r, c):
    if r == 0 and c == 0:
        # you have reached the end
        return 1
    if r < 0 or c < 0:
        # you went beyond the bounds of the grid
        return 0
    # otherwise shrink your grid in each dimension
    return lattice_paths(r-1, c) + lattice_paths(r, c-1)

print(lattice_paths(4, 4))