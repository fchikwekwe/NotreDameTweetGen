import random
import math
import histogram_maker

def cumulative_distribution(histogram):
    """compute the cumulative distribution function given pdf"""
    cumulative = []
    sum = 0
    for key, value in histogram.items():
        # print("key, value:", key, value)
        sum += value
        cumulative.append((key, sum))
    return cumulative

def binary_search(cumulative, target):
    """search through the list to find the target.

    If the target is not found, returns the next index.
    """
    left = 0
    right = len(cumulative) - 1
    while left < right:
        middle = int(math.floor((left + right) / 2))
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

def num_of_words(text, num):
    """use this functions to return a certain number of totally random words"""
    all_words = []
    if num >= 1:
        for i in range(num):
            word = sample(cumulative_distribution(read_hist(text)))
            all_words.append(word)
    else:
        word = sample(cumulative_distribution(read_hist(text)))
        all_words.append(word)
    return all_words

def print_sample():
    """this function takes input and prints out the sample text for you"""
    import sys
    args = "".join(sys.argv[1:])
    num = int(args)
    list_sample = num_of_words(num)
    sample = " ".join(list_sample)
    print(sample)


if __name__ == '__main__':
    print(" ".join(num_of_words(4))+ ".")
