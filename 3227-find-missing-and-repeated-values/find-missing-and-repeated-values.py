class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        arr = []

        for row in grid:
            arr.extend(row)

        repeated = -1 
        missing  = -1 

        for num in range(1,n*n+1):
            count = arr.count(num)

            if count == 2:
                repeated = num
            elif count == 0:
                missing = num
        return [repeated,missing]                