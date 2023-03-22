class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        ans = 0

        for i in nums:
            if i != 0:
                ans += (count * (count + 1)) // 2
                count = 0
            else:
                count += 1

        ans += (count * (count + 1)) // 2

        return ans