from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:        
        flight_graph = defaultdict(list)

        for f_src,f_dst,price in flights:
            flight_graph[f_src].append((f_dst,price))

        total_cost = float("inf")
        min_cost = {}
        queue = deque([(src,0,0)])

        while queue:
            cur,cur_price,stops = queue.popleft()

            if cur == dst:
                total_cost = min(total_cost,cur_price)
                continue

            if stops > k:
                continue

            if cur in min_cost and min_cost[cur] <= cur_price:
                continue
            min_cost[cur] = cur_price

            for path,price in flight_graph[cur]:
                if cur_price + price < total_cost:
                    queue.append((path,cur_price + price,stops + 1))

        return total_cost if total_cost != float("inf") else -1