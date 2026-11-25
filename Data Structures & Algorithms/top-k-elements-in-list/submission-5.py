class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        sol = []
        for i in nums:
            if i in frequency.keys():
                frequency[i] += 1
            else:
                frequency[i] = 1
        reversed_vals = dict(sorted(frequency.items(), key=lambda item: item[1], reverse = True))
        for i in reversed_vals:
            if len(sol) == k:
                return sol
            sol.append(i)
        if len(sol) == k:
                return sol