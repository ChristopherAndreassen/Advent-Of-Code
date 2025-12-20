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
        self.beamBelowPositions: list[Coordinate] = []

    def solve(self):
        # Move beam down
        for y in range(len(self.diagram)-1):
            self.beamBelowPositions = []
            for idx, coord in enumerate(self.beamPositions):
                beamBelowPositionsOutput = self.mv_beam_down(coord)
                for coordinate in beamBelowPositionsOutput:
                    self.diagram[coordinate.y] = str_replacer(self.diagram[coordinate.y], self.stBeam, coordinate.x)
                    self.beamBelowPositions.append(coordinate)
            self.beamPositions = self.beamBelowPositions.copy()
        self.result = len(self.beamPositions)

    def mv_beam_down(self, coord: Coordinate):
        # Return if last row
        if coord.y >= len(self.diagram)-1: return
        item_below = self.get_item(Coordinate(coord.x, coord.y+1))
        if item_below == self.stEmptySpace or item_below == self.stBeam:
            # Move item down
            coord.set_y(coord.y+1)
            return [coord]
        else:
            # Split the beam
            if coord.x <= 0 or coord.x >= len(self.diagram[coord.y])-1:
                if coord.x > 0: coord.set_coord(coord.x-1, coord.y+1)
                if coord.x < len(self.diagram[coord.y])-1: coord.set_coord(coord.x+1, coord.y+1)
                return [coord]
            else:
                return [Coordinate(coord.x-1, coord.y+1), Coordinate(coord.x+1, coord.y+1)]


    def get_item(self, coord: Coordinate):
        return self.diagram[coord.y][coord.x]


if __name__ == '__main__':
    #input = lines_in_path("input_test")
    input = lines_in_path("input")
    print(input)
    taskPart = Task(input)
    taskPart.solve()
    print(taskPart.result)