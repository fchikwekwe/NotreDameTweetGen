from flask import Flask
# import stochastic_sample
# import histogram_maker
import dictionary_words

app = Flask(__name__)

@app.route('/')
def dictionary():
    word_list = dictionary_words.get_source_text("/usr/share/dict/words")
    sentence = dictionary_words.make_a_sentence(20, word_list)
    return sentence

dictionary()
