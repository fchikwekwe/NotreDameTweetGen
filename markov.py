import random
import sample
from dictogram import Dictogram

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

def start_words(dictionary):
    # before entering loop get a 'start' word from dictionary
    start_words = []
    for key in dictionary:
        if key.islower() is False:
            start_words.append(key)
    word = random.choice(start_words)
    return word

def create_sentence(start_word, dictionary):
    # create sentence and add first word
    sentence = []
    sentence.append(start_word)
    print("sentence with just first word:", sentence)

    word = start_word
    for key, value in dictionary:
        if key == word:
            # sample from histogram of values
            sample.sample(value)
            break

    # exit dictionary and look for key
    # stop when word is not found

def main():
    example_list = ["One", "fish,", "two", "fish,", "red", "fish,", "blue", "fish."]
    dictionary = markov_model(example_list)
    first_word = start_words(dictionary)
    markov_sentence = create_sentence(first_word, dictionary)
    print(" ".join(markov_sentence))

if __name__ == '__main__':
    main()
