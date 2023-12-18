import string
from typing import List, Tuple

__creator__ =  "Burhan Özbek"
__date__ = "05.12.2023"
__version__ =  "1.2"



# Run the doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()


def collatz_sequence(number:int)->List[int]:
    '''
        :param number: Startzahl
        :return: Collatz Zahlenfolge, resultierend aus n
        >>> collatz_sequence(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    '''
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
    :param number: Startzahl
    :return: Startwert und Länge der längsten Collatz Zahlenfolge dere Startwert <=n ist
    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    max_length = 0
    max_start = 0
    for i in range(1, n+1):
        length = len(collatz_sequence(i))
        if length > max_length:
            max_length = length
            max_start = i
    return max_start, max_length


def longest_collatz_sequence_extra(n: int, p:3) -> Tuple[int, int]:
    """
    :param number: Startzahl
    :p (int): extra Parameter
    :return: Startwert und Länge der längsten Collatz Zahlenfolge dere Startwert <=n ist
    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    max_length = 0
    max_start = 0
    for i in range(1, n+1):
        sequence = [i]
        while i != 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number = p * number + 1
            sequence.append(number)
        length = len(sequence)
        if length > max_length:
            max_length = length
            max_start = i
    return max_start, max_length
    #Warum dies am Computer nicht empirisch bewiesen werden kann, liegt daran, dass es unendlich viele Startwerte gibt, und das Überprüfen aller möglichen Startwerte nicht praktikabel ist. Es ist eine offene Frage in der Mathematik, die bisher nicht vollständig gelöst wurde.



