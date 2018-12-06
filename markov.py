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

def start_token(dictionary):
    """ Get words that can start a sentence """
    start_tokens = []
    for key in dictionary:
        if key.islower() is False:
            start_tokens.append(key)
    token = random.choice(start_tokens)
    return token

def stop_token(dictionary):
    """ Get words that can end a sentence"""
    stop_tokens = []
    for key, value in dictionary.items():
        if key.endswith('.'):
            print("word with .", key)
            stop_tokens.append(key)

        for k, v in value.items():
            if k.endswith('.'):
                print("word with .", k)
                stop_tokens.append(k)
    return stop_tokens

def create_sentence(start_token, stop_tokens, dictionary):
    # create sentence and add first word
    sentence = []
    sentence.append(start_token)

    word = start_token
    print("word:", word)
    # stop when word is a stop token
    while word not in stop_tokens:
        for key, value in dictionary.items():
            if key == word:
                # sample from histogram of values
                print("value:", value)
                cumulative = sample.cumulative_distribution(value)
                sample_word = sample.sample(cumulative)
                # add new word to sentence
                sentence.append(sample_word)
                word = sample_word
                print("word:", word)
                # get out of for loop and start process over
                break
    return sentence

def main():
    example_list = ["One", "fish,", "two", "fish,", "red", "fish,", "blue", "fish."]
    dictionary = markov_model(example_list)
    print(dictionary)
    first_word = start_token(dictionary)
    end_words = stop_token(dictionary)
    print("end_words:", end_words)
    markov_sentence = create_sentence(first_word, end_words, dictionary)
    print(" ".join(markov_sentence))

if __name__ == '__main__':
    main()
