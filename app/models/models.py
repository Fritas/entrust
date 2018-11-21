class Question(object):


    def __init__(self, text, graph_function, options, answer, id=None, name=str(), img=None):
        """
        """
        self.id = id
        self.text = text
        self.graph_function = graph_function
        self.options = options
        self.answer = answer
        self.img = img

class Answer(object):


    def __init__(self, id, letter, text):
        self.id = id
        self.letter = letter
        self.text = text
