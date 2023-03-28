import bisect
class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l = len(days)

        maximum = (l + 1) * 1000 + 1

        memo = [maximum for _ in range(l + 1)]

        #print(memo)
        seed = [(0, 0)]
        while seed != []:
            idx, cost = seed.pop()
            #buying first day pass
            next_days, next_cost = days[idx] + 1, cost + costs[0]
            next_idx = bisect.bisect_left(days, next_days)
            if memo[next_idx] > next_cost:
                memo[next_idx] = next_cost
                if next_idx != l:
                    seed.append((next_idx, next_cost))

            next_days, next_cost = days[idx] + 7, cost + costs[1]
            next_idx = bisect.bisect_left(days, next_days)
            if memo[next_idx] > next_cost:
                memo[next_idx] = next_cost
                if next_idx != l:
                    seed.append((next_idx, next_cost))

            next_days, next_cost = days[idx] + 30, cost + costs[2]
            next_idx = bisect.bisect_left(days, next_days)
            if memo[next_idx] > next_cost:
                memo[next_idx] = next_cost
                if next_idx != l:
                    seed.append((next_idx, next_cost))
            #print(seed)
            
        #print(memo)
        return memo[-1]