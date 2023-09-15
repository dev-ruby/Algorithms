# BOJ 14725 - 개미굴
# 트라이 렌더링하기

import sys

input = lambda: sys.stdin.readline().rstrip()


class Node:
    def __init__(self, value, data=None, children=None):
        if children is None:
            children = {}

        self.value = value
        self.data = data
        self.children = children


class Trie:
    def __init__(self) -> None:
        self.root = Node(None)

    def insert_value(self, value) -> None:
        current = self.root

        for s in value:
            if s not in current.children:
                current.children[s] = Node(s)

            current = current.children[s]

        current.data = value

    def query(self, value) -> bool:
        current = self.root

        for s in value:
            if s in current.children:
                current = current.children[s]
            else:
                return False

        if current.data:
            return True
        else:
            return False

    def render(self, node=None, depth=0) -> None:
        if node:
            print("-" * (depth - 1) * 2 + node.value)
        else:
            node = self.root

        for key in sorted(list(node.children.keys())):
            self.render(node=node.children[key], depth=depth + 1)


def solve():
    trie = Trie()

    for _ in range(int(input())):
        n, *lst = input().split()

        trie.insert_value(lst)

    trie.render()


if __name__ == "__main__":
    solve()
