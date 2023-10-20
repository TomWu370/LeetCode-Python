class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)

        answers = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = len(nums)-1

            while j < k:
                sum = (nums[i] + nums[j] + nums[k]) 

                if sum == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    answers.append(triplet)
                    while j < k and nums[j] == triplet[1]:
                        j += 1
                    while j < k and nums[k] == triplet[2]:
                        k -= 1
                elif sum > 0:
                    j += 1
                else:
                    k -= 1
        return answers
                

# best to sort the list
# the list can be sorted because the answer only requires you to return the value, and not the index, therefore
# you only need to make sure the value with certain index are not duplicates, doesn't matter what the index are
# pick value at start as i, then have 2 pointers, move them in ways according to condition, so that they approach total of 0
# to avoid duplicate selection of the same 2Sum values, make sure the ith value is not the same
# even when correct sum is found, don't stop there and continue exhausting the search until you find another pair, with the same ith value sums to 0
# as long as the jth and kth value are not the same