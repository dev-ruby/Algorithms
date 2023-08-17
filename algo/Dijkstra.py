# BOJ 1753 - 최단경로
# 한 점 K부터 다른 모든 점까지의 최단경로 구하기

import sys
import math
import heapq

MAX = math.inf
MIN = -math.inf

input = lambda: sys.stdin.readline().rstrip()

def solve():
    v, e = map(int, input().split())
    k = int(input()) - 1

    graph = [[] for _ in range(v)]

    for _ in range(e):
        _u, _v, _w = map(int, input().split())
        graph[_u-1].append((_v-1, _w))

    def dijkstra(start):
        dist = [MAX for _ in range(v)]

        dist[start] = 0

        queue = [(0, start)]

        while queue:
            current_dist, current_node = heapq.heappop(queue)

            if dist[current_node] < current_dist:
                continue

            for new_node, new_dist in graph[current_node]:
                new_dist += current_dist

                if new_dist < dist[new_node]:
                    dist[new_node] = new_dist
                    heapq.heappush(queue, (new_dist, new_node))

        return dist

    distances = dijkstra(k)
    for d in distances:
        if d == math.inf:
            print("INF")
        else:
            print(d)

if __name__ == "__main__":
    solve()
