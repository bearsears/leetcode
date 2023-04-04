class Solution:
    def partitionString(self, s: str) -> int:
        memo, ans = set(), 0

        for i in s:
            if i in memo:
                ans += 1
                memo = set()
                memo.add(i)
            else:
                memo.add(i)
        if memo != set():
            ans += 1
        return ans