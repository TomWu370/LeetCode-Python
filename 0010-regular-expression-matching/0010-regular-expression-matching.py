class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matrix = {}
        def traverse(i, j):
            if (i, j) not in matrix:
                if j == len(p):
                    # check when pattern is done, whether text is also done
                    ans = i == len(s)
                else:
                    # check if char match or match with .
                    match = i < len(s) and p[j] in {s[i], '.'}
                    # check if next char is *
                    if j+1 < len(p) and p[j+1] == '*':
                        # check if rest of string after * are matching, or if the previous char match, 
                        # check the next char if it's repeat
                        ans = traverse(i, j+2) or (match and traverse(i+1, j))
                    else:
                        # if not *, check if char match, if so then go to next pair
                        ans = match and traverse(i+1, j+1)
                # update matrix
                matrix[i, j] = ans
            # if value already in matrix then matrix complete, return current matrix pair which is last pair
            return matrix[i, j]
        # this initialise return of final answer, program propagate backwards
        # so the answer is in the first matrix pair
        return traverse(0, 0)


# . matches any character, trigger any char bool mode
# * is match if future char matches the char before *, then star mode ends
# aaa, a = False
# aa, a* = True
# ab, .* = True
# guarantee if * then there's previous char
# . and * interaction
# abb, .* = True, . changes a into b