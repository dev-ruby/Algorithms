# BOJ 2042 - 구간 합 구하기
# 배열에서 구간 합, 숫자 변경 쿼리 처리하기

import math
import sys


class SegmentTree:
    def __init__(self, n: int, numbs: list[int], op, default: int):
        self.number_count = n
        self.height = math.ceil(math.log2(n))
        self.tree_size = 1 << (self.height + 1)
        self.tree = [0 for _ in range(self.tree_size)]

        self.numbs = numbs

        self.default = default

        self.operator = op

        self.initialize()

    def initialize(self):
        self.__initialize(1, 0, self.number_count - 1)

    def __initialize(self, node, start, end):
        if start == end:
            self.tree[node] = self.numbs[start]
        else:
            self.__initialize(node * 2, start, (start + end) // 2)
            self.__initialize(node * 2 + 1, (start + end) // 2 + 1, end)

            self.tree[node] = self.operator(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, node, start, end, index, val):
        if index < start or index > end:
            return

        if start == end:
            self.numbs[index] = val
            self.tree[node] = val
            return

        self.update(node * 2, start, (start + end) // 2, index, val)
        self.update(node * 2 + 1, (start + end) // 2 + 1, end, index, val)

        self.tree[node] = self.operator(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return self.default

        if left <= start and end <= right:
            return self.tree[node]

        left_query = self.query(node * 2, start, (start + end) // 2, left, right)
        right_query = self.query(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

        return self.operator(left_query, right_query)


input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)


def solve():
    n, m, k = map(int, input().split())

    nums = [int(input()) for _ in range(n)]

    def add(x, y):
        return x + y

    segment_tree = SegmentTree(n, nums, add, 0)

    queries = [(tuple(map(int, input().split()))) for _ in range(m + k)]

    for _query in queries:
        query_type, b, c = _query

        if query_type == 1:
            segment_tree.update(1, 0, n - 1, b - 1, c)
        elif query_type == 2:
            print(segment_tree.query(1, 0, n - 1, b - 1, c - 1))


if __name__ == "__main__":
    solve()
