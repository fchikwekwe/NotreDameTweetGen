from flask import Flask
import sample

app = Flask(__name__)

@app.route('/')
def sample_function():
    sample_word = sample.sample(sample.cumulative_distribution(sample.read_hist("histogram.txt")))
    return sample_word

sample_function()
