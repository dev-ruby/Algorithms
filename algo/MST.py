# BOJ 1197 - 최소 스패닝 트리
# 그래프에서 최소 스패닝 트리 찾기

import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    v, e = map(int, input().split())
    graph = []
    parent = [i for i in range(v)]

    def check(a, b):
        return find(a) == find(b)

    def find(x):
        nonlocal parent

        if parent[x] == x:
            return x

        parent[x] = find(parent[x])

        return parent[x]

    def union(a, b):
        a_root = find(a)
        b_root = find(b)

        if a_root > b_root:
            parent[b_root] = a_root
        else:
            parent[a_root] = b_root

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph.append((a-1, b-1, c))

    graph.sort(key = lambda x: x[-1], reverse=True)

    count = 0
    mst = 0

    while True:
        a, b, c = graph.pop()
        if not check(a, b):
            count += 1
            mst += c

            union(a, b)

        if count == v-1:
            break

    print(mst)


if __name__ == "__main__":
    solve()
