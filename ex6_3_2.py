def get_letter(letter_a, letter_z)->list:
    """
    The function returns a list of letters between A and Z or between a and z.
    :return:The list of all letters between A and Z or between a and z.
    """
    return [chr(letter) for letter in range(letter_a,letter_z)]

