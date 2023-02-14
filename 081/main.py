"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and
down, is indicated in bold red and is equal to 2427.

    131     673     234     102     18
    201     96      342     965     150
    630     803     746     422     111
    537     699     497     121     956
    805     732     524     37      331

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right
click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

---
Method:
- you can create a minimum cost function for each path by breaking down the matrix along diagonals
    e.g. Take 131 (first element) and add to adjacent bottom and right; then continue to repeat, using only the
    lowest of the available adjacent options

        131     673     234     102     18
        201     96      342     965     150
        630     803     746     422     111
        537     699     497     121     956
        805     732     524     37      331

        (131)   804     234     102     18
        332     96      342     965     150
        630     803     746     422     111
        537     699     497     121     956
        805     732     524     37      331

                (804)   1038     102     18
        (332)   428     342     965     150
        962     803     746     422     111
        537     699     497     121     956
        805     732     524     37      331

                        (1038)  102     18
                (428)   342     965     150
        (962)   803     746     422     111
        537     699     497     121     956
        805     732     524     37      331

                                (1140)  18
                        (770)   965     150
                (1231)  746     422     111
        (1499)  699     497     121     956
        805     732     524     37      331

                                        (1158)
                                (1735)   150
                        (1515)   422     111
                (1930)   497     121     956
        (2304)   732     524     37      331

                                        (1308)
                                (1937)   111
                        (2012)   121     956
                (2662)   524     37      331


                                        (2375)
                             (2096)      2427

                                final == 2427

"""
import numpy as np

matrix = np.array([
    [131, 673, 234, 102, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
])
