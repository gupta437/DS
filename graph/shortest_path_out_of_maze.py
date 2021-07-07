"""
We have considered BFS and DFS graph traversal algorithms in the previous lectures.
You task is to design an algorithms with breadth-first search that is able to find the shortest path from a
given source to a given destination. The maze is represented by a two-dimensional list.

[
   [S, 1, 1, 1, 1],
   [0, 1, 1, 1, 1],
   [0, 0, 0, 0, 1],
   [1, 0, 1, 1, 1],
   [0, 0, 0, 1, D]
]

The (0,0) is the source and (4,4) is the destination. 0 represents walls or obstacles and 1 is the
valid cells we can include in the solution.

Complexities:
    Time:
    Space:

"""


def shortest_path(maze, src, end):
    if maze[src[0]][src[1]] == 0 or maze[end[0]][end[1]] == 0:
        return []

    visited = set()
    min_dist = 0
    queue = [(src, 0)]

    while queue:
        curr_cell, dist = queue.pop(0)
        visited.add((curr_cell[0], curr_cell[1]))
        if curr_cell == end:
            return dist

        row = curr_cell[0]
        col = curr_cell[1]

        for i, j in [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]:
            if is_valid(i, j, maze, len(maze), len(maze[0]), visited):
                queue.append(([i, j], dist + 1))

    return min_dist


def is_valid(row, col, maze, num_rows, num_cols, visited_nodes):
    if row < 0 or row >= num_rows:
        return False

    if col < 0 or col >= num_cols:
        return False

    if (row, col) in visited_nodes:
        return False

    if maze[row][col] == 0:
        return False

    return True


def main():
    maze = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]
    print(shortest_path(maze, [0, 0], [4, 4]))


if __name__ == "__main__":
    main()
