__creator__ =  "Burhan Özbek"
__date__ = "05.12.2023"
__version__ =  "1.2"


def M(n):
    '''
    Computes the function M(n) according to the given definition.

    Parameters:
    - :param n (int): The input value.

    Returns:
    - int: The result of the function M(n).

        Examples:
        >>> M(87)
        91
    '''
    if n <= 100:
        return M(M(n+11))
    elif n > 100:
        return n - 10







# Run the doctests
if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()
    # Create a dictionary with the results

    start_time = time.time()
    results_dict = {i: M(i) for i in range(1, 201)}
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    #Was ist bemerkenswert beim Ergebnis dieser Funktion?
    #Erst ab 101 wird die Funktion M(n) berechnet, da die Bedingung n <= 100 nicht mehr erfüllt ist.

    # Output the results
    for key, value in results_dict.items():
        print(f"{key}: M({key}) = {value}")