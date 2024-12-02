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

# Find numbers depending on first list and add sum to answer
for num in dataSort[0]:
    answer += dataSort[1].count(num) * num

print(answer)

