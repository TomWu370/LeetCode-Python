class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations), 0, -1):
            if citations[len(citations) - i] >= i:
                return i
        return 0

    
# intuition, go from big to small, iterate backward from len of citations
# check if there are at most h paper, with atleast h citations
# intuition, it's better to first sort the list, then check if the len-ith place is atleast h citations
# in this case h is also i
# edge cases is handled, when the only item is 0, which returns 0