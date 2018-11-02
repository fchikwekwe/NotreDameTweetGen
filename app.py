from flask import Flask
import stochastic_sample
import histogram_maker

app = Flask(__name__)

@app.route('/')
# def hello_world():
#     return 'Hello, World!'

def tweet_gen():
    return "this string"

tweet_gen()
