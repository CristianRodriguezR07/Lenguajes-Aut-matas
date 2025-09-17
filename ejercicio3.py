"""Exercise 3 - Directed graph visualization (Student: Cristian Rodriguez).

This module draws a directed automaton using networkx and matplotlib.
The visualization was refactored to follow PEP8 and includes a `run()` entrypoint.
"""
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import networkx as nx

def draw_automaton() -> None:
    """Build and draw the directed graph for exercise 3."""
    G = nx.DiGraph()
    states = ["q0", "q1", "q2", "q3", "q4"]
    initial_state = "q0"
    final_states = ["q0", "q3"]

    transitions: List[Tuple[str, str, str]] = [
        ("q0", "q1", "0"),
        ("q0", "q2", "1"),
        ("q1", "q0", "0"),
        ("q1", "q2", "1"),
        ("q1", "q4", "1"),
        ("q2", "q1", "1"),
        ("q2", "q4", "0"),
        ("q4", "q3", "0"),
        ("q3", "q4", "0"),
        ("q4", "q2", "0"),
    ]

    for src, dst, label in transitions:
        if G.has_edge(src, dst):
            G[src][dst]["label"] += f", {label}"
        else:
            G.add_edge(src, dst, label=label)

    pos: Dict[str, Tuple[float, float]] = {
        "q0": (0, 0),
        "q1": (2, 0),
        "q2": (2, -2),
        "q4": (4, 0),
        "q3": (4, -2),
    }

    # Draw nodes and final-state double circles
    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="white", edgecolors="black")
    nx.draw_networkx_nodes(G, pos, nodelist=final_states, node_size=1300,
                           node_color="white", edgecolors="black", linewidths=2.5)
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight="bold")
    nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.2", arrows=True, arrowstyle="->")
    edge_labels = {(src, dst): G[src][dst]["label"] for src, dst in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.65)
    plt.annotate("", xy=pos[initial_state], xytext=(-1.2, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    plt.axis("off")
    plt.show()

def run() -> None:
    """Public entrypoint for exercise 3."""
    draw_automaton()

if __name__ == '__main__':
    run()
