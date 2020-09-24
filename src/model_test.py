from unittest import TestCase
from .model import Node, link, Link, connect
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

        fixed = dijkstra(self.start)
        for node, (d, prev) in fixed.items():
            # d, prev = v
            print(f'{node.name}: {d} prev={prev.name}')

    def testLink(self):
        l00 = Link("L00", 0)
        l01 = Link("L01", 3)
        l02 = Link("L02", 8)
        l12 = Link("L12", 4)
        l13 = Link("L13", 2)
        l14 = Link("L14", 9)
        l23 = Link("L23", 1)
        l24 = Link("L24", 3)
        l34 = Link("L34", 3)
        l35 = Link("L35", 7)
        l37 = Link("L37", 9)
        l46 = Link("L46", 5)
        l47 = Link("L47", 19)
        l56 = Link("L56", 5)
        l58 = Link("L58", 12)
        l67 = Link("L67", 14)
        l68 = Link("L68", 10)
        l78 = Link("L78", 3)

        all_links = (l00, l01, l02, l12, l13, l14, l35, l46, l47, l58,
                     l37, l47, l67, l68, l78)

        start, end = True, False
        connect({l00: end, l01: start, l02: start})
        connect({l01: end, l12: start, l13: start, l14: start})
        connect({l02: end, l12: end, l23: start, l24: start})
        connect({l13: end, l23: end, l34: start, l35: start})
        connect({l14: end, l24: end, l34: end, l46: start, l47: start})
        connect({l35: end, l56: start, l58: start})
        connect({l46: end, l56: end, l67: start, l68: start})
        connect({l37: end, l67: end, l78: start})
        connect({l58: end, l68: end, l78: end})

        l00.walk_to(l00, 0, start)

        for ln in all_links:
            print(ln)
