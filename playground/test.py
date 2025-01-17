from typing import cast

import networkx as nx
from rich import box, print
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty
from rich.style import Style
from rich.table import Table

from netext import TerminalGraph
from netext.edge_routing.modes import EdgeRoutingMode
from netext.edge_rendering.modes import EdgeSegmentDrawingMode
from netext.edge_rendering.arrow_tips import ArrowTip
from netext.node_rasterizer import JustContent

n = 10  # 10 nodes
m = 20  # 20 edges
seed = 20160  # seed random number generators for reproducibility

# Use seed for reproducibility
# g = nx.gnm_random_graph(n, m, seed=seed)

g = cast(nx.Graph, nx.binomial_tree(5))
g1 = cast(nx.DiGraph, nx.paley_graph(5))


def _render(n, d, s):
    t = Table(title=n)

    t.add_column("Key")
    t.add_column("Val")

    for key, val in d.items():
        t.add_row(key, Pretty(val))

    return t


nx.set_node_attributes(g1, JustContent(), "$shape")
nx.set_node_attributes(g1, _render, "$content-renderer")


def _render2(n, d, s):
    return f"#N{n}"


nx.set_node_attributes(g, Style(color="blue"), "$content-style")
nx.set_node_attributes(g, box.SQUARE, "$box-type")
nx.set_edge_attributes(g, Style(color="red"), "$style")
nx.set_edge_attributes(g, EdgeRoutingMode.ORTHOGONAL, "$edge-routing-mode")
nx.set_edge_attributes(g, EdgeSegmentDrawingMode.BOX, "$edge-segment-drawing-mode")
nx.set_edge_attributes(g, ArrowTip.ARROW, "$end-arrow-tip")
nx.set_edge_attributes(g, ArrowTip.ARROW, "$start-arrow-tip")

# nx.set_edge_attributes(g, "foo", "$label")
nx.set_node_attributes(g, _render2, "$content-renderer")
nx.set_node_attributes(g, True, "$show")

# nx.set_edge_attributes(g, False, "$show")
g.edges[8, 10]["$show"] = True

print(Panel(TerminalGraph(g), title="Binomial Tree", expand=False))
print(Panel(TerminalGraph(g1), title="Payley Graph", expand=False))

console = Console(record=True, width=80, height=60)

g = cast(nx.Graph, nx.binomial_tree(3))

nx.set_node_attributes(g, Style(color="blue"), "$style")
nx.set_node_attributes(g, box.SQUARE, "$box-type")

nx.set_edge_attributes(g, Style(color="red"), "$style")
nx.set_edge_attributes(g, EdgeRoutingMode.ORTHOGONAL, "$edge-routing-mode")
nx.set_edge_attributes(g, EdgeSegmentDrawingMode.BOX, "$edge-segment-drawing-mode")
nx.set_edge_attributes(g, ArrowTip.ARROW, "$end-arrow-tip")
nx.set_edge_attributes(g, ArrowTip.ARROW, "$start-arrow-tip")

# nx.set_edge_attributes(g, "foo", "$label")
nx.set_node_attributes(g, _render2, "$content-renderer")
nx.set_node_attributes(g, True, "$show")

console.print(TerminalGraph(g, console=console))
console.save_svg("test.svg", title="Binomial Tree")
