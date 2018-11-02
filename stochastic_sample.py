import random
import histogram_maker

def generate_weights(list):
    weights = []
    for word in list:
        word_count = list.count(word)
        weight = word_count/len(list)
    weights.append(word_count)
    weights_and_count = zip(list, weights)
    weights_count_list = list(weights_and_count)

def random_word(histogram):
    # iterate over the histogram
    for word in histogram:
        # using random module to get a random items
        # used random.choice initially, but then changed to random.randint
        random_index = random.randrange(len(histogram))

    random_word = histogram[random_index]
    return random_word

def weighted_probablity(weighted_histogram, num_trials):
    # this list will hold all the generated words
    results = []
    # the number of time that we will run this function
    for _ in range(num_trials):
        # setting up a while loop so that we always return a value
        not_chosen = True
        while not_chosen:
            # randomly choose a list from our list of lists
            random_choice = random.choice(weighted_histogram)
            # assigning variable names to list parts to make it readable
            # word = random_choice[0]
            # probability = random_choice[1]
            word, probability = random_choice
            # randomly generating a float between 0 and 1 inclusive
            random_number = random.uniform(0,1)
            # compare the probability with the random number
            if probability > random_number:
                # if probability is bigger then we get that word
                results.append(word)
                not_chosen = False
            else:
                # if not, try again
                continue
    # slow method, but it works
    return results

def logger(file_name, histogram):
    f = open(file_name, "a")
    f.write("\n\n{}".format(histogram))

if __name__ in '__main__':
    # word_list = histogram_maker.get_source_text("raven.txt")
    # print(generate_weights(word_list))
    weighted_histogram = [["there", 0.05], ["once", 0.2], ["was", 0.05], ["a", 0.1], ["man", 0.1], ["from", 0.1], ["nantucket", 0.4]]
    results_list = weighted_probablity(weighted_histogram, 10000)
    # using histogram function from histogram_maker
    results_histogram = histogram_maker.histogram(results_list)
    print(results_histogram)
    logger("stochastic_logger.txt", results_histogram)
