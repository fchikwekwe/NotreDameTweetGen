# import sys
import markov
from flask import Flask, render_template

app = Flask(__name__)

source_text = "corpus.txt"
text_list = markov.tokenize(source_text)

@app.route('/', methods=['GET', 'POST'])
def index():
    final_sentence = markov.main(text_list)
    return render_template('index.html', final_sentence=final_sentence)

if __name__ == '__main__':
    index()
