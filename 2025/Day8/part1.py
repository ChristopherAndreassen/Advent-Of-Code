import math
from functions import *


class Task:
    def __init__(self, coordJunctionBoxes: list[Coordinate]):
        self.coordJB: list[Coordinate] = coordJunctionBoxes
        self.result: int = 0

    def solve(self):
        # Move beam down
        print("hei")

    def set_min_dist_first(self):
        min_dist_idx = dist_coord(self.coordJB[0], self.coordJB[1])
        for idx in range(len(self.coordJB)-1):
            if dist_coord(self.coordJB[idx], self.coordJB[idx+1]) < min_dist_idx:
                min_dist_idx = idx


def sort_JB(coordJB: list[Coordinate]):
    swapped = True
    while swapped:
        swapped = False
        for idx in range(len(coordJB)-2):
            if dist_coord(coordJB[idx], coordJB[idx+1]) < dist_coord(coordJB[idx+1], coordJB[idx+2]):
                swap_JB(coordJB, idx, idx+2)
                swapped = True
    return coordJB


def swap_JB(coordJB: list[Coordinate], indFrom: int, indTo: int):
    toCoord = coordJB[indTo]
    coordJB[indTo] = coordJB[indFrom]
    coordJB[indFrom] = toCoord
    return coordJB


def dist_coord(coord1: Coordinate, coord2: Coordinate):
    return math.sqrt(pow(coord2.x-coord1.x, 2) + pow(coord2.y-coord1.y, 2) + pow(coord2.z-coord1.z, 2))


if __name__ == '__main__':
    input = lines_in_path("input_test")
    #input = lines_in_path("input")
    coordJunctionBoxes: list[Coordinate] = []
    for junctionBox in input:
        coord = junctionBox.split(",")
        print(coord)
        coordJunctionBoxes.append(Coordinate(int(coord[0]), int(coord[1]), int(coord[2])))
    print(input)
    sortedJB = sort_JB(coordJunctionBoxes)
    for coordJB in sortedJB:
        print(str(coordJB.x) + ", " + str(coordJB.y) + ", " + str(coordJB.z))
    for idx in range(len(sortedJB)-1):
        print(dist_coord(sortedJB[idx], sortedJB[idx+1]))
    #taskPart = Task(input)
    #taskPart.solve()
    #print(taskPart.result)