import string

'''
Creator: Burhan Özbek
Date: 17.11.2020
Version: 1.0
'''

# Run the doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()

def is_palindrom(s:str):
    """
        Checks if a given word is a palindrome.

        Parameters:
        - word (str): The word to be checked for palindrome.

        Returns:
        - bool: True if the word is a palindrome, False otherwise.

        Examples:
        >>> is_palindrom("9009")
        True
    """
    return s == s [::-1]

def is_palindrom_sentence(s:str):
    """
        Checks if a given sentence is a palindrome, considering only alphanumeric characters.

        Parameters:
        - sentence (str): The sentence to be checked for palindrome.

        Returns:
        - bool: True if the sentence is a palindrome, False otherwise.

        Examples:
        >>> is_palindrom_sentence("Oh, Cello! oll Echo!")
        True
        """
    translator = str.maketrans("", "", string.punctuation)
    result = s.translate(translator).replace(" ","").lower()
    return result == result [::-1]

def palindrom_product(x:int):
    """
        Finds the largest palindrome made from the product of two 3-digit numbers.

        Parameters:
        - x (int): The number of digits.

        Returns:
        - int: The largest palindrome made from the product of two x-digit numbers.

        Examples:
        >>> palindrom_product(1000)
        999
    """
    max_palindrom = 0
    for i in range(x):
        for j in range(x):
            produkt = i * j
            if produkt < x and str(produkt) == str(produkt)[::-1] and produkt > max_palindrom:
                max_palindrom = produkt

    return max_palindrom


def get_dec_hex_palindrom(x:int):
    '''
        Finds the biggest palindrom in decimal and hexadecimal system.

        Parameters:
        - x (int): The number of digits.

        Returns:
        - int: The biggest palindrom in decimal and hexadecimal system.

        Examples:
        >>> get_dec_hex_palindrom(58486)
        41514
    '''
    max = 0
    for i in range(x):
        if is_palindrom(str(i)) and is_palindrom(hex(i)[2:]):
            max = i

    return max