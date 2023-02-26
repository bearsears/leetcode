
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)

        k %= total

        l = len(chalk)
        idx = 0
        while chalk[idx] <= k:
            k -= chalk[idx]
            idx += 1
            if idx == l:
                idx = 0
        #print(k)
        return idx