class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 依旧注意 这里的子数组是 “连续” 的 如果不连续，只需要把负数全踢了累加就行 
        # 动态规划 本来准备用dp列表存储当前索引之前连续的子数组的和，但是这里因为只要最大和，所以nums这个列表遍历过的地方就不需要了，所以可以就在nums这个列表上改，把nums当dp
        dp = list(num) # dp和nums一样 方便在Python tutor里演示
        for i in range(1,len(nums)): # 因为后面有nums[i-1] 所以这里要从1开始，nums[0]的值会在max(nums[i-1],0)过程中被考虑，存在nums[i]里
            dp[i] += max(dp[i-1],0)
        return max(dp) # 这里不是输出dp[i] 因为dp中存储的是“以当前索引为结尾的连续子数组的最大和”，虽然是“最大和”但是有个限制条件是以当前索引，所以最后还需要选一个最大的
