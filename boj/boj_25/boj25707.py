n = int(input())
beads = list(map(int, input().split()))
print((max(beads) - min(beads)) * 2)