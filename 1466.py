class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        memo = dict()

        #1 means going to 
        #0 means leaving for
        for i in connections:
            if i[0] in memo:
                memo[i[0]][i[1]] = 1
            else:
                memo[i[0]] = dict()
                memo[i[0]][i[1]] = 1
            if i[1] in memo:
                memo[i[1]][i[0]] = 0
            else:
                memo[i[1]] = dict()
                memo[i[1]][i[0]] = 0
        
        #print(memo)

        city_memo = set()
        city = [0]
        ans = 0

        while city != []:
            idx = city.pop()
            for i in memo[idx]:
                if i in city_memo:
                    continue
                if memo[idx][i] == 1:
                    ans += 1
                
                city.append(i)
                
                #print(i, memo[idx][i])
            
            city_memo.add(idx)

        return ans