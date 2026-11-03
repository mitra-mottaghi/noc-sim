import random
from collections import deque
from dataclasses import dataclass

from src.routing import next_hop


@dataclass
class Packet:
    src: tuple
    dst: tuple
    created: int
    cur: tuple


def pick_dst(n, nodes, traffic, rng):
    if traffic == "transpose":          # needs a square mesh
        x, y = n
        return (y, x) if (y, x) != n else None
    return rng.choice([m for m in nodes if m != n])   # uniform


def simulate(rows, cols, rate, cycles, routing="xy", traffic="uniform",
             seed=0, failed_links=frozenset()):
    rng = random.Random(seed)
    nodes = [(x, y) for x in range(cols) for y in range(rows)]
    queues = {n: deque() for n in nodes}
    latencies = []
    dropped = 0

    for t in range(cycles):
        for n in nodes:
            if rng.random() < rate:
                dst = pick_dst(n, nodes, traffic, rng)
                if dst is not None:
                    queues[n].append(Packet(n, dst, t, n))

        moving = [queues[n].popleft() for n in nodes if queues[n]]
        for p in moving:
            nxt = next_hop(p.cur, p.dst, queues, routing, failed_links)
            if nxt is None:          # blocked by a failed link
                dropped += 1
                continue
            p.cur = nxt
            if p.cur == p.dst:
                latencies.append(t + 1 - p.created)
            else:
                queues[p.cur].append(p)

    delivered = len(latencies)
    total = delivered + dropped
    return {
        "rate": rate,
        "delivered": delivered,
        "dropped": dropped,
        "delivery_ratio": delivered / total if total else 1.0,
        "avg_latency": sum(latencies) / delivered if delivered else 0.0,
        "throughput": delivered / (len(nodes) * cycles),
    }


if __name__ == "__main__":
    for routing in ["xy", "adaptive"]:
        res = simulate(4, 4, 0.1, 5000, routing, "uniform")
        print(routing, f"latency={res['avg_latency']:.2f}",
              f"throughput={res['throughput']:.3f}")
