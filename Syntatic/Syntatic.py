from Lexic.Lexical import Lexical
from Token.Token import Token
import traceback


class Syntatic:

  def __init__(self, file_name):

    try:
      file = open(file_name, 'r')
    except Exception:
      traceback.print_exc()
    
    self.lexical_analyser = Lexical(file=file)
    
    while(self.lexical_analyser.has_next_token()):
      token = self.lexical_analyser.next_token()
      token.print_token()
    