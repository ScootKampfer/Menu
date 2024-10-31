def exposantN(number, exponent):

    i = 1
    newnumber = number

    while i < exponent:
        newnumber = newnumber*number
        i += 1
    return newnumber

print(exposantN(2,5))

print(2**5)