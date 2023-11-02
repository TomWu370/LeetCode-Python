class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = ''
        for i in reversed(s):
            print(i)
            if i == ' ':
                if not answer:
                    continue
                break
            else:
                answer += i

        return len(answer)

# essentially delimit by space then return last item in list
# and finally, remove empty strings for edge cases where there are space at the end
# use filter to replace easily, wrap result with list to get the final list
# or faster method since we don't care about space in between, only at the edges
# we can just use strip

# faster and more efficient way includes pointers or iterator
# traverse each item in the string backwards
# reversed can reverse most iterators
# if answer is empty then ignore space until answer is not empty
# keep appending non space to answer