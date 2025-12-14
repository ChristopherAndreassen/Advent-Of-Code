from functions import *


class task():
    def __init__(self, input: list[str]):
        self.input = input
        self.result = 0
        self.itemPaperPresent: str = "@"

    def solve(self):
        paperRemoved = 1
        while paperRemoved > 0:
            paperRemoved = self.removePaper()
            self.result += paperRemoved

    def removePaper(self):
        paperRemovedCycle = 0
        for column, rowOfItems in enumerate(self.input):
            for row, item in enumerate(rowOfItems):
                # Check if paper is accessible
                if item is not self.itemPaperPresent: continue
                if self.isPaperAccessible(column, row):
                    paperRemovedCycle += 1
                    # Remove paper from map
                    self.input[column] = replacer(self.input[column], "x", row)
        return paperRemovedCycle

    def isPaperAccessible(self, columnItem: int, rowItem: int):
        adjacentPaperCount = 0
        for column in range(columnItem - 1, columnItem + 2):
            if column < 0 or column >= len(self.input): continue
            for row in range(rowItem - 1, rowItem + 2):
                if row < 0 or row >= len(self.input[column]): continue
                if (column == columnItem and row == rowItem): continue
                # Count adjacent paper
                if self.input[column][row] is self.itemPaperPresent:
                    adjacentPaperCount += 1
        # Paper is accessible if adjacent paper is fewer then 4
        if adjacentPaperCount < 4: return True
        return False


if __name__ == '__main__':
    input = lines_in_path("input")
    print(input)
    taskPart = task(input)
    taskPart.solve()
    taskPart.isPaperAccessible(0,2)
    for i in taskPart.input:
        print(i)
    print(taskPart.result)