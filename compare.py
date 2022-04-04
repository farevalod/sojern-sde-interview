import sys, itertools

import argparse

def compare(version1,version2):
    """
    Compare two version numbers, version1 and version2, and return:

    1
    If version1 > version2
    -1
    If version1 < version2
    0
    otherwise

    The following are run as tests (doctest module):

    >>> compare("0.1","1.1")
    -1
    >>> compare("1.1","1.2")
    -1
    >>> compare("1.2.9.9.9.9","1.3")
    -1
    >>> compare("1.3.4","1.3")
    1
    >>> compare("1.10","1.3.4")
    1

    Examples given:
    0.1 < 1.1 < 1.2 < 1.2.9.9.9.9 < 1.3 < 1.3.4 < 1.10
    """

    if version1 == version2:
        return 0
    #We will compare every pair until one rev is strictly larger than the other
    #This gives us pairs from both tokenized version strings, and treats missing as 0s.
    for pair in itertools.zip_longest(version1.split("."), version2.split("."),  fillvalue="0"):
        if int(pair[0]) > int(pair[1]):
            return 1
        elif int(pair[0]) < int(pair[1]):
            return -1
    #They are equal but not literally, like  1 and 001, or 2 and 2.0
    return 0

parser = argparse.ArgumentParser(description='Compare version numbers')

parser.add_argument('version1', type=str,
                    help='First version to compare')
parser.add_argument('version2', type=str,
                    help='Second version to compare')

args = vars(parser.parse_args())
version1 = args["version1"]
version2 = args["version2"]

print(compare(version1, version2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
