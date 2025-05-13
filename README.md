
# SpotFinder – Autonomous Parking Path Planner

A personal project that implements a search-based algorithm to simulate autonomous vehicle parking. It uses the A* algorithm to compute optimal, collision-free paths on customizable 2D grid maps.

---

## Project Overview

**SpotFinder** is a simulation-based path planning system for autonomous parking. It features procedural map generation with obstacle zones, dynamic visualization of the computed path, and feasibility checks using Breadth-First Search (BFS).

---

## Project Structure

```
spotfinder/
├── assets/                 ← Folder to store generated visuals (e.g. path plots)
│ └── path_example.png
├── grid_map.py             ← Map generation and grid layout definitions
├── main.py                 ← Main entry point for running the simulation
├── planner.py              ← A* path planning algorithm implementation
├── visualizer.py           ← Functions for static and animated visualization
└── README.md               ← This file
```

---

## Features

- Implements **A\*** algorithm to find shortest feasible path to parking spot
- Uses **NumPy** arrays to represent grid environments
- **Matplotlib FuncAnimation** for step-by-step path visualization
- **BFS** used to verify if target is reachable from start
- Supports **procedural generation** of obstacle maps

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/clkyrkn/SpotFinder.git
cd SpotFinder
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the simulation:

```bash
python main.py
```

---

## Sample Output

Final path is drawn step-by-step using animation.

If map is unsolvable, you’ll receive a “Path not found” message with unreachable grid visualized.

---

## Example Output

![Sample Path](assets/sample_output.png)

## Tech Stack

- Python
- NumPy
- Matplotlib

---

## Author

**Yarkin Colak**  
ML & Simulation Enthusiast | CE Student @ RWTH Aachen

---

## Future Improvements

- Add GUI with PyQt or Tkinter  
- Allow user-defined start/goal positions  
- Implement D* or RRT for advanced planning
