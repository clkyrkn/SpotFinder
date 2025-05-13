import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def draw_path(grid, path, start, goal):
    height = len(grid)
    width = len(grid[0])

    # Convert map data to NumPy array (0: empty, 1: obstacle)
    map_data = np.array(grid)

    # Color map (cmap): 0 = white, 1 = black
    plt.figure(figsize=(width / 2, height / 2))
    plt.imshow(map_data, cmap='gray_r')

    # Path drawing (if available)
    if path:
        xs = [p[0] for p in path]
        ys = [p[1] for p in path]
        plt.plot(xs, ys, color='blue', linewidth=2, label='Path')

    # Starting and destination points
    plt.scatter(start[0], start[1], color='green', s=100, marker='o', label='Start')
    plt.scatter(goal[0], goal[1], color='red', s=100, marker='X', label='Goal')

    # Display settings
    plt.xticks(range(width))
    plt.yticks(range(height))
    plt.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--')
    plt.gca().invert_yaxis()
    plt.legend()
    plt.title("A* Path Planning")
    plt.tight_layout()
    plt.show()

def animate_path(grid, path, start, goal, interval=200):
    height = len(grid)
    width = len(grid[0])
    map_data = np.array(grid)

    fig, ax = plt.subplots(figsize=(width / 2, height / 2))
    ax.imshow(map_data, cmap='gray_r')
    ax.set_xticks(range(width))
    ax.set_yticks(range(height))
    ax.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--')
    ax.invert_yaxis()
    ax.set_title("A* Path Animation")

    # Draw start and target points
    ax.scatter(start[0], start[1], color='green', s=100, marker='o', label='Start')
    ax.scatter(goal[0], goal[1], color='red', s=100, marker='X', label='Goal')
    point, = ax.plot([], [], 'bs', markersize=12, label='Agent')  # Blue square

    # Road line (visible when completed)
    if path:
        xs = [p[0] for p in path]
        ys = [p[1] for p in path]
        ax.plot(xs, ys, color='blue', linewidth=1, alpha=0.3)

    def update(frame):
        if frame < len(path):
            x, y = path[frame]
            point.set_data(x, y)
        return point,

    ani = animation.FuncAnimation(fig, update, frames=len(path), interval=interval, blit=True, repeat=False)
    ax.legend()
    plt.show()
