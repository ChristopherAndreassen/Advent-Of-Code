def lines_in_path(path: str):
    with open(path + ".txt") as file:
        return[line.rstrip() for line in file]

def text_in_path(path: str, divider: str=None, secondDivider: str=None):
    with open(path + ".txt") as file:
        text=""
        for line in file:
            text += line.rstrip()
        if divider is None:
            return text.rstrip()
        if secondDivider is None:
            return text.rstrip().split(divider)
        return [item.split(secondDivider) for item in text.rstrip().split(divider)]

def isfloat(x):
    try:
        float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def StrToIntFloat(val: str):
    val = str(val)
    # Handle "," used instead of "." in float
    if "," in val:
        val = val[:val.find(",")] + "." + val[val.find(",") + 1:]
    # Set as int or float
    if isint(val):
        return int(val)
    try:
        return round(float(val), 2)
    except (TypeError, ValueError):
        raise


# Return strings in listString corresponding with searchString
def SearchResult(searchString: str, listString: list):
    return [word for word in listString if word[:len(searchString)].lower() == searchString[:len(searchString)].lower()]


def isEven(number: int):
    return number % 2 == 0

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range.
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def removeEmptyStrings(stList: list[str]):
    return [item for item in stList if item.strip()]

def listStrToInt(listString: str):
    return [int(string) for string in listString]