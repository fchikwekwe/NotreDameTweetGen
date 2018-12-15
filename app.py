# import sys
import markov
from flask import Flask, render_template

app = Flask(__name__)

source_text = "corpus.txt"
cleaned_text = markov.cleanup(source_text)
text_list = markov.tokenize(cleaned_text)
# create a data structure to hold random_sentences

@app.route('/', methods=['GET', 'POST'])
def index():
    # perhaps change this variable to random_sentences
    final_sentence = markov.main(text_list)
    # then push that sententence into your data structure
    # then create an algorithm to grab a random index from the data structure
    # set that to final_sentence

    '''NOTE: once your page has been loaded 1000's of times, your data structure
    of going to be huge. Time complexity is still O(1), but it could start to take
    up lots of space. If it gets to that, consider migrating your data to a
    database, and doing a fetch <~~~ don't optimize for this until you need to.
    '''
    return render_template('index.html', final_sentence=final_sentence)

if __name__ == '__main__':
    index()
