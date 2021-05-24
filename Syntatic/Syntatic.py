from Lexic.Lexical import Lexical
from Token.Token import Token
from Token.TokensCategories import TokensCategories
import traceback


class Syntatic:

  token = 0

  def __init__(self, file_name):

    try:
      file = open(file_name, 'r')
    except Exception:
      traceback.print_exc()

    self.lexical_analyser = Lexical(file=file)
    self.S()

    
  def GetToken(self):
    if(self.lexical_analyser.has_next_token()):
      return self.lexical_analyser.next_token()
  
  def PrintProduction(self, str1, str2):
    print("          {:s} = {:s}".format(str1, str2))

  def S (self):
    token = self.GetToken()
    
    if(token.token_category == TokensCategories.typeInt.name):
      self.PrintProduction("S", "'typeInt' SR")
      token.print_token()
      self.SR()


  def SR(self):
    token = self.GetToken()
    if(token.token_category == TokensCategories.funcDecl.name):
      self.PrintProduction("SR", "'funcDecl' SAux")
      token.print_token()
      self.SAux()
    # elif(token.token_category == TokensCategories.identifier.name):
    #   self.DeclVar()
    #   self.S()
    # elif(token.token_category == TokensCategories.arrayBegin.name):
    #   self.DeclArrOpc()
  
  def SAux(self):
    token = self.GetToken()
    if(token.token_category == TokensCategories.main.name):
      self.PrintProduction("SAux", "'main' Main")
      token.print_token()
      self.Main()
    elif(token.token_category == TokensCategories.identifier.name):
      self.PrintProduction("SAux", "'identifier' DeclFun S")
      token.print_token()
      self.DeclFun()
      self.S()
  
  # def DeclVar(self):
  #   print("DeclVar")

  def Main(self):
    self.PrintProduction("Main", "Params Body")
    self.Params()
    # print("Main = Params Body")

  def DeclFun(self):
    self.PrintProduction("DeclFun", "Params Body")
    # print("DeclFun = Params Body")

  def Params(self):
    token = self.GetToken()
    if(token.token_category == TokensCategories.paramBegin.name):
      self.PrintProduction("Param", "'(' Param ')'")
      token.print_token()
      self.Param()

  def Param(self):
    token = self.GetToken()
    self.PrintProduction("Param", "VarType")













  # def NotIntType(self):
  #   return token.token_category

  #   if(self.lexical_analyser.has_next_token()):
  #     current_token = self.lexical_analyser.next_token()

  #   if(current_token.token_category == TokensCategories.funcDecl.name):
  #     self.DeclFun()
  #     self.S()
  #   elif(current_token.token_category == TokensCategories.main.name):
  #     self.Main()
    
  # def DeclFun(self):
  #   print("asuidhaisudh")
  # def Main(self):
  #   print("OK")