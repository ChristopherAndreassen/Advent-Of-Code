from functions import *


class task():
    def __init__(self, input: list):
        self.input = input
        self.result = 0

    def solve(self):
        for stStartID, stEndID in self.input:
            # Check number range and add to result if not valid
            self.checkIdRange(int(stStartID), int(stEndID))

    def checkIdRange(self, startID: int, endID: int):
        # Check number range
        for ID in range(startID, endID + 1):
            lenID = len(str(ID))
            # Continue if number is odd
            if not isEven(lenID): continue
            # Continue if number is not repeated twice
            if str(ID)[:lenID//2] != str(ID)[lenID//2:]: continue
            # Number is invalid, add to result
            self.result += ID


if __name__ == '__main__':
    input = text_in_path("input", ",", "-")
    print(input)
    taskPart = task(input)
    taskPart.solve()
    print(taskPart.result)
