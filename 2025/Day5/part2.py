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
        sortedFreshIDsIdx = 0
        while sortedFreshIDsIdx < len(self.freshIDs)-1:
            firstID_firstPart = firstPartID(self.freshIDs[sortedFreshIDsIdx])
            firstID_secondPart = secondPartID(self.freshIDs[sortedFreshIDsIdx])
            secondID_firstPart = firstPartID(self.freshIDs[sortedFreshIDsIdx + 1])
            secondID_secondPart = secondPartID(self.freshIDs[sortedFreshIDsIdx + 1])
            if firstID_secondPart >= secondID_secondPart:
                self.freshIDs.pop(sortedFreshIDsIdx + 1)
            elif firstID_secondPart >= secondID_firstPart:
                self.freshIDs[sortedFreshIDsIdx] = newIDrange(firstID_firstPart, secondID_secondPart)
                self.freshIDs.pop(sortedFreshIDsIdx + 1)
            if secondID_firstPart > firstID_secondPart:
                sortedFreshIDsIdx += 1
        #
        for IDRange in self.freshIDs:
            self.freshIDRanges.append([firstPartID(IDRange), secondPartID(IDRange)])
        #
        for IDRange in self.freshIDRanges:
            self.result += IDRange[1] - IDRange[0] + 1

def firstPartID(numberRange):
    return int(numberRange.split("-")[0])

def secondPartID(numberRange):
    return int(numberRange.split("-")[1])

def newIDrange(startID: int, endID: int):
    return str(startID) + "-" + str(endID)


if __name__ == '__main__':
    input = lines_in_path("input")
    blankLineIndex = input.index("")
    freshIngredientIDs = input[:blankLineIndex]
    print(input)
    print(freshIngredientIDs)
    taskPart = task(freshIngredientIDs)
    taskPart.solve()
    print(taskPart.result)