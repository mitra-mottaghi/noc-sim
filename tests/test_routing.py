from src.routing import xy_route
from src.topology import build_mesh


def test_xy_path_uses_only_mesh_links():
    mesh = build_mesh(4, 4)
    path = xy_route((0, 0), (3, 2))
    assert path[0] == (0, 0) and path[-1] == (3, 2)
    for a, b in zip(path, path[1:]):
        assert mesh.has_edge(a, b)
