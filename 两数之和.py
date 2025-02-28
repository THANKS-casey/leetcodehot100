class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):# 当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，因此不需要再进行匹配；注意这里的范围是从i+1开始，如果从i开始的话，会出现i+j实际是i+i的特殊情况
                if nums[i] + nums[j] == target:
                    return [i,j]

        return [] # 删了这个没影响
