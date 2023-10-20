class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = float(-inf)
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                difference = target - sum

                if abs(difference) < abs(target-best):
                    best = sum
                if difference == 0:
                    return sum
                elif difference > 0:
                    k -= 1
                elif difference < 0:
                    j += 1
        return best


# 3Sum problem but with less loops
# loop through sorted nums list, with i as starting value
# use dual pointer then search through the list recording the best result
# move pointer according to certain conditions related to the target
# only need to output the closest result
# difference determined by difference between sum and target
# subtract target from sum then if result is negative then sum > target, otherwise sum < target