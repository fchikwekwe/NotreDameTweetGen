from flask import Flask, render_template
import sample

APP = Flask(__name__)

@APP.route('/')
def sample_function():
    sample_sentence = " ".join(sample.num_of_words(4))
    return render_template('index.html', sample_sentence=sample_sentence)

if __name__ == '__main__':
    sample_function()
