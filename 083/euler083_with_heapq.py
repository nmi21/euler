import time
import os
import heapq

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


def dijkstra(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize distance matrix with infinity
    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[0][0] = matrix[0][0]

    # Priority queue to store cells and their corresponding distances
    priority_queue = [(matrix[0][0], (0, 0))]

    # Define directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while priority_queue:
        dist, (row, col) = heapq.heappop(priority_queue)

        # Check neighbors
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                new_dist = dist + matrix[r][c]
                if new_dist < distance[r][c]:
                    distance[r][c] = new_dist
                    heapq.heappush(priority_queue, (new_dist, (r, c)))

    # Return the minimal path sum for the bottom-right cell
    return distance[rows - 1][cols - 1]


matrix = extract_matrix()
ans = dijkstra(matrix)
print(f"{ans=}")

print(f"{time.time() - t} sec")