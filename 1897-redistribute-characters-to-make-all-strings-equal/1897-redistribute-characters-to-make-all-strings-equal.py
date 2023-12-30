class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        counts = Counter("".join(words))
        
        for count in counts:
            if counts[count] % length != 0:
                return False
        return True

# intuition, words are equal if there are enough unique characters that can be evenly distributed to all words in words list
# in order words, use Counter, and check if each item can be evenly divided by the length of words