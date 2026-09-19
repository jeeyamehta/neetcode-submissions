class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = []
        ns = []
        tot = []

        for num in nums:
            if num not in ns:
                count.append(nums.count(num))
                ns.append(num)

        for i in range(k):
            tot.append(ns[count.index(max(count))])
            ns.pop(count.index(max(count)))
            count.pop(count.index(max(count)))

        return tot

