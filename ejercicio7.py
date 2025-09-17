"""Exercise 7 - PDA rendering with graphviz (Student: Yury Dorado).

This module generates a Graphviz DOT file and renders it to a PNG file.
Graphviz system binaries must be installed for rendering to work.
"""
from typing import List, Tuple, Dict
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyArrowPatch

def draw_pda() -> None:
    """Draw the PDA diagram for exercise 7."""
G = nx.DiGraph()
states = ["q0", "q1", "q2"]
initial_state = "q0"
final_states = ["q2"]
transitions = [
    ("q0", "q0", "b,Z;bZ\nb,a;λ\nb,b;bb\na,b;λ\na,a;aa\na,Z;aZ"),
    ("q0", "q1", "λ,Z;Z\nλ,a;λ"),
    ("q1", "q1", "λ,a;λ"),
    ("q1", "q2", "λ,Z;λ"),
]
for src, dst, label in transitions:
    if G.has_edge(src, dst):
        G[src][dst]["label"] += f"\n{label}"
    else:
        G.add_edge(src, dst, label=label)
pos = {"q0": (0, 0), "q1": (3, 0), "q2": (6, 0)}
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="lightyellow", edgecolors="black")
nx.draw_networkx_nodes(G, pos, nodelist=final_states, node_size=1300,
                       node_color="lightyellow", edgecolors="black", linewidths=2.5)
nx.draw_networkx_labels(G, pos, font_size=11, font_weight="bold")
nx.draw_networkx_edges(
    G, pos,
    connectionstyle="arc3,rad=0.25",  
    arrows=True,
    arrowstyle="->",
    arrowsize=15,
    width=1
)
nx.draw_networkx_edges(
    G, pos,
    edgelist=[("q0", "q0"), ("q1", "q1")],
    connectionstyle="arc3,rad=-0.4",  
    arrows=True,
    arrowstyle="->",
    arrowsize=15,
    width=1
)
edge_labels = {(src, dst): G[src][dst]["label"] for src, dst in G.edges}
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels,
    font_size=9,
    label_pos=0.6 
)
plt.annotate("", xy=pos[initial_state], xytext=(-1.0, 0),
             arrowprops=dict(arrowstyle="->", lw=1, mutation_scale=15))
plt.axis("off")
plt.show()

def run() -> None:
    """Public entrypoint for exercise 7."""
    draw_pda()

if __name__ == '__main__':
    run()
