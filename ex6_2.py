
def filter(function, iterable):
    """
    :param function: function we need to look at
    :param iterable: the value
    :return: if true - we return the item
    """

    yield  from [i for i in iterable if  function(i)  and i ]


def is_positive(number: int) -> bool:
    """
    Function checks if the number is positive.
    :param number: Gets a number.
    :return: Returns if is positive.
    """
    return number > 0

def is_older(number: int) -> bool:
    """
    Function checks if the number is older than 18.
    :param number: Gets a number.
    :return: returns if the number is mature.
    """
    return number > 18
