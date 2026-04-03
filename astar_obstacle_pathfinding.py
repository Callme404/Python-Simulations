import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from typing import List, Tuple, Optional, Dict


class Node:
    def __init__(self, position: Tuple[int, int], parent: Optional['Node'] = None):
        self.position = position
        self.parent = parent
        self.g = 0.0
        self.h = 0.0
        self.f = 0.0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.position == other.position

    def __lt__(self, other: 'Node') -> bool:
        return self.f < other.f


class AStarSimulator:
    def __init__(self, grid_size: Tuple[int, int], obstacle_ratio: float = 0.2):
        self.width, self.height = grid_size
        self.grid = np.zeros((self.height, self.width), dtype=int)
        self._generate_obstacles(obstacle_ratio)

    def _generate_obstacles(self, ratio: float) -> None:
        num_obstacles = int(self.width * self.height * ratio)
        for _ in range(num_obstacles):
            x, y = np.random.randint(0, self.width), np.random.randint(0, self.height)
            self.grid[y, x] = 1

    def _heuristic(self, current: Tuple[int, int], goal: Tuple[int, int]) -> float:
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        self.grid[start[1], start[0]] = 0
        self.grid[end[1], end[0]] = 0

        start_node = Node(start)
        end_node = Node(end)

        open_list: List[Node] = []
        closed_set: set = set()
        g_costs: Dict[Tuple[int, int], float] = {start: 0.0}

        heapq.heappush(open_list, start_node)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while open_list:
            current_node = heapq.heappop(open_list)

            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]

            closed_set.add(current_node.position)

            for dx, dy in directions:
                neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)

                if not (0 <= neighbor_pos[0] < self.width and 0 <= neighbor_pos[1] < self.height):
                    continue
                if self.grid[neighbor_pos[1], neighbor_pos[0]] == 1 or neighbor_pos in closed_set:
                    continue

                cost = 1.414 if dx != 0 and dy != 0 else 1.0
                tentative_g = current_node.g + cost

                if neighbor_pos not in g_costs or tentative_g < g_costs[neighbor_pos]:
                    g_costs[neighbor_pos] = tentative_g
                    neighbor_node = Node(neighbor_pos, current_node)
                    neighbor_node.g = tentative_g
                    neighbor_node.h = self._heuristic(neighbor_pos, end_node.position)
                    neighbor_node.f = neighbor_node.g + neighbor_node.h
                    heapq.heappush(open_list, neighbor_node)

        return None

    def visualize(self, start: Tuple[int, int], end: Tuple[int, int], path: Optional[List[Tuple[int, int]]]) -> None:
        vis_grid = np.copy(self.grid)
        if path:
            for step in path:
                vis_grid[step[1], step[0]] = 2

        vis_grid[start[1], start[0]] = 3
        vis_grid[end[1], end[0]] = 4

        cmap = ListedColormap(['white', 'black', 'royalblue', 'limegreen', 'crimson'])
        plt.figure(figsize=(8, 8))
        plt.imshow(vis_grid, cmap=cmap)

        plt.title("A* Pathfinding Simulation")
        plt.xticks([])
        plt.yticks([])

        legend_elements = [
            Patch(facecolor='limegreen', label='Start'),
            Patch(facecolor='crimson', label='End'),
            Patch(facecolor='royalblue', label='Path'),
            Patch(facecolor='black', label='Obstacle')
        ]
        plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.2, 1))

        plt.tight_layout()
        plt.savefig("astar_result.png")
        plt.show()


if __name__ == "__main__":
    params = {"size": (30, 30), "start": (2, 2), "end": (27, 27)}

    sim = AStarSimulator(grid_size=params["size"], obstacle_ratio=0.25)
    path = sim.find_path(params["start"], params["end"])

    if path:
        print(f"Path found: {len(path)} steps.")
    else:
        print("No path possible.")

    sim.visualize(params["start"], params["end"], path)