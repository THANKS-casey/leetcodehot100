class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: # 加一个空集合时候的判断 不然空集还是会输出maxsum=1 注意if not nums是判断空集的 和if nums is None 不一样，None也是个特殊类型，需要定义一个nums = None之后，nums才能被判断为是None，前者包含后者
            return 0
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
                sum = 1 # 这里记得也要改成1

        return maxsum
