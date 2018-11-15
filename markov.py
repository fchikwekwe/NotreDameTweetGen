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
        # check if key is stored already
        if word in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[word].add_count([text_list[index + 1]])
        else:
            # if not, create new entry with word as key and dictogram as value
            markov_dict[word] = Dictogram([text_list[index + 1]])
    # return dictionary
    return markov_dict

def create_sentence(dictionary):
    sentence = []
    for key in dictionary:
        if key != "sitting.":
            sentence.append(key)
    return sentence

if __name__ == '__main__':
    example_list = ["And", "the", "Raven,", "never", "flitting,", "still", "is", "sitting,", "still", "is", "sitting."]
    dictionary = markov_model(example_list)
    markov_sentence = create_sentence(dictionary)
    print(" ".join(markov_sentence))
