class Separators:
  def __init__(self):
    self.all_separators = [';', ' ', '(', ')', '\n', '\t', '{', '}',
              '+', '-', '/', '*', ':', '=', '.',
              '<', '>', '|', '&', ',', '[', ']', '!', '\r', '"', '\'', '%'];

    self.independent_separators = [';', '(', ')', '{', '}', '.','[',']']