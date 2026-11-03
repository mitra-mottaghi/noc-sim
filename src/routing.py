def xy_route(src, dst):
    """Return the XY path from src to dst (X first, then Y)."""
    x, y = src
    dx, dy = dst
    path = [src]
    while x != dx:
        x += 1 if dx > x else -1
        path.append((x, y))
    while y != dy:
        y += 1 if dy > y else -1
        path.append((x, y))
    return path


def next_hop(cur, dst, queues, routing="xy", failed=frozenset()):
    """Next router, or None if the needed link(s) have failed."""
    x, y = cur
    dx, dy = dst
    cand = []
    if x != dx:
        cand.append((x + (1 if dx > x else -1), y))
    if y != dy:
        cand.append((x, y + (1 if dy > y else -1)))
    if routing == "xy":
        n = cand[0]
        return None if frozenset((cur, n)) in failed else n
    cand = [n for n in cand if frozenset((cur, n)) not in failed]
    if not cand:
        return None
    return min(cand, key=lambda n: len(queues[n]))


if __name__ == "__main__":
    print(xy_route((0, 0), (3, 2)))
