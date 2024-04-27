# https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26


class Solution:
    dp = []

    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        self.dp = [[None for i in range(len(grid))] for i in range(len(grid))]
        length = len(grid)
        for i, row in enumerate(grid):
            if i == 0:
                self.dp[0] = row
                continue

            for j in range(length):
                minimum = None
                for index in range(length):
                    if j == index:
                        continue
                    if minimum and minimum <= self.dp[i - 1][index] + row[j]:
                        continue
                    minimum = self.dp[i - 1][index] + row[j]

                self.dp[i][j] = minimum
        return min(self.dp[-1])


solution = Solution()

print(solution.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13)
