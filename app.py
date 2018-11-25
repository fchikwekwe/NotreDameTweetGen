from flask import Flask, render_template
import sample

APP = Flask(__name__)

@APP.route('/')
def sample_function():
    sample_word = sample.sample(sample.cumulative_distribution(sample.read_hist("histogram.txt")))
    return sample_word

sample_function()
