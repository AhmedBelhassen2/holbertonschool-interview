#!/usr/bin/python3
""" determines if a given data set represents a valid UTF-8 encoding. """

def validUTF8(data):
    """
    UTF-8 Encode
    """
successive_10 = 0
    for nb_b in data:
        # b = bin(b).replace('0b', '').rjust(8, '0')[-8:]
        nb_b = format(nb_b, '#010b')[-8:]
        if successive_10 != 0:
            successive_10 -= 1
            if not nb_b.startswith('10'):
                return False
        elif nb_b[0] == '1':
            successive_10 = len(nb_b.split('0')[0])
            if successive_10 == 1 or successive_10 > 4:
                return False
            successive_10 -= 1

    return True if successive_10 == 0 else False
