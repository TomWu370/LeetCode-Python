class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) < k:
            return 0

        sub = sorted(nums[:k])
        index = (len(sub)-1)//2
        if len(sub)%2 == 0:
            mid = (sub[index]+sub[index+1])/2
        else:
            mid =sub[index]

        heap = [mid]

        for i in range(k, len(nums)):
            # critical to remove first item
            del sub[bisect.bisect_left(sub, nums[i-k])]

            if mid >= 2*mid:
                pass

            if nums[i] >= mid:
                bisect.insort_right(sub, nums[i])
            else:
                bisect.insort_left(sub, nums[i])
                
            index = (len(sub)-1)//2
            if len(sub)%2 == 0:
                heap.append((sub[index]+sub[index+1])/2)
            else:
                heap.append(sub[index])

        return heap
        

# sliding window
# then for each window, get the subarray
# append the statistics.median of the subarray to the heap
# however that is not efficient enough as it recalculates for eaach window
# better approach is to add the next item onto the current window, then delete the earlier index for next iteration
# to find median, either pick the middle of the length, or the mean between the 2 middle values.