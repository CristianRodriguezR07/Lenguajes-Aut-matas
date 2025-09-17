"""Exercise 5 - Directed graph visualization (Student: Jonathan Lanchero).

This module draws the automaton for exercise 5 and exposes run().
"""
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import networkx as nx

def draw_automaton() -> None:
    """Build and draw the directed graph for exercise 5."""
    G = nx.DiGraph()
    initial_state = "q0"
    final_states = ["q4"]

    transitions: List[Tuple[str, str, str]] = [
        ("q0", "q1", "1"),
        ("q0", "q2", "0"),
        ("q1", "q2", "0"),
        ("q1", "q4", "1"),
        ("q2", "q3", "1"),
        ("q2", "q4", "0"),
        ("q3", "q2", "0"),
        ("q3", "q4", "1"),
    ]

    for src, dst, label in transitions:
        if G.has_edge(src, dst):
            G[src][dst]["label"] += f", {label}"
        else:
            G.add_edge(src, dst, label=label)

    pos: Dict[str, Tuple[float, float]] = {
        "q0": (0, 0),
        "q1": (0, -2),
        "q2": (2, 0),
        "q3": (2, -2),
        "q4": (4, -1),
    }

    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="white", edgecolors="black")
    nx.draw_networkx_nodes(G, pos, nodelist=final_states, node_size=1300,
                           node_color="white", edgecolors="black", linewidths=2.5)
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight="bold")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, connectionstyle="arc3,rad=0.15", arrows=True, arrowstyle="->", width=1.5)
    edge_labels = {(src, dst): G[src][dst]["label"] for src, dst in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.55)

    # Draw large self-loops for q4 with annotations using plt.annotate for clarity
    x, y = pos["q4"]
    plt.annotate("0", xy=(x, y), xytext=(x + 0.4, y + 0.06),
                 arrowprops=dict(arrowstyle="->", lw=2, connectionstyle="arc3,rad=0.8"),
                 fontsize=11, ha="center")
    plt.annotate("1", xy=(x, y), xytext=(x - 0.3, y - 0.3),
                 arrowprops=dict(arrowstyle="->", lw=2, connectionstyle="arc3,rad=-0.8"),
                 fontsize=11, ha="center")

    plt.annotate("", xy=pos[initial_state], xytext=(-1, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    plt.axis("off")
    plt.show()

def run() -> None:
    """Public entrypoint for exercise 5."""
    draw_automaton()

if __name__ == '__main__':
    run()
