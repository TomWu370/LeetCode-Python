class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')

        return len(words[-1])


# essentially delimit by space then return last item in list
# and finally, remove empty strings for edge cases where there are space at the end
# use filter to replace easily, wrap result with list to get the final list
# or faster method since we don't care about space in between, only at the edges
# we can just use strip

# other method includes pointers or iterator
# traverse each item in the string backwards
# reversed can reverse most iterators
# if answer is empty then ignore space until answer is not empty
# keep appending non space to answer