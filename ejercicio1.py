"""Exercise 1 - PDA visualization (Student: Cristian Rodriguez).

This module draws a PDA-like directed graph using networkx and matplotlib.
A callable `run()` function is provided as entrypoint.
"""
from typing import Dict, Tuple, List
import networkx as nx
import matplotlib.pyplot as plt

def draw_pda() -> None:
    """Draw the PDA diagram for exercise 1."""
    G = nx.DiGraph()
    states = ["1", "2", "3", "4"]
    initial_state = "1"
    final_state = "4"
    transitions: List[Tuple[str, str, str]] = [
        ("1", "2", "0"),
        ("1", "3", "1"),
        ("2", "4", "1"),
        ("3", "4", "0"),
        ("4", "1", "0"),
        ("4", "2", "1"),
    ]
    for src, dst, label in transitions:
        G.add_edge(src, dst, label=label)
    pos: Dict[str, Tuple[float, float]] = {"1": (0, 0), "2": (2, 1), "3": (2, -1), "4": (4, 0)}
    nx.draw_networkx_nodes(G, pos, node_size=1800, node_color="white", edgecolors="black")
    nx.draw_networkx_nodes(G, pos, nodelist=[final_state], node_size=2000, node_color="white", edgecolors="black", linewidths=3)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
    nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.2", arrows=True)
    edge_labels = {(src, dst): label for src, dst, label in transitions}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    plt.annotate("", xy=pos[initial_state], xytext=(-0.5, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    plt.axis("off")
    plt.show()

def run() -> None:
    """Public entrypoint for exercise 1."""
    draw_pda()

if __name__ == '__main__':
    run()
