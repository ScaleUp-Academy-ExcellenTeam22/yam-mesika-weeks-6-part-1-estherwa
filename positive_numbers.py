def get_the_positive_numbers(list_of_number)->list:
    """
    The function gets a list of numbers and returns the positive numbers
    in the list.
    :param:list_of_numbers:A list of numbers.
    :return:A list of positive numbers.
    """
    return list(filter(lambda x:x > 0, list_of_number))
