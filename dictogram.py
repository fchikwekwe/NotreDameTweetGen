from __future__ import division, print_function # Python 2 and 3 compatability

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dictionary type"""


    def __init__(self, word_list=None):
        """Initialize this histogram as a new dictionary and count given words"""
        super(Dictogram, self).__init__() # Initialize this as a new dictionary
        # Add properties to track useful word counts for this histogram
        self.types = 0 # count of distinct word types in this histogram
        self.tokens = 0 # total count of all word tokens in this histogram
        # count words in given list, if any
        if word_list is not None:
            self.add_count(word_list)

    def add_count(self, word_list, count=1):
        """Increase frequency count of given word by given count amount"""
        for word in word_list:
            # if word is not in dictogram, add word and increment count, tokens, types
            if word not in self:
                self[word] = count
                self.types += count
                self.tokens += count
            # if word is in dictogram, increment count, tokens
            else:
                self[word] += count
                self.tokens += count

    def frequency(self, word, word_list):
        """Return frequency count of given word, or 0 if word is not found"""
        word_frequency = 0
        for key in word_list:
            if key == word:
                word_frequency += 1
        return word_frequency

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # create dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word, word_list)
        print('{!r} occurs {} times'.format(word, freq))
    print()

def main(arguments):
    # if a number is given as argument
    if len(arguments) <= 1:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a log repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                        ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())
    # if multiple arguments are given
    else:
        return print_histogram(arguments)

if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]
    main(arguments)
