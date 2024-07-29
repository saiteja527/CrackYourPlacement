class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            map1[nums[i]] = 1 + map1.get(nums[i],0)
        li = []
        for i,j in map1.items():
            if j == 2:
                li.append(i)
        return li
