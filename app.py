# import sys
import markov
from flask import Flask, render_template

app = Flask(__name__)

source_text = "corpus.txt"
cleaned_text = markov.cleanup(source_text)
text_list = markov.tokenize(cleaned_text)

@app.route('/', methods=['GET', 'POST'])
def index():
    final_sentence = markov.main(text_list)
    return render_template('index.html', final_sentence=final_sentence)

if __name__ == '__main__':
    index()
