class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.summation = [[] for i in range(len(self.matrix))]

        for i in range(len(self.matrix)):

            for j in range(len(self.matrix[i])):
                if i > 0:
                    if j > 0:
                        self.summation[i].append(self.matrix[i][j] +
                                                 self.summation[i][j - 1] + self.summation[i - 1][j])
                    else:
                        self.summation[i].append(self.matrix[i][j] +
                                                 self.summation[i - 1][j])
                else:
                    if j > 0:
                        self.summation[i].append(self.matrix[i][j] +
                                                 self.summation[i][j - 1])
                    else:
                        self.summation[i].append(self.matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                total += self.matrix[i][j]
        return total


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
                1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])

print(obj.summation)
param_1 = obj.sumRegion(2, 1, 4, 3)
