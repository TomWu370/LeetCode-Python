class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []
        for c in s:
            map1.append(s.index(c))
        for c in t:
            map2.append(t.index(c))
        if map1 == map2:
            return True
        return False
   
# intuition, iterate through 1 string, then for each character, replace all occurences with a unique number
# number is the first occurence of that character
# store first occurence in hashmap
# do it for both and check if both string are the same
# rather than unique number, assign the first occurence of that character's index to a list, then check if both list are equal