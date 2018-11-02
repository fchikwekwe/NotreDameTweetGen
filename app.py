from flask import Flask
import stochastic_sample
import histogram_maker

app = Flask(__name__)

@app.route('/')
# def hello_world():
#     return 'Hello, World!'

def tweet_gen():
    weighted_histogram = [["there", 0.05], ["once", 0.2], ["was", 0.05], ["a", 0.1], ["man", 0.1], ["from", 0.1], ["nantucket", 0.4]]
    results_list = stochastic_sample.weighted_probablity(weighted_histogram, 10000)
    results_histogram = histogram_maker.histogram(results_list)
    print(results_histogram)
