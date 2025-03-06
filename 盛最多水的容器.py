# 底宽确定时，组成水的体积的高由短板决定，短板内移，在底宽缩短的情况下体积可能变大，如果是长板内移，底宽缩短的情况下新体积必然小于等于之前的体积，所以只移动短板

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res,height[i]*(j-i))
                i += 1
            else:
                res = max(res,height[j]*(j-i))
                j -= 1
        return res
