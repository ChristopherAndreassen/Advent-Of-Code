from functions import *


class task():
    def __init__(self, input: list, joltSize: int):
        self.input = input
        self.joltSize = joltSize
        self.result = 0

    def solve(self):
        for bank in self.input:
            # Find the highest jolt in the battery bank
            self.findHighestJolt(bank)

    def findHighestJolt(self, bank: str):
        stHighestJolt: str = ""
        joltIndex: int = 0
        # Combine jolts to find the highest jolt combination in the battery bank
        for idx in range(1, 13):
            jolt, joltIndex = self.findHighestJoltInRange(bank, len(stHighestJolt), joltIndex)
            stHighestJolt += str(jolt)
            joltIndex += 1
        # Add value to result
        self.result += int(stHighestJolt)


    def findHighestJoltInRange(self, bank: str, joltCount: int, joltIndOffs: int = 0):
        highestJolt = -1
        highestJoltIndex = 0
        # Find the highest jolts
        for idx, jolt in enumerate(bank[joltIndOffs:len(bank)-self.joltSize+joltCount+1]):
            jolt = int(jolt)
            if jolt > highestJolt:
                highestJolt = jolt
                highestJoltIndex = idx

        return highestJolt, highestJoltIndex+joltIndOffs


if __name__ == '__main__':
    input = lines_in_path("input")
    print(input)
    taskPart = task(input,12)
    taskPart.solve()
    print(taskPart.result)
