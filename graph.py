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


def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(node):
        neighbors = []
        row, col = node

        delta_row = [-1, -2, -1, -2, 1, 2, 1, 2]
        delta_col = [-2, -1, 2, 1, -2, -1, 2, 1]

        for i in range(len(delta_row)):
            new_row = row + delta_row[i]
            new_col = col + delta_col[i]
            neighbors.append((new_row, new_col))
        return neighbors

    def bfs(start):
        queue = deque([start])
        visited = set()
        steps = 0

        while len(queue) > 0:
            no_of_possible_moves = len(queue)
            for _ in range(no_of_possible_moves):
                curr_move = queue.popleft()
                if curr_move[0] == x and curr_move[1] == y:
                    return steps
                for neighbor in get_neighbors(curr_move):
                    if neighbor in visited:
                        continue
                    visited.add(curr_move)
                    queue.append(neighbor)

            steps += 1

    # Knight starts at 0, 0
    return bfs((0, 0))


#                  Down    Up       Right   Left
possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 2147483647


# Parse all our gates and fan out to all of its neighbors incrementing by one
def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    def get_neighbors(x, y):
        neighbors = []
        # Right
        if x + 1 < len(dungeon_map):
            neighbors.append((x + 1, y))
        # Left
        if x - 1 >= 0:
            neighbors.append((x - 1, y))
        # Below
        if y + 1 < len(dungeon_map[y]):
            neighbors.append((x, y + 1))
        # Above
        if y - 1 >= 0:
            neighbors.append((x, y - 1))

        return neighbors

    queue = deque()
    width, height = len(dungeon_map), len(dungeon_map[0])
    # Add all the gates to our queue
    for r in range(width):
        for c in range(height):
            if dungeon_map[r][c] == 0:
                queue.append((r, c))
    # Find all the valid neighbors of the gates, if they are inf then change them to the amount of steps
    while len(queue) > 0:
        x, y = queue.popleft()
        for neighbor in get_neighbors(x, y):
            neighbor_x, neighbor_y = neighbor
            if dungeon_map[neighbor_x][neighbor_y] == INF:
                dungeon_map[neighbor_x][neighbor_y] = dungeon_map[x][y] + 1
                queue.append(neighbor)
    return dungeon_map


def openLock(self, deadends: List[str], target: str) -> int:
    def find_neighbors(combo):
        neighbors = []
        # Increment by one and decrement by one in each "cycle" which give us 8 total possible combinations
        for i in range(4):
            # 0000
            # Modify the digit in place by adding it by one and modulating by 10
            # module 10 will give us 0 if we are incrementing from 9 to 10
            incremented_digit = str((int(combo[i]) + 1) % 10)
            neighbors.append(combo[:i] + incremented_digit + combo[i + 1:])
            # Add by ten to negate the negative and give us the proper number
            decremented_digit = str(((int(combo[i]) - 1) + 10) % 10)
            neighbors.append(combo[:i] + decremented_digit + combo[i + 1:])
        return neighbors

    def bfs():
        # our queue will hold the turns and current combination
        queue = deque()
        queue.append(("0000", 0))
        # Deadends will be marked as visited so we will skip them
        visited = set(deadends)

        while queue:
            combo, turns = queue.popleft()
            # We found the combo in our queue
            if combo == target:
                return turns
            # Find our neighbors, dont have to check if deadend because its included in our visited
            for neighbor in find_neighbors(combo):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, turns + 1))
        return -1

    if target in deadends or '0000' in deadends:
        return -1
    return bfs()
