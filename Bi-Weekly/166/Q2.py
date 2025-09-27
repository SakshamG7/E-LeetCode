# TLE error, sad.

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # costs[j] + (j - i)**2
        graph = {}
        dist = {}
        for i in range(len(costs) + 1):
            graph[str(i)] = {}
            dist[str(i)] = float("inf")
            c = 1
            while len(costs) - i - c >= 0 and c < 4:
                # graph[str(i)].append(i + c)
                graph[str(i)][str(i+c)] = costs[i + c - 1] + c**2
                c += 1
        unvisited = set(graph.keys())
        start = '0'
        end = str(n)
        dist[start] = 0
        while unvisited:
            # cur = list(unvisited)[0]
            # find the next cheapest node
            # c = dist[cur]
            # for n in unvisited:
            #     if dist[n] < c:
            #         cur = n
            #         c = dist[n]
            cur = min(unvisited, key=lambda node: dist[node])
            if dist[cur] == float('inf'):
                # print(cur, "end as its equal to inf")
                break
            if cur == end:
                break
            unvisited.remove(cur)
            for next, weight in graph[cur].items():
                if next in unvisited:
                    n_dist = dist[cur] + weight
                    if n_dist < dist[next]:
                        dist[next] = n_dist
        return dist[end]