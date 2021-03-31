import re

class Lexical():

  def __init__(self, file):
    self.last_token = ""
    self.current_token = ""
    self.line_count = 0
    self.current_column = 0
    self.current_line = ""
    self.file = file

  
  def has_next_token():
    ...

  # Funcao para ler uma linha
  def has_next_line(self):
    line = self.file.readline()

    if(not line):
      return False
    
    self.current_line = line
    self.line_count += 1

    return True


  def has_next_token(self):

    while(self.has_next_line()):

      if(re.match('[ \t\n]+', self.current_line)):
        print("LINHA COM ESPACO EM BRANCO")
      print("Valor linha: ", self.current_line)
