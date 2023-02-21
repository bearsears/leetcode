import bisect
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        l = len(ages)
        to_sort = dict()
        memo = dict()
        memo[0] = 0
        for i in range(l):
            if not ages[i] in to_sort:
                to_sort[ages[i]] = []
            to_sort[ages[i]].append(scores[i])
            memo[scores[i]] = 0
        
        #print(ages, scores, to_sort, memo)
        ages.sort()
        to_iter = list(set(ages))
        to_iter.sort()
        ans = []

        for i in to_iter:
            to_sort[i].sort()
            ans.extend(to_sort[i])
        #print(ans)

        last = 0
        used = set([0])
        for i in ans:
            #print(i, last)
            find_max = 0
            for j in list(used):
                if i >= j:
                    find_max = max(find_max, memo[j])
            memo[i] = max(i + find_max, memo[i])
            used.add(i)

        return max(memo.values())