from functions import *


class task():
    def __init__(self, input: list[str]):
        self.input = input
        self.result = 0
        self.itemEmpty: str = "."

    def solve(self):
        for column, rowOfItems in enumerate(self.input):
            for row, item in enumerate(rowOfItems):
                # Check if paper is accessible
                if item is self.itemEmpty: continue
                if self.isPaperAccessible(column, row):
                    self.result += 1
                    self.input[column] = replacer(self.input[column], "x", row)

    def isPaperAccessible(self, columnItem: int, rowItem: int):
        adjacentPaperCount = 0
        for column in range(columnItem - 1, columnItem + 2):
            if column < 0 or column >= len(self.input): continue
            for row in range(rowItem - 1, rowItem + 2):
                if row < 0 or row >= len(self.input[column]): continue
                if (column == columnItem and row == rowItem): continue
                # Count adjacent paper
                if self.input[column][row] is not self.itemEmpty:
                    adjacentPaperCount += 1
        # Paper is accessible if adjacent paper is fewer then 4
        if adjacentPaperCount < 4: return True
        return False


if __name__ == '__main__':
    input = lines_in_path("input")
    print(input)
    taskPart = task(input)
    taskPart.solve()
    for i in taskPart.input:
        print(i)
    print(taskPart.result)