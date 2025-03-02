class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list) #创建一个特殊字典，如果用没有的键访问 一般字典会报错 这种字典会拿你输入的东西作为键，创建一个

        for st in strs:
            key = "".join(sorted(st)) # 把每个词儿按字母顺序排，字符间用""连起来，相当于直接连起来
            mp[key].append(st) # 以上一行排完的值做键，遍历每个字符串塞到值里

        return list(mp.values()) # mp.values() 获取 mp 这个 defaultdict 对象中所有的值，用list格式输出
