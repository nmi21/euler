"""
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

    (131)   673     (234)   (103)   (18)
    (201)   (96)    (342)   965     (150)
    630     803     746     (422)   (111)
    537     699     497     (121)   956
    805     732     524     (37)    (331)

Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt 
a 31K text file containing 80 by 80 matrix.

-- 
Method:
- Dijkstra's algorithm
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/#:~:text=Dijkstra's%20Algorithm%20finds%20the%20shortest,node%20and%20all%20other%20nodes.

- Dijkstra's method in my own words
    - you know 
        - source node (beginning)
        - end node (end)
    - for a matrix traversal like this, we will use the cost between each node as the value at each node
    - for each node that we visit, we find available neighbors
    - then we calculate the cost function of each of those moves
    - we take the smallest one and add it to a set of visited nodes
    - that should always be the smallest possible cost to get to that node, and so we never have to revisit it

my_data = [
    [131,   673,    234,    103,    18],
    [201,   96,     342,    965,    150],
    [630,   803,    746,    422,    111],
    [537,   699,    497,    121,    956],
    [805,   732,    524,    37,     331]
]

start off with another matrix that includes the distances
    dist = [
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]
    visited_nodes = {
    }
    unvisited_nodes = {
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }

You know the cost for your source node
Source node is (0, 0) and is my_data[0][0]
Remove (0, 0) from unvisited nodes
Add to (0, 0) visited nodes
    dist = [
        [131,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]
    visited_nodes = {
        (0, 0)
    }
    unvisited_nodes = {
                (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }

1. From each of the visited nodes, determine adjacent nodes
visited_nodes = {
    (0, 0)
}
    adjacent nodes to
        (0, 0): (0, 1), (1, 0)
2. Determine the cost to get to each node
    (0, 1)
        cost = dist[0][0] + my_data[0][1] = 131 + 673 = 804
    (1, 0)
        cost = dist[0][0] + my_data[1][0] = 131 + 201 = 332
3. Add each of those values to a queue
    queue = {
        (0, 1): 804
        (1, 0): 332
    }
4. Compare each key, item in the queue to the value in dist, take the smallest value
    dist = [
        [131,   804,    inf,    inf,    inf],
        [332,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]
5. Find the min val in the queue and extract the value and location key
    min_val = 332
    min_loc = (1, 0)
6. Remove the min_loc from the unvisited_nodes and add to visited_nodes
    visited_nodes = {
        (0, 0),
        (1, 0)
    }
    unvisited_nodes = {
                (0, 1), (0, 2), (0, 3), (0, 4),
                (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }

-- Repeat --

1. From each of the visisted nodes, determine adjacent values (only unvisited nodes)
    visited_nodes = {
        (0, 0),
        (1, 0)
    }
    adjacent_nodes = {
        (0, 1)
        (1, 1)
        (2, 0)
    }

2. Determine the cost to get to each node
    (0, 1)
        cost = dist[0][0] + my_data[0][1] = 131 + 673 = 804
    (1, 1)
        cost = dist[1][0] + my_data[1][1] = 332 + 96 = 428
    (2, 0)
        cost = dist[1][0] + my_data[2][0] = 332 + 630 = 962

3. Add each of those values to a queue
    queue = {
        (0, 1): 804
        (1, 1): 428
        (2, 0): 962
    }

4. Compare each key, item in the queue to the value in dist, take the smallest value
    (0, 1) = 804 < inf
    (1, 1) = 428 < inf
    (2, 0) = 962 < inf

    dist = [
        [131,   804,    inf,    inf,    inf],
        [332,   428,    inf,    inf,    inf],
        [962,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]

5. Find the min val in the queue and extract the value and location key
    min_val = 428
    min_loc = (1, 1)
    
6. Remove the min_loc from the unvisited_nodes and add to visited_nodes
    visited_nodes = {
        (0, 0),
        (1, 0), (1, 1)
    }
    unvisited_nodes = {
                (0, 1), (0, 2), (0, 3), (0, 4),
                        (1, 2), (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }
7. Clear the queue
    queue = {}

-- Repeat --


1. From each of the visisted nodes, determine adjacent values (only unvisited nodes)
    visited_nodes = {
        (0, 0),
        (1, 0), 
        (1, 1)
    }
    adjacent_nodes = {
        (0, 1)
        (2, 0)
        (0, 1)
        (2, 1)
        (1, 2)
    }

2. Determine the cost to get to each node
    (0, 1)
        cost = dist[0][0] + my_data[0][1] = 131 + 673 = 804
    (2, 0)
        cost = dist[1][0] + my_data[2][0] = 332 + 630 = 962
    (0, 1) [from (1, 1)]
        cost = dist[1][1] + my_data[0][1] = 428 + 673 = 1101
    (2, 1)
        cost = dist[1][1] + my_data[2][1] = 428 + 803 = 1231
    (1, 2)
        cost = dist[1][1] + my_data[1][2] = 428 + 342 = 770

3. Add each of those values to a queue
    queue = {
        (0, 1): 804 (((NOTE: take 804 because < 1101)))
        (2, 0): 962
        (2, 1): 1231
        (1, 2): 770
    }

4. Compare each key, item in the queue to the value in dist, take the smallest value
    (0, 1) = 804 == same
    (2, 0) = 962 == same
    (2, 1) = 1231 < inf
    (1, 2) = 770 < inf

    dist = [
        [131,   804,    inf,    inf,    inf],
        [332,   428,    770,    inf,    inf],
        [962,  1231,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]

5. Find the min val in the queue and extract the value and location key
    min_val = 770
    min_loc = (1, 2)

6. Remove the min_loc from the unvisited_nodes and add to visited_nodes
    visited_nodes = {
        (0, 0),
        (1, 0), (1, 1), (1, 2)
    }
    unvisited_nodes = {
                (0, 1), (0, 2), (0, 3), (0, 4),
                                (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }

7. Clear the queue
    queue = {}

-- REPEAT -- 


1. From each of the visisted nodes, determine adjacent values (only unvisited nodes)
    visited_nodes = {
        (0, 0),
        (1, 0), 
        (1, 1), 
        (1, 2)
    }
    adjacent_nodes = [
        (0, 1) from (0, 0)
        (2, 0) from (1, 0)
        (0, 1) from (1, 1)
        (2, 1) from (1, 1)
        (0, 2) from (1, 2)
        (2, 2) from (1, 2)
        (1, 3) from (1, 2)
    ]

2. Determine the cost to get to each node
    
    dist = [
        [131,   804,    inf,    inf,    inf],
        [332,   428,    770,    inf,    inf],
        [962,  1231,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]    

    my_data = [
        [131,   673,    234,    103,    18],
        [201,   96,     342,    965,    150],
        [630,   803,    746,    422,    111],
        [537,   699,    497,    121,    956],
        [805,   732,    524,    37,     331]
    ]

    (0, 1) from (0, 0)
        cost = dist[0][0] + my_data[0][1] = 131 + 673 = 804
    (2, 0) from (1, 0)
        cost = dist[1][0] + my_data[2][0] = 332 + 630 = 962
    (0, 1) from (1, 1)
        cost = dist[1][1] + my_data[0][1] = 428 + 673 = 1101
    (2, 1) from (1, 1)
        cost = dist[1][1] + my_data[2][1] = 428 + 803 = 1231
    (0, 2) from (1, 2)
        cost = dist[1][2] + my_data[0][2] = 770 + 234 = 1004
    (2, 2) from (1, 2)
        cost = dist[1][2] + my_data[2][2] = 770 + 746 = 1516
    (1, 3) from (1, 2)
        cost = dist[1][2] + my_data[1][3] = 770 + 965 = 1735

3. Add each of those values to a queue
    queue = {
        (0, 1): 804
        (2, 0): 962
        (2, 1): 1231
        (0, 2): 1004
        (2, 2): 1516
        (1, 3): 1735
    }

4. Compare each key, item in the queue to the value in dist, take the smallest value

    (0, 1) = 804 == same
    (2, 0) = 962 == same
    (2, 1) = 1231 == same
    (0, 2) = 1004 < inf
    (2, 2) = 1516 < inf
    (1, 3) = 1735 < inf
    
    dist = [
        [131,   804,   1004,    inf,    inf],
        [332,   428,    770,   1735,    inf],
        [962,  1231,   1516,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]

5. Find the min val in the queue and extract the value and location key
    min_val = 804
    min_loc = (0, 1)

6. Remove the min_loc from the unvisited_nodes and add to visited_nodes
    visited_nodes = {
        (0, 0), (0, 1)
        (1, 0), (1, 1), (1, 2)
    }
    unvisited_nodes = {
                        (0, 2), (0, 3), (0, 4),
                                (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }

7. Clear the queue
    queue = {}

-- REPEAT -- 

1. From each of the visisted nodes, determine adjacent values (only unvisited nodes)
    visited_nodes = {
        (0, 0), (0, 1)
        (1, 0), (1, 1), (1, 2)
    }
    adjacent_nodes = [
        (0, 2) from (0, 1)
        (2, 0) from (1, 0)
        (2, 1) from (1, 1)
        (0, 2) from (1, 2)
        (1, 3) from (1, 2)
        (2, 2) from (1, 2)
    ]

2. Determine the cost to get to each node

    my_data = [
        [131,   673,    234,    103,    18],
        [201,   96,     342,    965,    150],
        [630,   803,    746,    422,    111],
        [537,   699,    497,    121,    956],
        [805,   732,    524,    37,     331]
    ]

    dist = [
        [131,   804,   1004,    inf,    inf],
        [332,   428,    770,   1735,    inf],
        [962,  1231,   1516,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]

    (0, 2) from (0, 1)
        cost = my_data[0][2] + dist[0][1] = 234 + 804 = 1038
    (2, 0) from (1, 0)
        cost = my_data[2][0] + dist[1][0] = 630 + 332 = 962
    (2, 1) from (1, 1)
        cost = my_data[2][1] + dist[1][1] = 803 + 428 = 1231
    (0, 2) from (1, 2)
        cost = my_data[0][2] + dist[1][2] = 234 + 770 = 1004
    (1, 3) from (1, 2)
        cost = my_data[1][3] + dist[1][2] = 965 + 770 = 1735
    (2, 2) from (1, 2)
        cost = my_data[2][2] + dist[1][2] = 746 + 770 = 1516
    
3. Add each of those values to a queue
    queue = {
        (2, 0): 962
        (2, 1): 1231
        (0, 2): 1004
        (1, 3): 1735
        (2, 2): 1516
    }

4. Compare each key, item in the queue to the value in dist, take the smallest value

    (2, 0) = 962 == same
    (2, 1) = 1231 == same
    (0, 2) = 1004 == same
    (1, 3) = 1735 == same
    (2, 2) = 1516 == same

    dist = [
        [131,   804,   1004,    inf,    inf],
        [332,   428,    770,   1735,    inf],
        [962,  1231,   1516,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]

5. Find the min val in the queue and extract the value and location key
    min_val = 962
    min_loc = (2, 0)

6. Remove the min_loc from the unvisited_nodes and add to visited_nodes
    visited_nodes = {
        (0, 0), (0, 1)
        (1, 0), (1, 1), (1, 2)
        (2, 0)
    }
    unvisited_nodes = {
                        (0, 2), (0, 3), (0, 4),
                                (1, 3), (1, 4),
                (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }
7. Clear the queue
    queue = {}

-- REPEAT -- 
    
1. From each of the visisted nodes, determine adjacent values (only unvisited nodes)
    visited_nodes = {
        (0, 0), (0, 1)
        (1, 0), (1, 1), (1, 2)
        (2, 0)
    }
    adjacent_nodes = [
        (0, 2) from (0, 1)
        (2, 1) from (1, 1)
        (0, 2) from (1, 2)
        (1, 3) from (1, 2)
        (2, 2) from (1, 2)
        (2, 1) from (2, 0)
        (3, 0) from (2, 0)
    ]

2. Determine the cost to get to each node

    my_data = [
        [131,   673,    234,    103,    18],
        [201,   96,     342,    965,    150],
        [630,   803,    746,    422,    111],
        [537,   699,    497,    121,    956],
        [805,   732,    524,    37,     331]
    ]

    dist = [
        [131,   804,   1004,    inf,    inf],
        [332,   428,    770,   1735,    inf],
        [962,  1231,   1516,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]

    (0, 2) from (0, 1)
        cost = my_data[0][2] + dist[0][1] = 234 + 804 = 1038
    (2, 1) from (1, 1)
        cost = my_data[2][1] + dist[1][1] = 803 + 428 = 1231
    (0, 2) from (1, 2)
        cost = my_data[0][2] + dist[1][2] = 234 + 770 = 1004
    (1, 3) from (1, 2)
        cost = my_data[1][3] + dist[1][2] = 965 + 770 = 1735
    (2, 2) from (1, 2)
        cost = my_data[2][2] + dist[1][2] = 746 + 770 = 1516
    (2, 1) from (2, 0)
        cost = my_data[2][1] + dist[2][0] = 803 + 962 = 1765
    (3, 0) from (2, 0)
        cost = my_data[3][0] + dist[2][0] = 537 + 962 = 1499

3. Add each of those values to a queue
    queue = {
        (2, 1) = 1231
        (0, 2) = 1004
        (1, 3) = 1735
        (2, 2) = 1516
        (3, 0) = 1499
    }

4. Compare each key, item in the queue to the value in dist, take the smallest value

    (2, 1) = 1231 == same
    (0, 2) = 1004 == same
    (1, 3) = 1735 == same
    (2, 2) = 1516 == same
    (3, 0) = 1499 < inf

    dist = [
        [131,   804,   1004,    inf,    inf],
        [332,   428,    770,   1735,    inf],
        [962,  1231,   1516,    inf,    inf],
        [1499,  inf,    inf,    inf,    inf],
        [inf,   inf,    inf,    inf,    inf],
    ]

5. Find the min val in the queue and extract the value and location key
    min_val = 1004
    min_loc = (0, 2)

6. Remove the min_loc from the unvisited_nodes and add to visited_nodes
    visited_nodes = {
        (0, 0), (0, 1), (0, 2)
        (1, 0), (1, 1), (1, 2)
        (2, 0)
    }
    unvisited_nodes = {
                                (0, 3), (0, 4),
                                (1, 3), (1, 4),
                (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }

7. Clear the queue
    queue = {}

Continue to repeat until you reach the end node



"""

