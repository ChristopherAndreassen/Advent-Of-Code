from operator import truediv

from functions import *


class Task:
    def __init__(self, diagram: list[str]):
        self.diagram: list[str] = diagram
        self.stStart: str = "S"
        self.stSplitter: str = "^"
        self.stEmptySpace: str = "."
        self.stBeam: str = "|"
        self.result: int = 0
        self.beamPositions: list[Coordinate] = [Coordinate(diagram[0].find(self.stStart), 0)]
        self.splitPaths = {}

    def solve(self):
        # Move beam down
        for x in range(len(self.diagram[len(self.diagram)-1])):
            self.splitPaths[self.get_key(x, len(self.diagram)-1)] = 1
        for y in range(len(self.diagram)-2, -1, -1):
            for x, row in enumerate(self.diagram[y]):
                if row == self.stSplitter:
                    self.splitPaths[self.get_key(x, y)] = self.splitPaths[self.get_key(x-1, y+1)] + self.splitPaths[self.get_key(x+1, y+1)]
                else:
                    self.splitPaths[self.get_key(x, y)] = self.splitPaths[self.get_key(x, y+1)]
        print(self.splitPaths)
        self.result = self.splitPaths[self.get_key(self.diagram[0].find(self.stStart), 0)]

    def get_item(self, x: int, y: int):
        return self.diagram[y][x]

    def get_key(self, x: int, y: int):
        return str(y)+"_"+str(x)

if __name__ == '__main__':
    #input = lines_in_path("input_test")
    input = lines_in_path("input")
    print(input)
    taskPart = Task(input)
    taskPart.solve()
    print(taskPart.result)