# TLE error, whoops, accidently came up with DFS lol.


List = list

class Solution:
    min_cost = float('inf')
    def get_results(self, n, costs, path=[], cost=0):
        paths = []
        if len(path) > 0:
            cur_step = path[-1]
        else:
            cur_step = 0

        if cur_step == n:
            if cost < self.min_cost:
                self.min_cost = cost
            return [cost, path]
        
        for i in range(1, 3 + 1):
            next_step = cur_step + i
            next_path = path.copy() + [next_step]
            if next_step <= len(costs):
                next_cost = cost + costs[next_step - 1] + (next_step - cur_step) ** 2
                if next_cost < self.min_cost:
                    paths.append(self.get_results(
                        n,
                        costs,
                        next_path,
                        next_cost
                    ))
            else:
                break
        
        # print(paths)

        #return min(sub[0] for sub in paths)
        min_path = [float('inf'), path.copy()]
        for p in paths:
            if p[0] <= min_path[0]:
                min_path = p.copy()
        return min_path
    def climbStairs(self, n: int, costs: List[int]) -> int:
        self.min_cost = float('inf')
        return self.get_results(n, costs)[0]
