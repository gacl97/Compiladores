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
    self.lexeme_table = LexemeTable().token_map

  def get_current_char(self):
    return str(self.current_line[self.current_column])
  
  def print_line(self):

    # print(self.current_line[len(self.current_line)-1])
    if(self.current_line[len(self.current_line)-1] == "\n"):
      print("{:>4d}  {}".format(self.line_count, self.current_line), end="")
    else:
      print("{:>4d}  {}".format(self.line_count, self.current_line))
  

  def print_token(self, token):
    print("          [{:>04d}, {:>04d}] ({:>04d}, {:>20s}) {{{}}}".format(token.line_number, token.column_number, token.token_id, token.token_category, token.lexeme))

  def next_token(self):

    i = self.current_column
    while(i < len(self.current_line) and (self.current_line[i] == ' ' or self.current_line[i] == '\n')):
      self.current_column += 1
      i += 1

    lexeme = self.get_current_char()
    
    # Caso de ser um número
    if(re.match('[0-9]', lexeme)):
      self.current_column += 1
      while(self.current_column < len(self.current_line)):
        if(re.match('[0-9]', self.get_current_char())):
          lexeme += self.get_current_char()
          self.current_column += 1
          continue 
        # Caso seja um ponto flutuante
        if(self.get_current_char() != '.'):
          if(re.match('^[0-9]+\.[0-9]+', lexeme)):
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.floatVal.name, TokensCategories["floatVal"].value)
            return token
          # Caso seja um inteiro
          elif(re.match('[0-9]$', lexeme)):
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.intVal.name, TokensCategories["intVal"].value)
            return token
          # Caso contrário, não é um token não identificado
          else:
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.notDefined.name, TokensCategories["notDefined"].value)
            return token

        if(self.get_current_char() == '.' and re.match('[0-9]', lexeme)):
          lexeme += self.get_current_char()
          self.current_column += 1
    
    #Demais Casos

    while(self.current_column < len(self.current_line)):

      if(self.get_current_char() in self.separators):
        #Caso de string
        if(lexeme == '"' or lexeme == '\''):
          self.current_column += 1
          while(self.current_column < len(self.current_line)):
            if(self.get_current_char() != '\n'):
              lexeme += self.get_current_char()
            if((self.get_current_char() == '"' and lexeme[0] == '"') or (self.get_current_char() == '\'' and lexeme[0] == '\'')):
              self.current_column += 1
              break
            self.current_column += 1
          if(lexeme[0] == '"' and lexeme[-1] == '"'):
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.stringVal.name, TokensCategories["stringVal"].value)
            return token
          elif(lexeme[0] == '\'' and lexeme[-1] == '\'' and len(lexeme) == 3):
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.charVal.name, TokensCategories["charVal"].value)
            return token

        #Caso de haver a uniao de 2 separadores
        elif(lexeme == self.get_current_char()):
          self.current_column += 1
          if(self.current_column < len(self.current_line)):
            likely_token = lexeme + self.get_current_char()
            if(likely_token in self.lexeme_table):
              lexeme = likely_token
              self.current_column += 1
          
          token = None
          if(lexeme in self.lexeme_table):
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, self.lexeme_table.get(lexeme), TokensCategories[self.lexeme_table.get(lexeme)].value)
          else:
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.notDefined.name, TokensCategories["notDefined"].value)
          
          return token

        else:
          # Verificar se é reservado
          if(lexeme in self.lexeme_table):
            token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, self.lexeme_table.get(lexeme), TokensCategories[self.lexeme_table.get(lexeme)].value)
            return token
          else:
            # Verificar se é um identificador
            if(re.match("[a-zA-Z]([A-Za-z0-9\_]*)", lexeme)):
              token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.identifier.name, TokensCategories["identifier"].value)
              return token          

        # Se não for nenhum dos anteriores não é identificado
        token = Token(self.line_count, self.current_column - len(lexeme) + 1, lexeme, TokensCategories.notDefined.name, TokensCategories["notDefined"].value)
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
      
      self.line_count += 1
      self.current_line = "EOF"
      self.print_line()
      token = Token(self.line_count, 1, "", TokensCategories.EOF.name, TokensCategories["EOF"].value)
      self.print_token(token)
      return False
    return True