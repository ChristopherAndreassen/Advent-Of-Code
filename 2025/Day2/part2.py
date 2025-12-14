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
            for lenDivideID in range(2, len(str(ID))+1):
                lenID = len(str(ID))
                # Continue if number is not dividable by number
                if lenID % lenDivideID != 0: continue
                # Divide ID
                dividedID = [str(ID)[i:i+lenID//lenDivideID] for i in range(0, lenID, lenID//lenDivideID)]
                # Continue if divided ID has equal parts
                if len(set(dividedID)) != 1: continue
                # Number is invalid, add to result
                self.result += ID
                break


if __name__ == '__main__':
    input = text_in_path("input", ",", "-")
    print(input)
    taskPart = task(input)
    taskPart.solve()
    print(taskPart.result)
