messages = [{'order': '0', 'word': 'People'}, {'order': '1', 'word': 'who'}, {'order': '2', 'word': 'know'}, {'order': '3', 'word': 'what'}, {'order': '4', 'word': "they're"}, {'order': '5', 'word': 'talking'}, {'order': '6', 'word': 'about'}, {'order': '7', 'word': "don't"}, {'order': '8', 'word': 'need'}, {'order': '9', 'word': 'PowerPoint.'}]


def get_phrase():
    phrase = ''
    for i in range(10):
        phrase = phrase + (messages[i]['word']) + ' '
    print(phrase)

if __name__ == "__main__":
    get_phrase()