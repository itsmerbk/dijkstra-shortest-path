import heapq

def dijkstra(graph, src, dst):
    dist, prev, pq = {src: 0}, {}, [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")): continue
        if u == dst: break
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v], prev[v] = nd, u; heapq.heappush(pq, (nd, v))
    path, cur = [], dst
    while cur in prev or cur == src:
        path.append(cur)
        if cur == src: break
        cur = prev[cur]
    return dist.get(dst, float("inf")), path[::-1]

if __name__ == "__main__":
    g = {"A": [("B", 4), ("C", 1)], "C": [("B", 2), ("D", 5)], "B": [("D", 1)], "D": []}
    assert dijkstra(g, "A", "D") == (4, ["A", "C", "B", "D"])
    print("[PASS] 011_dijkstra_shortest_path")
