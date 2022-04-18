from ex6_2 import filter , is_positive, is_older
from positive_numbers import get_the_positive_numbers

if __name__ == '__main__':

    list_of_numbers = [-1,-2,-5,0, 1, 4, 2, 17, 35, 59, 99, 119]


    # Prints ex6.2
    print(tuple(filter(is_positive, list_of_numbers )))
    # Prints ex6.2
    print(tuple(filter(is_older, list_of_numbers )))
    # Prints ex6.2.2
    print("The positive numbers in the list are: ",get_the_positive_numbers(list_of_numbers))







