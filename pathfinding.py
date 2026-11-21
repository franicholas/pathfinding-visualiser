def manhattan_distance(current, goal):
    distance = abs(current[0] - goal[0]) + abs(current[1] - goal[1])
    return distance

def is_inside_grid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def get_valid_neighbours(position, rows, cols, walls):
    row, col = position

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbours = []

    for d in directions:
        dr, dc = d[0], d[1]
        neib_row = row + dr
        neib_col = col + dc

        if is_inside_grid(neib_row, neib_col, rows, cols) and (neib_row, neib_col) not in walls:#
            neighbours.append((row + dr, col + dc))


    return neighbours


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()

    return path

def bfs(start, goal, rows, cols, walls):
    queue = [start]
    visited = {start}
    came_from = {start: None}
    exploration_order = []


    while queue:

        current = queue.pop(0)
        exploration_order.append(current)


        if current == goal:
            return reconstruct_path(came_from, start, goal), visited, exploration_order

        neighbours = get_valid_neighbours(current, rows, cols, walls)

        for neighbour in neighbours:

            if neighbour not in visited:

                came_from[neighbour] = current
                queue.append(neighbour)
                visited.add(neighbour)

    return [], visited, exploration_order

def astar(start, goal, rows, cols, walls):

    open_set = [start]
    came_from = {start: None}
    g_cost = {start: 0}
    f_cost = {start: manhattan_distance(start, goal)}
    visited = set()
    exploration_order = []

    while open_set: 
        current = open_set[0]
        for cell in open_set:
            if f_cost[cell] < f_cost[current]:
                current = cell

        open_set.remove(current)
        visited.add(current)
        exploration_order.append(current)

        if current == goal:
            return reconstruct_path(came_from, start, goal), visited, exploration_order

        for neighbour in get_valid_neighbours(current, rows, cols, walls):


            tentative_g = g_cost[current] + 1

            if neighbour not in g_cost or tentative_g < g_cost[neighbour]:
                g_cost[neighbour] = tentative_g
                f_cost[neighbour] = g_cost[neighbour] + manhattan_distance(neighbour, goal)
                came_from[neighbour] = current

                if neighbour not in open_set:
                    open_set.append(neighbour)

    return [], visited, exploration_order

if __name__ == "__main__":

    walls = {(1, 2), (2, 2), (3, 1)}

    start = (0, 0)
    goal = (4, 4)

    rows = 5
    cols = 5

    bfs_path, bfs_visited = bfs(start, goal, rows, cols, walls)
    astar_path, astar_visited = astar(start, goal, rows, cols, walls)

    print("BFS path length:", len(bfs_path) - 1)
    print("A* path length:", len(astar_path) - 1)

    print("BFS explored:", len(bfs_visited))
    print("A* explored:", len(astar_visited))