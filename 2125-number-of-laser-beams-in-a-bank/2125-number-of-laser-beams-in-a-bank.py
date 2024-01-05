class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        start = None
        for row in bank:
            if row.find('1') >= 0 and not start:
                start = row.count('1')
            elif row.find('1') >= 0 and start:
                target = row.count('1')
                total += start * target
                start = target
            
        return total
# intuition, start from top row, then for each security camera in this row
# it will have the total number of camera on the next available row with cameras
# if no cameras on next row then there are no camera, same with this row
# to get number of cameras, use string.count
# use string.find to check if contains camera, it will return the index, or -1 if not found