from operator import truediv

from functions import *


class task():
    def __init__(self, problemParts: list[list[int]], problemOperation: list[str]):
        self.problemParts: list[list[int]] = problemParts
        self.operation: list[str] = problemOperation
        self.symAdded = "+"
        self.symMultiplied = "*"
        self.result: int = 0

    def solve(self):
        for idx, operation in enumerate(self.operation):
            resultProblem = 1
            if operation == self.symAdded: resultProblem = 0
            for part in self.problemParts:
                if operation == self.symAdded:
                    resultProblem += part[idx]
                else:
                    resultProblem *= part[idx]
            self.result += resultProblem


if __name__ == '__main__':
    input = lines_in_path("input")
    problemPart = []
    problemOperation = []
    for idx, line in enumerate(input):
        if idx < len(input)-1:
            problemPart.append(listStrToInt(removeEmptyStrings(input[idx].split(" "))))
        else:
            problemOperation = removeEmptyStrings(input[idx].split(" "))
    print(problemPart)
    taskPart = task(problemPart, problemOperation)
    taskPart.solve()
    print(taskPart.result)