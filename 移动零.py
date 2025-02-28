class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1 # find 0,put it in where left is, then move left foeward by 1
            right += 1 # next right
