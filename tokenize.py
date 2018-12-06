
def all_tokens(text):
    source = open(text, "r").read().split()
    return source

if __name__ in '__main__':
    all_tokens("hunchback.txt")
