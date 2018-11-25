from flask import Flask, render_template
import sample

APP = Flask(__name__)

@APP.route('/')
def sample_function():
    sample_word = sample.sample(sample.cumulative_distribution(sample.read_hist("histogram.txt")))
    return render_template('index.html', sample_word=sample_word)

if __name__ == '__main__':
    sample_function()
