def is_isogram(word):
    """ determines if a word has no repeating letters
        
        returns a boolean
    """
    word = word.lower()

    for letter in word:
        if word.count(letter) > 1 and letter.isalpha():
            return False
    return True