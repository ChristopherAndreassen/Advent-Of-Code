def lines_in_path(path: str):
    with open(path + ".txt") as file:
        return[line.rstrip() for line in file]


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
