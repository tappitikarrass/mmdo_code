def north_west_corner(supply, demand):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    i = 0
    j = 0
    bfs = []
    while len(bfs) < len(supply) + len(demand) - 1:
        s = supply_copy[i]
        d = demand_copy[j]
        v = min(s, d)
        supply_copy[i] -= v
        demand_copy[j] -= v
        bfs.append(((i, j), v))
        if supply_copy[i] == 0 and i < len(supply) - 1:
            i += 1
        elif demand_copy[j] == 0 and j < len(demand) - 1:
            j += 1
    return bfs

def main():
    costs = [[4, 5, 6, 8, 10],
             [10, 3, 2, 3, 15],
             [4, 10, 5, 1, 16],
             [0, 0, 0, 0, 0]]
    supply = [110, 30, 50, 80, 90]
    demand = [130, 90, 40, 100]

    bfs = north_west_corner(supply, demand)
    
    for i in bfs:
        print(i)

    matrix = list()
    for i in range(len(demand)):
        matrix.append(list())
        for j in range(len(supply)):
            matrix[i].append(0)

    f = 0
    for i in bfs:
        x=i[0][1]
        y=i[0][0]
        matrix[x][y] = i[1]
        f += costs[x][y] * i[1]

    print()
    for i in range(len(matrix)):
        print(matrix[i])
    print(f"F = {f}")
        

if __name__ == "__main__":
    main()
