class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 注意这里的子数组是指 连续 的
        count = {}
        count[0] = 1 # 因为如果之前的前缀和存在curr_sum - k的情况，由于是连续的序列，所以之前的前缀和有几个相同的，就说明有几个前缀和为k的 因为curr_sum - k（之前的前缀和）+ k（现在的前缀和）=curr_sum（现在的前缀和） 所以如果索引为0时就满足nums[0]=k 了，那因为之前没有前缀和，所以需要我们预设一个0
        result = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num # 计算当前前缀和
            if curr_sum - k in count: # 发现满足的子序列
                result += count[curr_sum - k] #满足的个数 加到result里
            count[curr_sum] = count.get(curr_sum, 0) + 1 # 因为if判断条件里没用到count[curr_sum]，所以这个东西放在if前面也行
        return result
