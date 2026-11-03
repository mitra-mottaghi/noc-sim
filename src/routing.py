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


if __name__ == "__main__":
    print(xy_route((0, 0), (3, 2)))
