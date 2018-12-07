import re


def cleanup(text):
    with open(text, 'r') as source_text:
        # print(source_text.read())
        new_text = re.sub('[A-Z]{3,}', ' ', source_text.read())
    return new_text


if __name__ in '__main__':
    cleanup('souls_of_black_folk.txt')
