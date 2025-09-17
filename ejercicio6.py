"""Exercise 6 - Detailed automaton drawing (Student: Yury Dorado).

This module uses matplotlib primitives for precise control of node placement
and edge shapes. It exposes a run() function.
"""
from matplotlib.patches import FancyArrowPatch, Circle
import matplotlib.pyplot as plt

def draw_automaton() -> None:
    """Draw the automaton for exercise 6 using matplotlib patches."""
    pos = {
        "q0": (0.15, 0.80),
        "q1": (0.45, 0.82),
        "q2": (0.48, 0.45),
        "q3": (0.72, 0.45),
        "q4": (0.95, 0.45),
    }

    node_radius = 0.065
    node_facecolor = "#fff8d6"
    edge_color = "black"

    fig, ax = plt.subplots(figsize=(11,6))
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0.15, 0.95)

    # Draw nodes
    for name, (x, y) in pos.items():
        circ = Circle((x, y), node_radius, facecolor=node_facecolor,
                      edgecolor=edge_color, linewidth=2, zorder=3)
        ax.add_patch(circ)

    # Final state q4: double circle
    x4, y4 = pos["q4"]
    outer = Circle((x4, y4), node_radius + 0.013, facecolor="none",
                   edgecolor=edge_color, linewidth=2.8, zorder=3)
    ax.add_patch(outer)

    # Labels
    for name, (x, y) in pos.items():
        ax.text(x, y, name, fontsize=14, fontweight="bold", ha="center", va="center", zorder=5)

    def curved_arrow(p_from, p_to, rad=0.0, lw=1.8, label=None, label_offset=(0,0), txt_rot=0):
        arr = FancyArrowPatch(p_from, p_to, connectionstyle=f"arc3,rad={rad}", arrowstyle='->',                              mutation_scale=20, linewidth=lw, color=edge_color, shrinkA=10, shrinkB=10, zorder=2)
        ax.add_patch(arr)
        if label:
            lx = (p_from[0] + p_to[0]) / 2 + label_offset[0]
            ly = (p_from[1] + p_to[1]) / 2 + label_offset[1]
            ax.text(lx, ly, label, fontsize=10, ha="center", va="center", rotation=txt_rot, zorder=6)

    def self_loop(center, rad=0.5, dx_label=0.0, dy_label=0.12, label="", loop_width=1.6):
        x, y = center
        start = (x - node_radius*0.20, y + node_radius*0.95)
        end = (x + node_radius*0.20, y + node_radius*0.95)
        arr = FancyArrowPatch(start, end, connectionstyle=f"arc3,rad={rad}", arrowstyle='->',                              mutation_scale=18, linewidth=loop_width, color=edge_color, shrinkA=0, shrinkB=0, zorder=2)
        ax.add_patch(arr)
        if label:
            ax.text(x + dx_label, y + dy_label, label, fontsize=9, ha="center", va="center", zorder=6)

    # q0 loops
    self_loop(pos["q0"], rad=0.70, dx_label=-0.02, dy_label=0.165, label="a, a ; aa", loop_width=1.8)
    self_loop(pos["q0"], rad=0.42, dx_label=+0.02, dy_label=0.125, label="a, Z ; aZ", loop_width=1.6)

    # q0 -> q1
    curved_arrow((pos["q0"][0] + node_radius*0.6, pos["q0"][1]), (pos["q1"][0] - node_radius*0.6, pos["q1"][1]),
                 rad=0.08, lw=1.8, label="a ; ba", label_offset=(0, 0.035))

    # q1 loop
    self_loop(pos["q1"], rad=0.62, dx_label=0.01, dy_label=0.165, label="b, b ; bb", loop_width=1.8)

    # q1 -> q2 (large descent)
    curved_arrow((pos["q1"][0], pos["q1"][1] - node_radius*0.1),
                 (pos["q2"][0] - node_radius*0.45, pos["q2"][1] + node_radius*0.45),
                 rad=-0.85, lw=1.9, label="c, b ; λ", label_offset=(0.12, 0.05), txt_rot=-20)

    # q2 loop and q2 -> q3
    self_loop(pos["q2"], rad=0.55, dx_label=-0.02, dy_label=0.12, label="c, b ; λ", loop_width=1.6)
    curved_arrow((pos["q2"][0] + node_radius*0.5, pos["q2"][1]), (pos["q3"][0] - node_radius*0.5, pos["q3"][1]),
                 rad=0.06, lw=1.8, label="a, a ; λ", label_offset=(-0.02, 0.035))

    # q3 loop and q3 -> q4
    self_loop(pos["q3"], rad=0.50, dx_label=0.00, dy_label=0.12, label="a, a ; λ", loop_width=1.6)
    curved_arrow((pos["q3"][0] + node_radius*0.6, pos["q3"][1]), (pos["q4"][0] - node_radius*0.6, pos["q4"][1]),
                 rad=0.06, lw=1.8, label="λ, Z ; λ", label_offset=(+0.02, 0.03))

    # Start arrow
    arrow_start = (pos["q0"][0] - 0.14, pos["q0"][1])
    arrow_end = (pos["q0"][0] - node_radius*0.65, pos["q0"][1])
    ax.annotate("", xy=arrow_end, xytext=arrow_start, arrowprops=dict(arrowstyle="->", linewidth=2.2, color=edge_color), zorder=1)

    ax.set_aspect('equal')
    ax.axis("off")
    plt.tight_layout()
    plt.show()

def run() -> None:
    """Public entrypoint for exercise 6."""
    draw_automaton()

if __name__ == '__main__':
    run()
