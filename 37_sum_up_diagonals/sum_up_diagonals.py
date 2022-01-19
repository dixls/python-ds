def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
             [1,   2],
             [30, 40],
         ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ]
        >>> sum_up_diagonals(m2)
        30
    """
    first_set = sum([matrix[pos][pos] for pos in range(len(matrix))])
    # second_set = 
    for 
    #i looked at the solution and it is very simple and iterating thru things backwards just seems fake