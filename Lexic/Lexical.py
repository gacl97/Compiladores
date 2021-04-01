import re
from categories.LexemeTable import LexemeTable
from categories.Separators import Separators
from Token.Token import Token

class Lexical():

  def __init__(self, file):
    separators = Separators()
    self.last_token = ""
    self.current_token = ""
    self.line_count = 0
    self.current_column = 0
    self.current_line = ""
    self.file = file
    self.separators = separators.all_separators
    self.independent_separators = separators.independent_separators
    self.lexeme_table = LexemeTable().token_map

  def get_current_char(self):
    return self.current_line[self.current_column]
  
  def print_line(self, lexeme):
    print("{:>4d}  {}".format(self.current_column, lexeme))

  def next_token(self):
    i = self.current_column
    while(i < len(self.current_line) and self.current_line[i] == ' '):
      self.current_column += 1
      i += 1

    lexeme = self.get_current_char()
    while(True):
      print("Current char {}".format(self.get_current_char()), " Esta na tabela de separadores {}".format(self.get_current_char() in self.separators))

      if(self.get_current_char() in self.separators):
        print("SEPARATOR")

        if(self.get_current_char in self.independent_separators):
          print("ENCONTROU UM LEXEMA SEPARADOR IDEPENDENTE")
          self.print_line(lexeme)
          token = Token(self.line_count, self.current_column, lexeme, self.lexeme_table.get(lexeme))
          self.current_column += 1
          return token;

        self.current_column += 1
        break

      if(lexeme in self.lexeme_table):
        print("ENCONTROU UM LEXEMA QUE NAO SEJA SEPARADORES")
        self.print_line(lexeme)
        token = Token(self.line_count, self.current_column, lexeme, self.lexeme_table.get(lexeme))
        self.current_column += 1
        return token
      
      self.current_column += 1
      lexeme += self.get_current_char();
      print(lexeme)

    #   print(self.current_line[self.current_column])
    
    

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

      if(re.match('[\s]*$', self.current_line)):
        print("LINHA COM ESPACO EM BRANCO")
        continue
      while(self.current_column < len(self.current_line)):
        token = self.next_token()

      # Break pra ver somente uma linha por enquanto
      break
      self.last_token = self.current_token        
      # print("Valor linha: ", self.current_line)

      
