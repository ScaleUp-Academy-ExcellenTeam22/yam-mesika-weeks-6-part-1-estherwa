def full_names(first_names, last_names, min_length=0)->list:
    """
       This function has to return a list of all the names of all  the different possible options .
       :param: first_names.
       :param: last_names.
       :return: The function return list of full names of all the possible options of first and the last names.
    """


    return [first_name.capitalize() + " " + last_name.capitalize()
            for first_name in first_names for last_name in last_names
            if len(f"{first_name} {last_name}") >= min_length and min_length is not None]