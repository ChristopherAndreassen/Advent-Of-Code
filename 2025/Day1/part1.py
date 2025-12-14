from functions import *


class part1():
    def __init__(self, dialStartNumber: int):
        self.dialNumber = dialStartNumber
        self.result = 0

    def solve(self):
        # Find all lines in input
        listRotations = lines_in_path("input")
        for rotation in listRotations:
            self.rotateDial(rotation)

    def rotateDial(self, rotation: str):
        if getRotationRight(rotation):
            self.dialNumber += getRotationValue(rotation)
        else:
            self.dialNumber -= getRotationValue(rotation)
        # Adjust dial number and update result
        while self.dialNumber >= 100:
            self.dialNumber -= 100
        while self.dialNumber < 0:
            self.dialNumber += 100
        if self.dialNumber == 0:
            self.result += 1

    def getDialNumber(self):
        return self.dialNumber

    def getResult(self):
        return self.result


def getRotationRight(rotation:str):
    return rotation[0]=="R"

def getRotationValue(rotation:str):
    return int(rotation[1:])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    taskPart1 = part1(50)
    taskPart1.solve()
    print(taskPart1.getResult())
    print(taskPart1.getDialNumber())
