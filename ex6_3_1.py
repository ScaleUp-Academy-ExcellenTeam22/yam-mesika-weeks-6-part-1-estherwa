def words_length(sentence):
    """
    This function gets a sentence and has to return a list of the length.
    :param sentence:The string of the sentence given by the user.
    :return: List of the length in the words .
    """
    return [len(word) for word in sentence.split(' ')]
