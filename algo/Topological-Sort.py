# BOJ 2252 - 줄 세우
# 일부 학생의 키 비교 결과로 줄 세우기

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        indegree[b-1] += 1


    def topological_sort():
        nonlocal graph, indegree

        queue = deque()
        result = []

        for x in range(n):
            if not indegree[x]:
                queue.append(x)

        while queue:
            node = queue.popleft()
            result.append(node + 1)

            for connected_node in graph[node]:
                indegree[connected_node] -= 1

                if not indegree[connected_node]:
                    queue.append(connected_node)

        return result

    res = topological_sort()
    print(*res)

if __name__ == "__main__":
    solve()
