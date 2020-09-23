from .model import Node
import heapq


def dijkstra(nodes, start):
    fixed = {}
    nearest = [(0, start, start)]
    heapq.heapify(nearest)

    while nearest:
        dist, node, prev = heapq.heappop(nearest)
        if node not in fixed:
            fixed[node] = (dist, prev)

        for nb, d in node.links().items():
            if nb not in fixed:
                heapq.heappush(nearest, (d + dist, nb, node))

    return fixed
