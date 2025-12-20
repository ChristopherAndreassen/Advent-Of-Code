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


def str_to_int_float(val: str):
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
def search_result(search_string: str, list_string: list):
    return [word for word in list_string if word[:len(search_string)].lower() == search_string[:len(search_string)].lower()]


def is_even(number: int):
    return number % 2 == 0

def str_replacer(s, new_string, index, no_fail=False):
    # raise an error if index is outside the string
    if not no_fail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range.
    if index < 0:  # add it to the beginning
        return new_string + s
    if index > len(s):  # add it to the end
        return s + new_string

    # insert the new string between "slices" of the original
    return s[:index] + new_string + s[index + 1:]


def remove_empty_strings(stList: list[str]):
    return [item for item in stList if item.strip()]


def list_str_to_int(listString: str):
    return [int(string) for string in listString]


class Coordinate:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def set_coord(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_z(self, z: int):
        self.z = z