class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = ''
        for i in reversed(s):
            print(i)
            if i == ' ' and not answer:
                continue
            elif i == ' ':
                break
            else:
                answer += i

        return len(answer)


# essentially delimit by space then return last item in list
# and finally, remove empty strings for edge cases where there are space at the end
# use filter to replace easily, wrap result with list to get the final list

# more efficient way includes pointers or iterator
# traverse each item in the string backwards
# reversed can reverse most iterators
# if answer is empty then ignore space until answer is not empty
# keep appending non space to answer