import random
import math
import histogram_maker
import timeit

def cumulative_distribution(histogram):
    """compute the cumulative distribution function given pdf"""
    cumulative = []
    sum = 0
    for i, j in enumerate(histogram):
        sum += j[1]
        cumulative.append((j[0], sum))
    return cumulative

def binary_search(cumulative, target):
    """search through the list to find the target.

    If the target is not found, returns the next index.
    """
    left = 0
    right = len(cumulative) - 1
    while left < right:
        middle = math.floor((left + right) / 2)
        if cumulative[middle][1] == target:
            return middle
        elif cumulative[middle][1] < target:
            left = middle + 1
        elif cumulative[middle][1] > target:
            right = middle - 1
    return left if target <= cumulative[left][1] else left + 1

def sample(cumulative):
    """Generate sample from distribution"""
    totals = cumulative[-1][1]
    random_int = random.randint(1, totals)

    return cumulative[binary_search(cumulative, random_int)][0]

def read_hist(text_file):
    """read the histogram from a txt file"""
    histogram = []
    with open(text_file, 'r') as f:
        for index in f:
            hist_entry = index.split()
            histogram.append((hist_entry[0], int(hist_entry[1])))
    return histogram

if __name__ == '__main__':

    sample = sample(cumulative_distribution(read_hist("histogram.txt")))
    print(sample)
