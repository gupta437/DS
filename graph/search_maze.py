def search_maze(maze, src, end):
    if maze[src[0]][src[1]] == 0 or maze[end[0]][end[1]] == 0:
        return []

    path = []
    dfs(src, maze, path, end)
    return path


def dfs(curr, maze, path, end):
    if not is_valid(curr[0], curr[1], maze, len(maze), len(maze[0])):
        return False

    path.append(curr)
    maze[curr[0]][curr[1]] = 0
    if list(curr) == end:
        return True

    row = curr[0]
    col = curr[1]

    if any(
            dfs((x, y), maze, path, end)
            for x, y in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]):
        return True


def is_valid(row, col, maze, num_rows, num_cols):
    if not 0 <= row < num_rows:
        return False

    if not 0 <= col < num_cols:
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
    print(search_maze(maze, [0, 0], [4, 4]))


if __name__ == "__main__":
    main()
