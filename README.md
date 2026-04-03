# Python-Simulations
A collection of simulations using NumPy and Matplotlib.

1. Projectile Trajectory Analysis
**File:** `projectile_motion.py`

A kinematic simulation that calculates and compares the flight paths of projectiles at varying launch angles. 

### Key Features:
* **Vectorized Mathematics:** Instead of using iterative loops, this script uses **NumPy** to calculate 100+ position coordinates simultaneously across the time domain.
* **Data Visualization:** Uses **Matplotlib** to generate a professional-grade comparison plot, showing how different angles affect the total displacement (range) and peak height.
* **Mathematical Foundation:** Implements the classic kinematic equation: 
  $$y = v_0 \sin(\theta)t - \frac{1}{2}gt^2$$



---

## 2. A* Pathfinding Simulation
**File:** `astar_simulator.py`

A grid-based implementation of the A* search algorithm, commonly used in game AI for NPC navigation, but here applied as a standalone coordinate-based simulation.

### Key Features:
* **Optimized Search:** Uses the **A* heuristic formula** ($f = g + h$) and a **Priority Queue** (`heapq`) to ensure the most efficient path is calculated with minimal node exploration.
* **Environment Modeling:** The search space is managed as a **NumPy matrix**, allowing for efficient boundary checking and obstacle placement.
* **Graphical Output:** Generates a mapped representation of the environment, identifying the start point, end point, obstacles, and the resulting optimal path.



---

## Technical Requirements
To run these simulations, you will need Python 3.8+ and the following libraries:
* **NumPy:** For high-performance array operations.
* **Matplotlib:** For data plotting and visualization.
