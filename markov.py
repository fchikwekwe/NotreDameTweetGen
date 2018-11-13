import dictogram
import sample

# make a dictionary that stores
# get a random word to start with

"""main is defined outside of the Dictogram class, but inside dictogram file
    main function takes a list as its parameter"""

def markov_model(text_list):
    """ this function takes in a word and checks to see what words come after it
    to determine the word sequence for our generated markov chain"""
    markov_dict = dict()
    # takes in list of words
    # for each word in list, key is word and value is dictogram
    # check if key is stored already
    ## if it is, then append it to the existing histogram
    ## if it isn't, then create a new entry with word as key and dictogram as value
    # return dictionary

if __name__ == '__main__':
    example_list = ["these", "words", "of", "my", "own", "are", "my", "own"]
    markov_model(example_list)
