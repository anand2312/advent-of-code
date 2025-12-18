import bisect
from dataclasses import dataclass
from itertools import combinations
from math import sqrt, dist
from pprint import pprint

from helpers import Puzzle


puzzle = Puzzle(day=8)


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int
    z: int

    def edge_to(self, other: Point) -> Edge:
        l = dist((self.x, self.y, self.z), (other.x, other.y, other.z))
        return Edge(length=l, pts=(self, other))


@dataclass(eq=False)
class Edge:
    length: float
    pts: tuple[Point, Point]

    def __eq__(self, other: Edge) -> bool:
        return self.pts == other.pts or (self.pts[1], self.pts[0]) == other.pts

    
def main(lines: list[str], n_edges: int) -> int:
    pts = [Point(*[int(i) for i in line.split(",")]) for line in lines]
    edges: list[Edge] = []

    for p1, p2 in combinations(pts, 2):
        bisect.insort(edges, p1.edge_to(p2), key=lambda p: - p.length)

    dsu = list(set([pt]) for pt in pts)
    count = 0
    while count < n_edges:
        edge = edges.pop()
        a, b = edge.pts
        if any(a in s and b in s for s in dsu):
            # cycle
            count += 1
            continue
        
        for s in dsu:
            if a in s:
                set_a = s
                continue
            if b in s:
                set_b = s
                continue
        
        set_a.update(set_b)
        dsu.remove(set_b)
        count += 1
    
    sizes = sorted([len(s) for s in dsu], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]
            

if __name__ == "__main__":
    print(main(puzzle.sample_lines(), 10))
    print(main(puzzle.lines(), 1000))