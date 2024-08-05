import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, end: bool) -> None:
        self.isend = end
        self.child = dict()


class Trie(object):
    def __init__(self) -> None:
        self.head = Node(False)

    def add(self, s) -> None:
        cur = self.head
        for c in s:
            if not cur.child.get(c):
                cur.child[c] = Node(False)
            cur = cur.child[c]
        cur.isend = True

    def find(self, s) -> None:
        cur = self.head
        for c in s:
            if not cur.child.get(c):
                return False
            cur = cur.child[c]
        return cur.isend


def dfs(depth: int, node: Node) -> None:
    cur = node
    for i in sorted(cur.child):
        print("-" * (2 * depth) + i)
        dfs(depth + 1, cur.child[i])


n = int(input())
t = Trie()
for _ in range(n):
    k, *food = input().split()
    t.add(food)
dfs(0, t.head)
