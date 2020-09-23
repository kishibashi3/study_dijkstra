from unittest import TestCase
from .model import Node, link
from .dykstra import dijkstra


class TestGraph(TestCase):

    def setUp(self):

        n0 = Node("N0")
        n1 = Node("N1")
        n2 = Node("N2")
        n3 = Node("N3")
        n4 = Node("N4")
        n5 = Node("N5")
        n6 = Node("N6")
        n7 = Node("N7")
        n8 = Node("N8")

        link(n0, n1, 3)
        link(n0, n2, 8)
        link(n1, n2, 4)
        link(n1, n3, 2)
        link(n1, n4, 9)
        link(n2, n3, 1)
        link(n2, n4, 3)
        link(n3, n4, 3)
        link(n3, n5, 7)
        link(n3, n6, 9)
        link(n4, n6, 5)
        link(n4, n7, 19)
        link(n5, n6, 5)
        link(n5, n8, 12)
        link(n6, n7, 14)
        link(n6, n8, 10)
        link(n7, n8, 3)

        self.all_nodes = (n0, n1, n2, n3, n4, n5, n6, n7, n8)
        self.start = n0

    def testDomain(self):
        self.start.walk_to(self.start, 0)

        for n in self.all_nodes:
            print(n)

    def testDijkstra(self):

        fixed = dijkstra(self.all_nodes, self.start)
        for node, v in fixed.items():
            d, prev = v
            print(f'{node.name}: {d} prev={prev.name}')

