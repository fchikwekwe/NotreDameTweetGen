import sys
import tokenize
from dictogram import Dictogram
import sample
# from flask import Flask, render_template

# APP = Flask(__name__)

# @APP.route('/', methods=['GET', 'POST'])
def index():
    random_walk = " ".join(sample.num_of_words(source, 4))
    return render_template('index.html', random_walk=random_walk)

if __name__ == '__main__':
    source = "hunchback.txt"
    token_list = tokenize.all_tokens(source)
    dictogram = Dictogram(token_list)
    # print(dictogram)
    index()
