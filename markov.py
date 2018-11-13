from dictogram import Dictogram
# import sample

# make a dictionary that stores
# get a random word to start with

"""main is defined outside of the Dictogram class, but inside dictogram file
    main function takes a list as its parameter"""

# takes in list of words
def markov_model(text_list):
    """ this function takes in a word and checks to see what words come after it
    to determine the word sequence for our generated markov chain"""
    markov_dict = dict()
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - 1):
        # text_list[index] should be our word from list
        word = text_list[index]
        print("word: {}".format(word))
        # check if key is stored already
        if word in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[word].add_count([text_list[index + 1]])
        else:
            # if not, create new entry with word as key and dictogram as value
            markov_dict[word] = Dictogram([text_list[index + 1]])
    # return dictionary
    return markov_dict

def create_sentence():
    sentence = []
    for key, value in dictionary:



if __name__ == '__main__':
    example_list = ["these", "words", "of", "my", "own", "are", "my", "own"]
    print(markov_model(example_list))
