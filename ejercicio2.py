"""Exercise 2 - PDA visualization (Student: Cristian Rodriguez).

Draws a PDA using networkx and matplotlib. The module exposes run().
"""
from typing import List, Tuple, Dict
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyArrowPatch

def draw_pda() -> None:
    """Draw the PDA diagram for exercise 2."""
G = nx.DiGraph()
states = ["q0", "q1", "q2", "q3"]
initial_state = "q0"
final_states = ["q0"]

transitions = [
    ("q0", "q0", "c"),
    ("q0", "q1", "a"),
    ("q0", "q2", "b"),
    ("q1", "q0", "a"),
    ("q1", "q1", "c"),
    ("q1", "q3", "b"),
    ("q2", "q1", "a"),
    ("q2", "q2", "b"),
    ("q3", "q0", "a"),
    ("q3", "q3", "b"),
]
for src, dst, label in transitions:
    if G.has_edge(src, dst):
        G[src][dst]["label"] += f", {label}"
    else:
        G.add_edge(src, dst, label=label)
pos = {
    "q0": (0, 0),
    "q1": (3, 0),
    "q2": (1.5, 2.5),
    "q3": (1.5, -2.5),
}
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="white", edgecolors="black")
nx.draw_networkx_nodes(G, pos, nodelist=final_states, node_size=1300,
                       node_color="white", edgecolors="black", linewidths=2.5)
nx.draw_networkx_labels(G, pos, font_size=11, font_weight="bold")
nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.25", arrows=True, arrowstyle="->")
edge_labels = {(src, dst): G[src][dst]["label"]
               for src, dst in G.edges if src != dst}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
loop_offsets = {
    "q0": (0, 0.6),  
    "q1": (0, 0.6),
    "q2": (0, 0.6),
    "q3": (0, -0.6), 
}
for node, offset in loop_offsets.items():
    label = G[node][node]["label"]
    x, y = pos[node]
    plt.text(x + offset[0], y + offset[1], label,
             fontsize=11, fontweight="bold", ha="center")
plt.annotate("",
             xy=pos[initial_state],     
             xytext=(-1.8, 0),         
             arrowprops=dict(arrowstyle="->", lw=1.5))
plt.axis("off")
plt.show()

def run() -> None:
    """Public entrypoint for exercise 2."""
    draw_pda()

if __name__ == '__main__':
    run()
