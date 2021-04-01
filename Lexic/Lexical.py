import re
from categories.LexemeTable import LexemeTable
from categories.Separators import Separators
from Token.Token import Token
from Token.TokensCategories import TokensCategories

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
    return str(self.current_line[self.current_column])
  
  def print_line(self):
    print("{:>4d}  {}".format(self.line_count, self.current_line))

  def print_token(self, token):
    print("          [{:>04d}, {:>04d}] ({:>04d}, {:>20s}) {{{}}}".format(token.line_number, token.column_number, token.token_id, token.token_category, token.lexeme))

  def next_token(self):
    i = self.current_column
    while(i < len(self.current_line) and (self.current_line[i] == ' ' or self.current_line[i] == '\n')):
      self.current_column += 1
      i += 1

    lexeme = self.get_current_char()
    while(self.current_column < len(self.current_line)):

      if(self.get_current_char() in self.separators):
        if(lexeme == self.get_current_char()):
          self.current_column += 1
          if(self.current_column < len(self.current_line)):
            likely_token = lexeme + self.get_current_char()
            if(likely_token in self.lexeme_table):
              lexeme = likely_token
              self.current_column += 1
        token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, self.lexeme_table.get(lexeme), TokensCategories[self.lexeme_table.get(lexeme)].value)
        self.print_token(token)
        return token 
      
      self.current_column += 1
      if(not(self.get_current_char() in self.separators)):
        lexeme += self.get_current_char();

    
    

  # Funcao para ler uma linha
  def has_next_line(self):
    line = self.file.readline()

    if(not line):
      return False
    
    self.current_line = line
    self.line_count += 1
    self.current_column = 0

    return True


  def has_next_token(self):

    if(self.line_count == 0 and self.current_column == 0):
      if(self.has_next_line()):
        self.print_line()
      else:
        self.print_line()
        return False
    if(re.match('[\s]*$', self.current_line[self.current_column:])):
      while(self.has_next_line()):
        self.print_line()
        if(not re.match('[\s]*$', self.current_line)):
          return True
      return False
    return True






    # while(self.has_next_line()):
    #   print(self.current_line)
    #   if(re.match('[\s]*$', self.current_line)):
    #     print("LINHA COM ESPACO EM BRANCO")
    #     continue
    #   while(self.current_column < len(self.current_line)):
    #     token = self.next_token()

      # Break pra ver somente uma linha por enquanto
      # break
      # self.last_token = self.current_token        
      # print("Valor linha: ", self.current_line)

      
