class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        occurence = dict.fromkeys(range(1, len(nums)+1), 0) # initialise empty dictionary with default value 0
        for num in nums:
            occurence[num] += 1
        result = [max(occurence, key=occurence.get), min(occurence, key=occurence.get)]
        return result
        

# initialise empty hashmap with the expected list of values
# then populate hashmap by iterating through nums via occurence
# return the keys with maximum and minimum occurences