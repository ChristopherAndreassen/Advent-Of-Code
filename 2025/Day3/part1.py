from functions import *


class task():
    def __init__(self, input: list):
        self.input = input
        self.result = 0

    def solve(self):
        for bank in self.input:
            # Find the highest jolt in the battery bank
            self.findHighestJolt(bank)

    def findHighestJolt(self, bank: str):
        highestJolt = 0
        # Combine jolts to find the highest jolt combination in the battery bank
        for idx, firstPartJolt in enumerate(bank[:len(bank)-1]):
            for secondPartJolt in bank[idx+1:]:
                jolt = int(firstPartJolt+secondPartJolt)
                if jolt > highestJolt: highestJolt = jolt
        self.result += highestJolt


if __name__ == '__main__':
    input = lines_in_path("input")
    print(input)
    taskPart = task(input)
    taskPart.solve()
    print(taskPart.result)