import os
import time
import pdb

t = time.time()


def extract_matrix():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_path = __location__ + "/" + "p083_matrix.txt"
    with open(file=file_path, mode="r") as file:
        # extract data from the file
        # remove leading and trailing whitespaces with .strip()
        # extract each element using .split() and select the , char to split on
        # map each element to an int
        # convert to a list
        # do it for each line in the file
        data = [list(map(int, line.strip().split(','))) for line in file]
    
    return data


def dijkstra(data, __print=False):
    # use Dijkstra's algorithm to get the shortest path sum
    #
    # input a graph (matrix) in the form
    # graph = [
    #   [a, b, c],
    #   [d, e, f],
    #   [g, h, i]
    # ]


    def print_mat(mat, mat_name):
        print(f"{mat_name} = [")
        for m in mat:
            print(f"    {m}")
        print("]")
        print()


    rows = len(data)
    cols = len(data[0])

    # create visited nodes
    visited_nodes = set()
    # create unvisited
    unvisited_nodes = set([(r, c) for r in range(rows) for c in range(cols)])

    # create a dist matrix
    dist = [[float('inf')] * cols for _ in range(rows)]
    
    # initialize distances with source node
    dist[0][0] = data[0][0]
    # change source from unvisited to visited
    visited_nodes.add((0, 0))
    unvisited_nodes.remove((0, 0))

    end = (rows - 1, cols - 1)
    queue = {}
    while end not in visited_nodes:

        # 1. From each of the visisted nodes, determine adjacent nodes (only unvisited nodes)
        for node in visited_nodes:
            r = node[0]
            c = node[1]
            node_cost = dist[r][c]

            adj_left = tuple((r, c - 1))
            adj_right = tuple((r, c + 1))
            adj_up = tuple((r - 1, c))
            adj_down = tuple((r + 1, c))

            temp = [adj_left, adj_right, adj_up, adj_down]
            valid_adjacents = [x for x in temp if x in unvisited_nodes]

            # 2. Determine the cost to get to each node
            for adj in valid_adjacents:
                adj_cost = node_cost + data[adj[0]][adj[1]]

                # 3. Add each of those values to a queue
                if adj not in queue:
                    queue[adj] = adj_cost

                queue[adj] = min(queue[adj], adj_cost)

        min_val = float('inf')
        min_loc = (-1, -1)  # choose an out of bounds location
        for node, val in queue.items():
            r_node = node[0]
            c_node = node[1]

            # 4. Compare each key, item in the queue to the value in dist, take the smallest value
            dist[r_node][c_node] = min(dist[r_node][c_node], val)

            # 5. Find the min val in the queue and extract the value and location key
            if val < min_val:
                min_val = val
                min_loc = node

        # 6. Remove the min_loc from the unvisited_nodes and add to visited_nodes
        unvisited_nodes.remove(min_loc)
        visited_nodes.add(min_loc)
        queue.pop(min_loc)

        if __print:
            print_mat(dist, "dist")

    return dist[end[0]][end[1]]


# my_data = [
#     [131,   673,    234,    103,    18],
#     [201,   96,     342,    965,    150],
#     [630,   803,    746,    422,    111],
#     [537,   699,    497,    121,    956],
#     [805,   732,    524,    37,     331]
# ]

# dijkstra(my_data, __print=True)

matrix = extract_matrix()
ans = dijkstra(matrix, False)
print(f"{ans=}")

print(f"{time.time() - t} sec")

# Performance improvements
# - Queue
#       - currently I calculate the queue independently each time
#       - it would be nice to know if those calculations already exist, and not clear the queue each time
#       - I think that it is currently a lot of calculations that are being repeated,
#       and they will grow as the number of adjacent nodes increases
