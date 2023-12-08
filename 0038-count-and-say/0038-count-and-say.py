class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"
        for i in range(n-1):
            freq = []
            tempS = ""
            for j in say:
                if tempS == "" or tempS[0] == j:
                    tempS += j
                else:
                    freq.append(tempS)
                    tempS = j
            else:
                # perform append for final set of string
                freq.append(tempS)
            say = ""
            for k in freq:
                say += str(len(k)) + k[0]

        return say

# we don't have to convert num to say, we just need the resulting number
# which can be achieved by using Counter to count the frequency *
# we just need to iteratively perform the same operation, of adding frequency and the number together
# then calculate the frequency of the new string to get to the next iteration
# * however we need a way to calculate the frequency of streaks of continuous same numbers
# for example 1211 should be considered as 1, 2, 11
# 1 way is to find a way to split string into array based on streaks, then calculate the len of each string for frequency
# could be done with regex, but simpler method is simply count frequency by hand then split
# the method used is by adding to a string if current character is the same, if not then append to list, then start fresh