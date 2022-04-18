from ex6_2 import filter , is_positive, is_older
from ex6_3_1 import words_length
from ex6_3_2 import get_letter
from ex6_3_3 import count_word
from positive_numbers import get_the_positive_numbers
from ex6_2_3 import timer



if __name__ == '__main__':

    list_of_numbers = [-1,-2,-5,0, 1, 4, 2, 17, 35, 59, 99, 119]

    # Prints ex6.2
    print(tuple(filter(is_positive, list_of_numbers )))
    # Prints ex6.2
    print(tuple(filter(is_older, list_of_numbers )))
    # Prints ex6.2.2
    print("The positive numbers in the list are: ",get_the_positive_numbers(list_of_numbers))
    # Prints ex6.2.3
    time= timer(print, "Hello")
    print("First time",time)
    time1=timer(zip, [0,1,2,3], [4, 5, 6])
    print(time1)
    time2=timer("Hi {name}".format, name="Bug")
    print(time2)
    #ex6.3.1
    sentence = "Toto, I've a feeling we're not in Kansas anymore"
    print(words_length(sentence))
    #EX6.3.2 - once we will print it for capital letter and another time for regular letter
    print(get_letter(ord('A'),ord('Z')))
    print(get_letter(ord('a'), ord('z')))
    text_counter= """
        You see, wire telegraph is a kind of a very, very long cat.
        You pull his tail in New York and his head is meowing in Los Angeles.
        Do you understand this?
        And radio operates exactly the same way: you send signals here, they receive them there.
        The only difference is that there is no cat.
        """
    # EX6.3.3
    print((count_word(text_counter)))








