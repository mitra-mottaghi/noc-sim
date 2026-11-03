import random
from collections import deque
from dataclasses import dataclass

from src.routing import xy_route


@dataclass
class Packet:
    src: tuple
    dst: tuple
    created: int
    path: list
    hop: int = 0


def simulate(rows, cols, rate, cycles, seed=0):
    """Cycle-based NoC simulation with XY routing.

    rate: probability that each node injects a packet per cycle.
    Each router forwards one packet (queue head) per cycle.
    """
    rng = random.Random(seed)
    nodes = [(x, y) for x in range(cols) for y in range(rows)]
    queues = {n: deque() for n in nodes}
    latencies = []

    for t in range(cycles):
        # 1) inject new packets (uniform random destination)
        for n in nodes:
            if rng.random() < rate:
                dst = rng.choice([m for m in nodes if m != n])
                queues[n].append(Packet(n, dst, t, xy_route(n, dst)))

        # 2) each router sends its head packet one hop
        moving = [queues[n].popleft() for n in nodes if queues[n]]
        for p in moving:
            p.hop += 1
            here = p.path[p.hop]
            if here == p.dst:
                latencies.append(t + 1 - p.created)
            else:
                queues[here].append(p)

    delivered = len(latencies)
    return {
        "rate": rate,
        "delivered": delivered,
        "avg_latency": sum(latencies) / delivered if delivered else 0.0,
        "throughput": delivered / (len(nodes) * cycles),
    }


if __name__ == "__main__":
    for r in [0.02, 0.05, 0.1, 0.2, 0.3]:
        res = simulate(4, 4, r, 5000)
        print(f"rate={r:<5} latency={res['avg_latency']:.2f}  "
              f"throughput={res['throughput']:.3f}")
