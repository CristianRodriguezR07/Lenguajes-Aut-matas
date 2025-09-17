"""Exercise 4 - Directed graph visualization (Student: Jonathan Lanchero).

This module draws the automaton for exercise 4. It exposes a run() function.
"""
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import networkx as nx

def draw_automaton() -> None:
    """Build and draw the directed graph for exercise 4."""
    G = nx.DiGraph()
    states = ["q0", "q1", "q2"]
    initial_state = "q0"
    final_states = ["q0"]

    transitions: List[Tuple[str, str, str]] = [
        ("q0", "q1", "1"),
        ("q1", "q0", "0"),
        ("q0", "q2", "0"),
        ("q2", "q0", "1"),
    ]

    for src, dst, label in transitions:
        if G.has_edge(src, dst):
            G[src][dst]["label"] += f", {label}"
        else:
            G.add_edge(src, dst, label=label)

    pos: Dict[str, Tuple[float, float]] = {
        "q0": (0, 0),
        "q1": (2, 0),
        "q2": (1, -1.5),
    }

    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="white", edgecolors="black")
    nx.draw_networkx_nodes(G, pos, nodelist=final_states, node_size=1300,
                           node_color="white", edgecolors="black", linewidths=2.5)
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight="bold")
    nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.2", arrows=True, arrowstyle="->")
    edge_labels = {(src, dst): G[src][dst]["label"] for src, dst in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.6)
    plt.annotate("", xy=pos[initial_state], xytext=(-1, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    plt.axis("off")
    plt.show()

def run() -> None:
    """Public entrypoint for exercise 4."""
    draw_automaton()

if __name__ == '__main__':
    run()
