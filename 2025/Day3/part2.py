from functions import *


class JoltGroup():
    def __init__(self, value: int=0, indexes:list =None, subIndexes:list =None):
        if indexes is None:
            indexes = []
        if subIndexes is None:
            subIndexes = []
        self.value = value
        self.indexes = indexes
        self.subIndexes = subIndexes


class task():
    def __init__(self, input: list):
        self.input = input
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
            jolt, joltIndex = self.findHighestJoltInRange(bank[joltIndex:], 12)
            stHighestJolt += str(jolt)
        #
        self.result += int(stHighestJolt)


    def findHighestJoltInRange(self, bankPart: str, joltSize: int, joltIndOffs: int = 0):
        highestJoltGroup: JoltGroup = JoltGroup()
        SubHighestJoltGroup: JoltGroup = JoltGroup()
        #
        if len(bankPart) < joltSize: return 0, joltIndOffs
        # Find the highest jolts
        for idx, jolt in enumerate(bankPart[:len(bankPart)-joltSize+1]):
            jolt = int(jolt)
            if jolt > highestJoltGroup.value:
                highestJoltGroup.value = jolt
                highestJoltGroup.indexes.clear()
            if jolt == highestJoltGroup.value:
                highestJoltGroup.indexes.append(idx)
        #
        highestJoltGroup.subIndexes.extend(SubHighestJoltGroup.indexes)
        print(highestJoltGroup.value)
        print(highestJoltGroup.indexes)
        #
        while len(highestJoltGroup.indexes) > 1:
            SubHighestJoltGroup.value = 0
            for idx, joltIdx in enumerate(highestJoltGroup.subIndexes):
                subJolt, subJoltIdx = self.findHighestJoltInRange(bankPart[joltIdx+1:], joltSize-1, joltIdx+1)
                print(bankPart[joltIdx+1:])
                print(joltSize-1)
                print(joltIdx+1)
                print()
                print(subJolt)
                print(subJoltIdx)
                #
                if subJolt > SubHighestJoltGroup.value:
                    SubHighestJoltGroup.value = subJolt
                    SubHighestJoltGroup.indexes.clear()
                    SubHighestJoltGroup.subIndexes.clear()
                if subJolt == SubHighestJoltGroup.value:
                    SubHighestJoltGroup.indexes.append(highestJoltGroup.indexes[idx])
                    SubHighestJoltGroup.subIndexes.append(subJoltIdx)
            #
            highestJoltGroup.indexes.clear()
            highestJoltGroup.indexes.extend(SubHighestJoltGroup.indexes)
            highestJoltGroup.subIndexes.clear()
            highestJoltGroup.subIndexes.extend(SubHighestJoltGroup.subIndexes)

        return highestJoltGroup.value, highestJoltGroup.indexes[0]+joltIndOffs


if __name__ == '__main__':
    input = lines_in_path("input")
    print(input)
    taskPart = task(input)
    taskPart.solve()
    print(taskPart.result)
