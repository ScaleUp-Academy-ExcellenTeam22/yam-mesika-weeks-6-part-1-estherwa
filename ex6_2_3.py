import time


def timer(function,*args,**kwargs)->time:
    """
    A function that receives parameters and calculates the time that takes to finish running the function.
    :param func:The function to calculate its time.
    :param args:A pointer to the specific item.
    :param kwargs:An argument list to the function.
    :return:The time that takes for the function to finish running.
    """
    start_of_time = time.time()
    function(*args,**kwargs)
    end_of_time = time.time()
    return end_of_time-start_of_time

