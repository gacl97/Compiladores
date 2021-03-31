from Lexic.Lexical import Lexical


class Syntatic:

  def __init__(self):
    # Receber o arquivo ou ler o arquivo aqui. Futuramente por argumentos.
    file = open("teste.txt", 'r')
    
    self.lexical_analyser = Lexical(file=file)

    self.lexical_analyser.has_next_token()
    