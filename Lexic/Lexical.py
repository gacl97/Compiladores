import re

class Lexical():

  def __init__(self, file):
    self.last_token = ""
    self.current_token = ""
    self.line_count = 0
    self.current_column = 0
    self.current_line = ""
    self.file = file

  
  def next_token(self):
    i = self.current_column
    while(i < len(self.current_line) and self.current_line[i] == ' '):
      self.current_column += 1
      i += 1
    
    

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

      # if(re.match('[\s]*$', self.current_line)):
      #   print("LINHA COM ESPACO EM BRANCO")
      #   continue
      # count = 0
      aux = re.match('[a-zA-Z0-9]*', self.current_line)
      print(aux)
      # print(re.match('[a-zA-Z0-9]*', self.current_line[aux.end() + 1:]))
      # self.next_token()
      #   self.last_token = self.current_token        
      # }
      # print("Valor linha: ", self.current_line)

      
