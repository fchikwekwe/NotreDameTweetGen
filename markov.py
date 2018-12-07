import random
import sample
from dictogram import Dictogram

"""main is defined outside of the Dictogram class, but inside dictogram file
    main function takes a list as its parameter"""
def tokenize(text):
    """ makes text into a list """
    source = open(text, "r").read().split()
    return source

# takes in list of words
def first_order_markov(text_list):
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

def nth_order_markov(order, text_list):
    """ this function takes in a word and checks to see what words come after it
    to determine the word sequence for our generated markov chain"""
    markov_dict = dict()
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - order):
        # text_list[index] should be our word from list
        window = tuple(text_list[index: index+order])
        # check if key is stored already
        if window in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[window].add_count([text_list[index + order]])
        else:
            # if not, create new entry with window as key and dictogram as value
            markov_dict[window] = Dictogram([text_list[index + order]])
    # return dictionary
    # print(markov_dict)
    return markov_dict

def start_token(dictionary):
    """ Get words that can start a sentence """
    start_tokens = []
    for key in dictionary:
        if key[0].islower() is False:
            start_tokens.append(key)
    # print(start_tokens)
    token = random.choice(start_tokens)
    return token

def stop_token(dictionary):
    """ Get words that can end a sentence"""
    stop_tokens = []
    for key, value in dictionary.items():
        # the key number must be changed depending on order number
        if key[2].endswith('.') or key[2].endswith('?'):
            # print("word with .", key)
            stop_tokens.append(key)

    # print("stop tokens:", stop_tokens)
    return stop_tokens

def create_sentence(start_token, stop_tokens, dictionary):
    """ takes dictionary, start and end tokens and makes a sentence """
    # create sentence and add first word
    sentence = []
    # this is hard coded; must be changed to fit the order number
    (word1, word2, word3) = start_token
    sentence.append(word1)
    sentence.append(word2)
    sentence.append(word3)

    current_token = start_token
    # stop when current_token is a stop token
    while current_token not in stop_tokens:
        for key, value in dictionary.items():
            if key == current_token:
                # sample from histogram of values
                cumulative = sample.cumulative_distribution(value)
                sample_word = sample.sample(cumulative)
                # add new sample to sentence_list
                sentence.append(sample_word)
                # assign second word of key and value to current token
                # this is hard coded; must fit the order number
                (current_token_one, current_token_two, current_token_three) = current_token
                current_token = (current_token_two, current_token_three, sample_word)
                # get out of for loop and start process over
                break
    return sentence

def main(source_text):
    """ calling functions and defining variables """
    text_list = tokenize(source_text)
    dictionary = nth_order_markov(3, text_list)
    first_word = start_token(dictionary)
    end_words = stop_token(dictionary)
    markov_list = create_sentence(first_word, end_words, dictionary)
    markov_sentence = " ".join(markov_list)
    print(markov_sentence)
    return markov_sentence

if __name__ == '__main__':
    source_text = 'hunchback.txt'
    main(source_text)
