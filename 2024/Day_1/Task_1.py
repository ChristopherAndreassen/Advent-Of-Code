# Read text file
text_filename = '{}'.format("Task_1_Input.txt")
with open(text_filename, 'r') as text_reader:
    fileData = text_reader.read()

# Init values
dataSort = [[], []]
answer = 0

# Divide data in lists
fileData = fileData.split("\n")
for dataRow in fileData:
    dataRow = dataRow.split("   ")
    dataSort[0].append(int(dataRow[0]))
    dataSort[1].append(int(dataRow[1]))

# Find data in list in rising order and add difference to answer
while len(dataSort[0]) > 0:
    answer += abs(min(dataSort[0]) - min(dataSort[1]))
    dataSort[0].remove(min(dataSort[0]))
    dataSort[1].remove(min(dataSort[1]))

print(answer)

