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
            for part in self.problemParts[idx]:
                if operation == self.symAdded:
                    resultProblem += part
                else:
                    resultProblem *= part
            self.result += resultProblem


if __name__ == '__main__':
    input = lines_in_path("input")
    problemPart = []
    problemPartDivided = [[]]
    problemOperation = []
    for idx in range(len(input)-1):
        for i, num in enumerate(input[idx]):
            #print(problemPart)
            if len(problemPart)-1 < i: problemPart.append("")
            if num != " ": problemPart[i] += num
    for num in problemPart:
        if num == "":
            problemPartDivided.append([])
        else:
            problemPartDivided[-1].append(int(num))
    problemOperation = removeEmptyStrings(input[len(input)-1].split(" "))
    print(problemPartDivided)
    print(problemOperation)
    taskPart = task(problemPartDivided, problemOperation)
    taskPart.solve()
    print(taskPart.result)