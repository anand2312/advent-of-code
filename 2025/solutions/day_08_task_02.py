import bisect
from itertools import combinations

from helpers import Puzzle
from day_08_task_01 import Point, Edge


puzzle = Puzzle(day=8)


def main(lines: list[str]) -> int:
    pts = [Point(*[int(i) for i in line.split(",")]) for line in lines]
    edges: list[Edge] = []

    for p1, p2 in combinations(pts, 2):
        bisect.insort(edges, p1.edge_to(p2), key=lambda p: - p.length)

    dsu = list(set([pt]) for pt in pts)

    while len(dsu) > 1:
        edge = edges.pop()
        a, b = edge.pts
        if any(a in s and b in s for s in dsu):
            # cycle
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
        
        if len(dsu) == 1:
            return edge.pts[0].x * edge.pts[1].x


if __name__ == "__main__":
    print(main(puzzle.sample_lines()))
    print(main(puzzle.lines()))