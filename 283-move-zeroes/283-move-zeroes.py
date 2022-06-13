class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0;
        count0 = 0
        length = len(nums)
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k+=1
            else:
                count0 += 1
                nums.append(0)
        for j in range(length - count0,length):
            nums[j]=0
        del nums[length:]
        