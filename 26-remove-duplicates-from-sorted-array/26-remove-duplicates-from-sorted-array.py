class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) > 1:
                nums.remove(num)
        k = len(nums)
        return k