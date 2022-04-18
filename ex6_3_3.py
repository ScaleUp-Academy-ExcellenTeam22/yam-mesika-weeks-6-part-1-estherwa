import string
def count_word(text:str):
    """
    A function that gets one specific paragraph and has to return the length of each word.
    :param text:one long paragraph.
    :return:the length of each word in the text.
    """


    text=set(filter(lambda x: len(x) > 0,text.replace("\n"," ").translate(str.maketrans('', '')).split()))

    return {word: len(word) for word in text }
