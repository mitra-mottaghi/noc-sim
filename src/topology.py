import networkx as nx
import matplotlib.pyplot as plt


def build_mesh(rows: int, cols: int) -> nx.Graph:
    """Build a 2D mesh. Each node is a router at (x, y)."""
    G = nx.grid_2d_graph(cols, rows)  # nodes are (x, y)
    for node in G.nodes:
        G.nodes[node]["pos"] = node
    return G


def draw_mesh(G: nx.Graph, path: str | None = None) -> None:
    pos = {n: n for n in G.nodes}
    nx.draw(G, pos, with_labels=True, node_color="lightblue",
            node_size=700, font_size=8)
    if path:
        plt.savefig(path, dpi=200, bbox_inches="tight")
    else:
        plt.show()


if __name__ == "__main__":
    mesh = build_mesh(4, 4)
    print("Routers:", mesh.number_of_nodes())
    print("Links:", mesh.number_of_edges())
    draw_mesh(mesh, "docs/mesh_4x4.png")