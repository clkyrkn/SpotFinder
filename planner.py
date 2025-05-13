import heapq

class AStarPlanner:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.height = len(grid)
        self.width = len(grid[0])
        self.directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Left, right, up, down

    def heuristic(self, a, b):
        # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_walkable(self, x, y):
        return self.grid[y][x] == 0

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def plan(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}

        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            for dx, dy in self.directions:
                neighbor = (current[0] + dx, current[1] + dy)
                x, y = neighbor

                if not self.in_bounds(x, y) or not self.is_walkable(x, y):
                    continue

                tentative_g_score = g_score[current] + 1  # Cost of all movements 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None  # Path not found
