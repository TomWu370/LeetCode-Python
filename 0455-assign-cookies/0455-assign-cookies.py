class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        last = 0
        g.sort()
        s.sort()
        for i in range(len(g)):
            for j in range(last, len(s)):
                if s[j] >= g[i]:
                    count += 1
                    last = j + 1
                    break
        return count

# intuition typical 2 pointer problem, have 2 pointers through each of the list
# assume both sorted, it's not, so sort both lists
# if current cookie is more than/equal to desired cookie size, move both pointer up 1, to represent consumed
# if cookie is smaller than desired then more to next cookie size
# return total consumed