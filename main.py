from ex6_2 import filter , is_positive, is_older

if __name__ == '__main__':

    the_ages = [-1,-2,-5,0, 1, 4, 2, 17, 35, 59, 99, 119]

    print(tuple(filter(is_positive, the_ages)))

    print(tuple(filter(is_older, the_ages)))




