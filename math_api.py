from flask import Flask
from flask import request
import numpy as np
import statistics

app = Flask(__name__)

@app.route("/min")
def api_min():
    """
    api_min: given list of numbers and a quantifier (how many) provides n min number(s)
    Parameters:
        nums: list of numbers. Floats or ints.
        n: return n smaller numbers from list. Integer. Default: 1
    """
    args = request.args.to_dict(flat=False)
    nums = [float(x) for x in args.get('nums', '')]
    if "n" in args:
        n = int(args.get('n', '')[0])
    else:
        n = 1
    return(str(", ".join([str(x) for x in min_internal(nums)])))

def min_internal(nums,n=1):
    """
    min_internal: split for testing
    Parameters:
        nums: list of numbers. Floats or ints.
        n: return n smaller numbers from list. Integer. Default: 1

    >>> min_internal([1,2,3],1)
    [1]
    >>> min_internal([1.0,2.5,3.99],1)
    [1.0]
    >>> min_internal([1,2,3],2)
    [1, 2]
    >>> min_internal([1,2,3])
    [1]
    """
    #First n elements of the sorted list
    nums.sort()
    return(nums[:n])

@app.route("/max")
def api_max():
    """
    api_max: given a list of numbers and a quantifier (how many) provides n max number(s)
    Parameters:
        nums: list of numbers. Floats or ints.
        n: return n largest numbers from list. Integer. Default: 1
    """
    args = request.args.to_dict(flat=False)
    nums = [float(x) for x in args.get('nums', '')]
    if "n" in args:
        n = int(args.get('n', '')[0])
    else:
        n = 1
    return(str(", ".join([str(x) for x in max_internal(nums)])))

def max_internal(nums,n=1):
    """
    max_internal: split for testing
    Parameters:
        nums: list of numbers. Floats or ints.
        n: return n smaller numbers from list. Integer. Default: 1

    >>> max_internal([1,2,3])
    [3]
    >>> max_internal([1,2,3],2)
    [2, 3]
    >>> max_internal([1,2,3],1)
    [3]
    """
    #Last n elements of the sorted list
    nums.sort()
    return(nums[-n:])

@app.route("/avg")
def api_avg():
    """
    api_avg: given a list of numbers, calculates their average
    Parameters:
        nums: array of numbers. Floats or ints.
    """
    args = request.args.to_dict(flat=False)
    nums = [float(x) for x in args.get('nums', '')]
    return str(avg_internal(nums))

def avg_internal(nums):
    """
    avg_internal: split for testing
    Parameters:
        nums: list of numbers. Floats or ints.

    >>> avg_internal([1.8,2.4,3.6])
    2.6
    >>> avg_internal([1,2,3])
    2.0
    >>> avg_internal([1,2,3,99])
    26.25
    """
    return sum(nums) / len(nums)

@app.route("/median")
def api_median():
    """
    api_median: given a list of numbers, calculates their median
    Parameters:
        nums: array of numbers. Floats or ints.
    """
    args = request.args.to_dict(flat=False)
    nums = [float(x) for x in args.get('nums', '')]
    return(str(median_internal(nums)))

def median_internal(nums):
    """
    median_internal: split for testing
    Parameters:
        nums: list of numbers. Floats or ints.

    >>> median_internal([1,2,3])
    2
    >>> median_internal([1,2,3,4,5,6,7,8])
    4.5
    >>> median_internal([1,2,3,4,5,6,7,888])
    4.5
    """
    return statistics.median(nums)

@app.route("/percentile")
def api_percentile():
    """
    api_percentile: given a list of numbers and quantifier 'q', compute the qth percentile of the list elements.
    The percentile should just return one number (from the list).  Use the nearest-rank method.
    https://en.wikipedia.org/wiki/Percentile#The_nearest-rank_method

    Note about numpy.percentile:
        method: This optional method parameter specifies the method to use when the desired quantile lies between two data points i < j.
    And in particular:
        nearest: Takes i or j, whichever is nearest.
    Which matches the required spec from Wikipedia.

    Parameters:
        nums: array of numbers. Floats or ints.
        q: percentile. Float or int. Default: 50
    """
    args = request.args.to_dict(flat=False)
    nums = [float(x) for x in args.get('nums', '')]
    if "q" in args:
        q = float(args.get('q', '')[0])
    else:
        q = 50
    return str(percentile_internal(nums, q))

def percentile_internal(nums,q=50):
    """
    percentile_internal: split for testing
    Parameters:
        nums: array of numbers. Floats or ints.
        q: percentile. Float or int. Default: 50

    >>> percentile_internal([1,2,3], 50)
    2
    >>> percentile_internal([3,4,5])
    4
    >>> percentile_internal([3,4,5],1)
    3
    >>> percentile_internal([3,4,5],99)
    5
    """
    return np.percentile(nums,q, method="nearest")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
