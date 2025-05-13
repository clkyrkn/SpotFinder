from grid_map import GridMap
from planner import AStarPlanner
from visualizer import draw_path


def main():
    
    # 1. Create the map
    gm = GridMap(width=10, height=10, obstacle_prob=0.7)  
    gm.print_map()

    # 2. Start path planner
    planner = AStarPlanner(gm.grid, gm.start, gm.goal)
    path = planner.plan()

    # 3. seeing in action (without animation):
    if path:                                                
        draw_path(gm.grid, path, gm.start, gm.goal)      

    # 4.Check the result
    if path:
        print(f"\n Road found! Length: {len(path)}")
        print(f"Path: {path}")
    else:
        print("\n Path not found.")

if __name__ == "__main__":
    main()