#BOJ 17387 - 선분 교차 2
#선분 교차 판

import sys

input = lambda: sys.stdin.readline().rstrip()


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)

    def __ge__(self, other):
        return (self.x, self.y) >= (other.x, other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


def ccw(p1: Point, p2: Point, p3: Point) -> int:
    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.x * p1.y - p3.x * p2.y - p1.x * p3.y


def is_crossing(l1: Line, l2: Line) -> bool:
    a, b, c, d = l1.p1, l1.p2, l2.p1, l2.p2
    abc = ccw(a, b, c)
    abd = ccw(a, b, d)
    cda = ccw(c, d, a)
    cdb = ccw(c, d, b)

    if abc * abd == 0 and cda * cdb == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c

        if a <= d and c <= b:
            return True
        else:
            return False

    if abc * abd <= 0 and cda * cdb <= 0:
        return True
    else:
        return False

def solve():
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, x4, y4 = list(map(int, input().split()))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)

    l1 = Line(p1, p2)
    l2 = Line(p3, p4)

    print(int(is_crossing(l1, l2)))


if __name__ == "__main__":
    solve()
