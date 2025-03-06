# 注意这道题，题目中的ikj指的是下标，题目意思是找几个不同位置的数字组成3元组，而不是说这个3元组里不能有重复的数字，所以我们只能手动通过while判断去重（在k和j定的时候可以跳过相同的i），而不能通过list（set（））全部去重

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums)-2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1 #因为我们找到了ijk，这时候k不换，要想找到新的就必须把ij两个全换到他们的下一个，不然只换一个的话，没有用，其他两个定，和为0，找到的还是和之前的一样的
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return res
