class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            if len(nums2) == 0:
                return median(nums1)
            return self.findMedianSortedArrays(nums2, nums1)
        
        start, end = 0, len(nums1)
        l1,r1,l2,r2 = None, None, None, None
        while True:

            i = (start + end) // 2
            j = ((len(nums1) + len(nums2) + 1) // 2) - i
          
             
            l1 = float(-inf) if i == 0 else nums1[i-1]
            r1 = float(inf) if i == len(nums1) else nums1[i]

            l2 = float(-inf) if j == 0 else nums2[j-1]
            r2 = float(inf) if j == len(nums2) else nums2[j]


            if l1 <= r2 and l2 <= r1:
                if (len(nums1)+len(nums2)) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                end = i - 1
            else:
                start = i + 1

        return 0

# iterate through list starting from middle point of nums1
# index for nums2 is selected by taking the middle of the combined array then subtracting numbers of item in half of nums1, this splits the total number of items into 2 half, ensuring left and right sides have exactly the same total +-1
# in reality it's split into 4 halves but it's treated lke 2 main halves
# then gradually increment like binary search to find the condition that meets the sorted condition, where l1 is less than right side and l2 is also less than right side