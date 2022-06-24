from collections import deque
from typing import List


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    def get_neighbors(node):
        return graph[node]

    def bfs(start, target):
        queue = deque([start])
        visited = set([start])
        length = 0
        while len(queue) > 0:
            no_of_nodes = len(queue)

            for _ in range(no_of_nodes):
                curr_node = queue.popleft()
                if curr_node == target:
                    return length

                for neighbor in get_neighbors(curr_node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            length += 1
        return length

    return bfs(a, b)


def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    def get_neighbor(x, y):
        neighbors = []
        # Right
        if x + 1 < len(image[x]):
            neighbors.append((x + 1, y))
        # Left
        if x - 1 >= 0:
            neighbors.append((x - 1, y))
        # Below
        if y + 1 < len(image[y]):
            neighbors.append((x, y + 1))
        # Above
        if y - 1 >= 0:
            neighbors.append((x, y - 1))

        return neighbors

    def bfs(x, y):
        queue = deque([(r, c)])
        color_to_change = image[r][c]
        while len(queue) > 0:
            no_of_pixels = len(queue)

            for _ in range(no_of_pixels):
                curr_x, curr_y = queue.popleft()
                if image[curr_x][curr_y] == replacement or image[curr_x][curr_y] != color_to_change:
                    continue
                image[curr_x][curr_y] = replacement
                # Append neighbors
                for neighbor in get_neighbor(curr_x, curr_y):
                    queue.append(neighbor)

    if image[r][c] != replacement:
        bfs(r, c)
    return image


def count_number_of_islands(grid: List[List[int]]) -> int:
    def get_neighbors(x, y):
        neighbors = []
        # Right
        if x + 1 < len(grid):
            neighbors.append((x + 1, y))
        # Left
        if x - 1 >= 0:
            neighbors.append((x - 1, y))
        # Below
        if y + 1 < len(grid[0]):
            neighbors.append((x, y + 1))
        # Above
        if y - 1 >= 0:
            neighbors.append((x, y - 1))

        return neighbors

    # Includes diagonals
    def bfs(start):
        queue = deque([start])
        row, col = start
        grid[row][col] = 0
        # Find neighbors and set them to 0 if they are part of the island
        while len(queue) > 0:
            row, col = queue.popleft()
            for neighbor in get_neighbors(row, col):
                # We can set this to our first neighbor because we already handled it above
                row, col = neighbor
                # Edge of the island - We don't want the neighbors
                if grid[row][col] == 0:
                    continue
                queue.append(neighbor)
                grid[row][col] = 0

    num_islands = 0
    rows = len(grid)
    columns = len(grid[0])
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            num_islands += 1
    return num_islands
