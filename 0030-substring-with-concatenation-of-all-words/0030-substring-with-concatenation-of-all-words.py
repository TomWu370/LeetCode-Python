class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0]) * len(words)
        sublength = len(words[0])
        ans = []

        for i in range(len(s)-length+1):
            content = s[i:i+length]
            subwords = [content[i:i+sublength] for i in range(0, length, sublength)]
            if Counter(subwords) == Counter(words):
                ans.append(i)
        return ans



# use fixed window sliding
# record starting index of the first permutation found
# since window is fixed size, we can go through the string with decent time complexity
# step 1 is to generate all the permutations of a given list, then as we find 1, remove from the list
# however this becomes more intense as we increase word list size
# another method is to split the window of text into equal components, since all words have fixed size
# we can use the length of 1 word in words, to determine the split length
# then we check whether all of the split words are in words (since it has to have all words, even if 1 split word is wrong, it's False)
# this can be done by using all function and list comprehension inside
# all(x in list for x in list2)
# however this method ignores duplicates, by using Counter and directly compare the lists, item by item
# we will be able to return true even if list2 has 2 of the same items
## then if true, we add the concatonated word into an list
## then each time, we check if the new concatonated word is in this list, before we proceed
# we don't need to care about duplicate valid words, as seen with foobarfoobar testcase, we just need to return index
# for all valid concatonated words in the string
