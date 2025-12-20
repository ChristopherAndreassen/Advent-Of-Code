import math
from functions import *


class Task:
    def __init__(self, coordJunctionBoxes: list[Coordinate]):
        self.coordJB: list[Coordinate] = coordJunctionBoxes
        self.result: int = 0
        self.coordJB_dist_to_coord: list[list[float]] = []
        self.circuit: list[list[int]] = []

    def solve(self):
        #
        for coord in self.coordJB:
            self.coordJB_dist_to_coord.append(self.dist_to_coord(coord))
        #
        for idx, listDist in enumerate(self.coordJB_dist_to_coord):
            i1, i2 = self.is_shortest_dist()

    def is_shortest_dist(self):
        shortest_dist_index_1 = 0
        shortest_dist_index_2 = 0
        shortest_dist = self.coordJB_dist_to_coord[0][0]
        if shortest_dist == 0: shortest_dist = self.coordJB_dist_to_coord[0][1]
        for idx, listDist in enumerate(self.coordJB_dist_to_coord):
            for i, dist in listDist:
                if dist < shortest_dist and dist > 0:
                    shortest_dist = dist
                    shortest_dist_index_1 = idx
                    shortest_dist_index_2 = i
        self.coordJB_dist_to_coord[shortest_dist_index_1][shortest_dist_index_2] = 0
        self.coordJB_dist_to_coord[shortest_dist_index_2][shortest_dist_index_1] = 0
        return shortest_dist_index_1, shortest_dist_index_2

    def dist_to_coord(self, coordInput: Coordinate):
        list_dist_to_coord: list[float] = []
        for coord in self.coordJB:
            list_dist_to_coord.append(dist_coord(coordInput, coord))
        return list_dist_to_coord


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