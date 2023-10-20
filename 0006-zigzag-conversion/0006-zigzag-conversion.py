class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        
        matrix = [[] for row in range(numRows)]
        i = 0

        for char in s:
            matrix[i].append(char)
            if i == 0:
                step = 1
            elif i == numRows -1:
                step = -1
            i += step
        convertion = ""
        for L in matrix:
            convertion += "".join(L)
        return convertion

# intuitively this is a case of appending item to n number of lists, going from top to bottom and up, according to a certain condition
# what needs to be realised is how zigzag pattern does not matter, it's simply an up and down pattern that oscillates
# create 2d array