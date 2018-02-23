from heapq import heappush, heappop
from collections import defaultdict

t = int(raw_input())
for q in range(t):
    n, m = map(int, raw_input().split())
    edges = [map(int, raw_input().split()) for i in range(m)]
    adj = defaultdict(list)
    for u, v, s, l in edges:
        adj[u].append((v, 1.0 * l / s))
    pq = [(0, 1)]
    vis = set()
    while len(pq) > 0:
        cost, u = heappop(pq)
        if u == n:
            print int(cost + 0.5)
            break
        if u in vis:
            continue
        vis.add(u)
        for v, c in adj[u]:
            heappush(pq, (cost + c, v))
