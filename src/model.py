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
    start = True
    end = False

    def __init__(self, name, length):
        self.name = name
        self._length = length

        self._connects = {
            self.start: {},  # starts { ln: start_of_ln }
            self.end: {},  # ends { ln: start_of_ln }
        }
        self._dist = {
            self.start: 10000,
            self.end: 10000,
        }
        self._prev = None

    def connects(self, start, connects):
        self._connects[start] = connects

    def walk_to(self, prev, dist, start):
        self._dist[start] = dist

        if self._dist[not start] <= dist + self._length:
            self._prev = None
            return

        self._prev = (prev, start)
        self._dist[not start] = dist + self._length

        for ln, st in self._connects[not start].items():
            ln.walk_to(self, dist + self._length, st)

    def __repr__(self):
        return f'{self.name}: {self._dist[self.start]} {self._dist[self.end]}, prev={self._prev}'


def connect(links):
    for ln, start in links.items():
        ls = {k: v for k, v in links.items() if k is not ln}
        ln.connects(start, ls)
