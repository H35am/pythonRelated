import doctest


def returnPrimeNumbers(number):
    """

    :param number:
    :return: List with prime numbers

    >>> returnPrimeNumbers(9)
    [2,3,5,7]

    >>> returnPrimeNumbers(2)
    [2]
    """

    aLijst = []
    assert number > 0
    assert number == int(number)

    if number == 2:
        #print(number, "Invoer is 2.")
        aLijst.append(number)
    else:

        for i in range(2, number):
            #print(i)
            add = True
            if i != 2:
                for j in range(3, i):
                    print(i, j, i % j)
                    if i % j == 0:
                        add = False
                        break
            if add:
                aLijst.append(i)

    return aLijst


if __name__ == "__main__":
    doctest.testmod()
