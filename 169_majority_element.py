class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        res = maj = 0

        for n in nums:
            hash[n] = hash.get(n, 0) + 1
            if hash[n] > maj:
                res = n
                maj = hash[n]
        return res
