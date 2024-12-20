from collections import defaultdict, deque


class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q = deque([1])
        cur_time = 0
        res = -1
        visit_times = defaultdict(list)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:
                        return cur_time
                    res = cur_time

                for nei in adj[node]:
                    nei_times = visit_times[nei]
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        visit_times[nei].append(cur_time)
            
            if (cur_time // change) % 2 == 1:
                cur_time += change - (cur_time % change)
            cur_time += time

        return res

n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5
obj = Solution()
print(obj.secondMinimum(n, edges, time, change))