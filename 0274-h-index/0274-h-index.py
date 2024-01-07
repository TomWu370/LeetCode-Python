class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        print(citations)
        for i in range(len(citations), 0, -1):
            compare = len(citations) -2 - i
            print(f' i {i} : {compare}')
            if citations[len(citations) - i] >= i:
                return i
        return 1 if citations[0] >= 1 else 0

# intuition, go from big to small, iterate backward from len of citations
# check if there are at most h paper, with atleast h citations
# intuition, it's better to first sort the list, then check if the len-ith place is atleast h citations
# edge cases is handled if the for loop is not executed