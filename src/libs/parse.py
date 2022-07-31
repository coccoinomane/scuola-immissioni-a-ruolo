from typing import List


def parseBool(value: str, default: bool = None) -> int:
    """
    Get a variable and return False or True based on its value;
    return the default value if the variable is none.

    Rules:
    - a string/number with the value of '1' will be cast to True
    - a string with the value 'true' or 'True' will be cast to True.
    - a string with the value 't' or 'T' will be cast to True.
    - anything else will be cast to False
    """
    if value is None:
        return default

    # 'true', 'True' and '1' all mean True
    if value.lower() == "true" or value.lower() == "t" or value == "1":
        return True

    return False


def parseInt(value: str, default: int = None) -> int:
    """
    Get a variable and cast it to integer; return the
    default value if the variable is none; raises
    an error if the variable is not an integer.
    """
    if value is None:
        return default
    try:
        return int(value)
    except:
        raise Exception(f"Given value must be an integer, {value} given")


def parsePositiveInt(value: str, default: int = None) -> int:
    """
    Get a variable and cast it to integer; return the
    default value if the variable is none; raises
    an error if the variable is not an integer or if it
    is smaller than zero.
    """
    intValue = parseInt(value, default)
    if intValue < 0:
        raise Exception(
            f"Given value must be higher than or equal to 0, '{value}' given"
        )
    return intValue


def parseFloat(value: str, default: float = 0) -> float:
    """
    Get a variable and cast it to a float; return the
    default value if the variable is none; raises an
    error if the variable is not a float
    """
    if value is None:
        return default
    try:
        return float(value)
    except:
        raise Exception(f"Given value must be a float number, '{value}' given")


def parsePositiveFloat(value: str, default: float = 0) -> float:
    """
    Get a variable and cast it to a float; return the
    default value if the variable is none; raises an
    error if the variable is not a float or if it
    is smaller than zero.
    """
    floatValue = parseFloat(value, default)
    if floatValue < 0:
        raise Exception(
            f"Given value must be higher than or equal to 0, '{value}' given"
        )
    return floatValue


def parsePercentage(value: str, default: float = 0) -> float:
    """
    Same as parseFloat, but raises an error if the value is smaller
    than 0 or larger than 100, and allows to use a trailing % sign
    """
    if value is None:
        return default

    # Allow to use a % trailing sign
    sanitizedValue = value.strip()
    if sanitizedValue[-1] == "%":
        sanitizedValue = sanitizedValue[:-1]

    # Cast to a number
    try:
        floatValue = float(sanitizedValue)
    except:
        raise Exception(f"Given value must be a percentage, '{value}' given")

    # Check that the % is within bounds
    if floatValue < 0:
        raise Exception(
            f"Given value must be higher than or equal to 0%, '{value}' given"
        )
    if floatValue > 100:
        raise Exception(f"Given value must be lower than 100%, '{value}' given")

    return floatValue


def parseListOfStrings(value: str, default: List[str] = []) -> List[str]:
    """
    Parse a comma-separated string into a list of strings;
    return None if the variable is none
    """
    if value is None:
        return default
    return [v.strip() for v in value.split(",")]


def parseListOfInts(value: str, default: List[int] = []) -> List[int]:
    """
    Parse a comma-separated string into a list of integers;
    return None if the variable is none, raises an
    exception if the string elements are not castable to
    integers.
    """
    if value is None:
        return default
    return [int(v.strip()) for v in value.split(",")]
