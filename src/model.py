class Node:
    def __init__(self, name):
        self.name = name
        self._links = {}
        self._prev = None
        self._dist = 100000

    def link(self, node, dist):
        self._links[node] = dist

    def dist(self):
        return self._dist

    def links(self):
        return self._links

    def walk_to(self, prev, dist):
        if self._dist > dist:
            self._prev = prev
            self._dist = dist
            [nb.walk_to(nb, dist + d) for nb, d in self._links.items() if nb is not prev]

    def __repr__(self):
        return f'{self.name}: {self._dist} prev={self._prev.name}'

    def __gt__(self, other):
        return self.name > other.name


def link(a, b, dist):
    a.link(b, dist)
    b.link(a, dist)


class Link:

    def __init__(self, name, length):
        self.name = name
        self._length = length

        self._connects = {
            True: {},  # starts { ln: start_of_ln }
            False: {},  # ends { ln: start_of_ln }
        }
        self._direction = None  # True if start => end
        self._dist = 100000

    def connect(self, start, ln , start_of_ln):
        self._connects[start][ln] = start_of_ln

    def walk_to(self, prev, dist, start):
        if self._dist > dist:
            for ln, st in self._connects[not start].items():
                if ln is not prev:
                    ln.walk_to(ln, dist + self._length, st)


