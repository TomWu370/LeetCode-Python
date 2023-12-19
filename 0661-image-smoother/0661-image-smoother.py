class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            row = []
            for j in range(n):
                temp = [img[i][j]]
                for direction in directions:
                    if 0 <= i+direction[0] < m and 0 <= j+direction[1] < n:
                        temp.append(img[i+direction[0]][j+direction[1]])
                row.append(floor(mean(temp)))
            ans.append(row)

        return ans
        
# machine learning smoothing techniques
# apply a 3x3 filter through every pixel of an given image, ignore values that don't exist
# then take average
# intuition for this step, push to a list then take mean, this way there's no need to care about calculating mean
# then floor this average
# then repeat for next pixel
# the easiest way to get all the surrounding 8 value is to have a directions list of tuples for direction
# or iterate through -1 - 1 for x and y coordinates
# then check for constraints on these coordiantes to make sure they're not out of bounds