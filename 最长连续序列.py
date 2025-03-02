class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums = list(nums_set) #这里不能用nums = list(nums_set).sort() 因为.sort()这个东西光排不返回，排好了返回一个空值，这里不能给空值
        nums.sort()
        sum = 1 # 注意刚开始sum和maxsum都得是1，如果是0的话会使结果少1（因为一个不连续的时候，它本身的长度就有1）
        maxsum = 1
        length = len(nums_set)
        for i in range(length-1): #防止后面nums[i+1]索引越界
            if (nums[i+1] - nums[i]) == 1:
                sum += 1
                if maxsum < sum:
                    maxsum = sum
            else:
                sum = 0

        return maxsum
