def triangle_solver(triangle: str):
    triangle = triangle.splitlines()
    sum_tri = []
    for row in triangle:
        line = row.split()
        line = [int(x) for x in line]
        sum_tri.append(line)
    for n in range(len(sum_tri) - 2, -1, -1):
        for i in range(len(sum_tri[n])):
            sum_tri[n][i] += max(sum_tri[n+1][i], sum_tri[n+1][i+1])
    return sum_tri[0][0]
