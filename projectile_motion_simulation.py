import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Dict


class ProjectileSimulator:
    def __init__(self, gravity: float = 9.81):
        self.g = gravity

    def calculate_trajectory(self, velocity: float, angle_degrees: float) -> Dict[str, np.ndarray]:
        theta = np.radians(angle_degrees)

        v_x = velocity * np.cos(theta)
        v_y = velocity * np.sin(theta)

        t_total = (2 * v_y) / self.g
        t_steps = np.linspace(0, t_total, num=100)

        x_points = v_x * t_steps
        y_points = (v_y * t_steps) - (0.5 * self.g * t_steps ** 2)

        return {
            "time": t_steps,
            "x": x_points,
            "y": y_points,
            "max_range": np.max(x_points),
            "max_height": np.max(y_points)
        }

    def run_multi_angle_analysis(self, velocity: float, angles: list) -> None:
        plt.figure(figsize=(10, 6))

        for angle in angles:
            data = self.calculate_trajectory(velocity, angle)
            plt.plot(data["x"], data["y"], label=f"{angle}° (Range: {data['max_range']:.1f}m)")

        plt.title(f"Projectile Trajectory Analysis - v={velocity}m/s")
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.axhline(0, color='black', lw=1)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()

        plt.savefig("projectile_analysis.png", dpi=300)
        plt.show()


if __name__ == "__main__":
    sim = ProjectileSimulator()
    sim.run_multi_angle_analysis(35.0, [30, 45, 60, 75])