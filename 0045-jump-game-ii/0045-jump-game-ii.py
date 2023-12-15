class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current, furthest = 0, nums[0]
        for i in range(len(nums)-1):
            # after calculating a jump, continue the next spots, to see if there's a further jump
            # i.e if can jump 2 squares, then you scan the next 2 squares and get the furthest value
            furthest = max(furthest, i+nums[i])
            if i == current:
                # performs the jump
                jumps += 1
                current = furthest
            if current >= len(nums)-1:
                return jumps

        return jumps
            
# intuition, declare a empty list, opposite of what we're trying to achieve
# or the opposite or minimise, so infinite
# set base case as 0
# then iterate through the list, update all of the minimums
# for each step available, check if the step will cause index to go past target
# if not then update the current best steps, to be the minimum of previously possible defined minimum values
# all the way to the last item, which we return
# intuition for time reduction, the assumption, we can always reach the end
# this means we can have a greedy approach, let's say we can reach 3,1,end
# maybe going to 1 is optimal, however anything 1 can reach can be reached by 3, this is why greedy works here