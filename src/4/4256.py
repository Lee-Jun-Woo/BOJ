import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def postorder(prs: int, pre: int, ins: int, ine: int) -> None:
    if (prs > pre) or (ins > ine):
        return

    root = preorder[prs]

    if prs < pre:
        iroot = idx[root]
        postorder(prs + 1, iroot + prs - ins, ins, iroot - 1)
        postorder(pre - ine + iroot + 1, pre, iroot + 1, ine)

    print(root, end=" ")


for _ in range(int(input())):
    n = int(input())
    preorder = tuple(map(int, input().split()))
    inorder = tuple(map(int, input().split()))

    idx = [0] * (n + 1)
    for i in range(n):
        idx[inorder[i]] = i

    postorder(0, n - 1, 0, n - 1)
    print()
