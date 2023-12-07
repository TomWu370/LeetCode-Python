class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums).most_common()
        tally = 0
        ans = []
        for i in frequency:
            if tally == k:
                return ans
            ans.append(i[0])
            tally += 1
        return ans

# use Counter class to get frequencies, Counter will sort the dictionary automatically, then loop through the keys to get K amount