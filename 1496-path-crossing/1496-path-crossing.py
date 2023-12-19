class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), (0,0): True}
        start = [0, 0]

        for p in path:
            start[0] += paths[p][0]
            start[1] += paths[p][1]
            if tuple(start) in paths:
                return True
            else:
                paths[tuple(start)] = True
        return False
        

# intuition, has a dictionary for checking whether coordinate have been travelled
# then have 2 for loops for coordinates, store resulting coordinate in dictionary
# store path coordinate equivalent to dictionary as well for quick check ups
# check if resulting path is in dictionary, if yes then return True, otherwise return False when loop ends