

class IncorrectNumberError(Exception):

    pass


class IncorrectNumberTypeError(IncorrectNumberError):

    pass


class NumberIsNotIntegerError(IncorrectNumberError):

    pass


def check_number(raw_number: str):

    try:
        number = float(raw_number)
    except ValueError:
        raise IncorrectNumberTypeError()

    if not number.is_integer():
        raise NumberIsNotIntegerError()

    number = int(number)

    return number
