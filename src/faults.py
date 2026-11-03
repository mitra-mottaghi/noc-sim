import random

from src.topology import build_mesh


def random_link_faults(rows, cols, k, seed=0):
    """Pick k random mesh links to fail. A link is frozenset({a, b})."""
    edges = list(build_mesh(rows, cols).edges)
    rng = random.Random(seed)
    return {frozenset(e) for e in rng.sample(edges, k)}
