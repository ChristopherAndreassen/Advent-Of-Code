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

    def solve(self):
        # Move beam down
        for y in range(len(self.diagram)):
            for x in range(len(self.diagram[y])):
                self.mv_beam_down(x, y)

    def mv_beam_down(self, x: int, y: int):
        # Return if last row
        if y >= len(self.diagram)-1: return
        item = self.get_item(x, y)
        item_below = self.get_item(x, y+1)
        if item == self.stBeam or item == self.stStart:
            if item_below == self.stEmptySpace:
                # Move item down
                self.set_item_below(x, y, self.stBeam)
            elif item_below == self.stSplitter:
                # Split the beam
                if x > 0: self.set_item_below(x-1, y, self.stBeam)
                if x < len(self.diagram[y])-1: self.set_item_below(x+1, y, self.stBeam)
                self.result += 1


    def get_item(self, x: int, y: int):
        return self.diagram[y][x]

    def set_item_below(self, x: int, y: int, item_new: str):
        self.diagram[y+1] = str_replacer(self.diagram[y+1], item_new, x)


if __name__ == '__main__':
    #input = lines_in_path("input_test")
    input = lines_in_path("input")
    print(input)
    taskPart = Task(input)
    taskPart.solve()
    print(taskPart.diagram)
    print(taskPart.result)