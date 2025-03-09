class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: # 如果题目列表为空，返回空列表
            return []
        intervals.sort(key=lambda x:x[0]) # 对题目所给列表内列表排序，确保排序后左边的左端点永远是最小的，在出现重叠时，左端点永远不用更新，只用更新右端点
        result = [intervals[0]] # 刚开始result为空列表时不能根据索引读取，所以需要先把intervals[0]这项塞给result
        for interval in intervals[1:]: # intervals[0]已经塞到result做最初值了，所以后续比较从intervals[1]开始就行

            # 这里要注意一个小点，就是result内的排序也是sort了的

            if interval[0] <= result[-1][1]: # 新读取的intervals的左端点必然大于result最后一个元素的左端点，所以只更新result的右端点，新读取的intervals的左端点如果不大于result最后一个的右端点，就可以合并
                result[-1][1] = max(result[-1][1],interval[1]) # 右端点更新，取result最后一个列表的右端点和新读取的interval的右端点的最大值
            else:
                result.append(interval) #新读取的intervals的左端点如果大于result最后一个的右端点，说明新读取的interval范围真的大，直接放最后边
        return result
