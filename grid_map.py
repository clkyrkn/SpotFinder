import random
from collections import deque

class GridMap:
    def __init__(self, width=10, height=10, obstacle_prob=0.25,
                 start=(0, 0), goal=(9, 9), randomize=True):
        self.width = width
        self.height = height
        self.start = start
        self.goal = goal
        self.obstacle_prob = obstacle_prob

        if randomize:
            self.grid = self.generate_random_grid()
        else:
            self.grid = self.default_grid()

    def default_grid(self):
        return [
            [0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
        ]

    def generate_random_grid(self):
        while True:
            grid = []
            for y in range(self.height):
                row = []
                for x in range(self.width):
                    if (x, y) == self.start or (x, y) == self.goal:
                        row.append(0)
                    else:
                        row.append(1 if random.random() < self.obstacle_prob else 0)
                grid.append(row)

            if self.is_reachable(grid):
                return grid

    def is_reachable(self, grid):
        visited = [[False] * self.width for _ in range(self.height)]
        queue = deque([self.start])
        visited[self.start[1]][self.start[0]] = True

        while queue:
            x, y = queue.popleft()
            if (x, y) == self.goal:
                return True

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if not visited[ny][nx] and grid[ny][nx] == 0:
                        visited[ny][nx] = True
                        queue.append((nx, ny))
        return False

    def print_map(self):
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                if (x, y) == self.start:
                    row += 'S '
                elif (x, y) == self.goal:
                    row += 'G '
                elif self.grid[y][x] == 1:
                    row += '█ '
                else:
                    row += '. '
            print(row)


