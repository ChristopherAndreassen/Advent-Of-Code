from operator import truediv

from functions import *


class task():
    def __init__(self, freshIngredientIDs: list[str]):
        self.freshIDs: list[str] = freshIngredientIDs
        self.freshIDRanges: list[list[int]] = []
        self.freshAvailableIDs: list[int] = []
        self.result: int = 0

    def solve(self):
        #
        self.freshIDs = sorted(self.freshIDs, key=firstPartID)
        #
        #for IDRange in self.freshIDs:

        #
        for IDRange in self.freshIDs:
            divider = IDRange.index("-")
            self.freshIDRanges.append([int(IDRange[:divider]), int(IDRange[divider+1:])])
        #
        for stID in self.availableIDs:
            ID = int(stID)
            if self.isFresh(ID):
                self.freshAvailableIDs.append(ID)
        #
        self.result = len(self.freshAvailableIDs)

    def isFresh(self, ID: int):
        for freshIDRange in self.freshIDRanges:
            if freshIDRange[0] <= ID <= freshIDRange[1]:
                return True
        return False

def firstPartID(numberRange):
    return int(numberRange.split("-")[0])

def secondPartID(numberRange):
    return int(numberRange.split("-")[1])


if __name__ == '__main__':
    input = lines_in_path("input")
    blankLineIndex = input.index("")
    freshIngredientIDs = input[:blankLineIndex]
    print(input)
    print(freshIngredientIDs)
    taskPart = task(freshIngredientIDs)
    taskPart.solve()
    print(taskPart.result)