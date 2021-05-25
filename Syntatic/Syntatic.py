from re import T
from Lexic.Lexical import Lexical
from Token.Token import Token
from Token.TokensCategories import TokensCategories
import traceback


class Syntatic:


  def __init__(self, file_name):

    self.epsilon = "ε"
    try:
      file = open(file_name, 'r')
    except Exception:
      traceback.print_exc()

    self.lexical_analyser = Lexical(file=file)
    self.token = self.GetToken()
    self.S()

    
  def GetToken(self):
    if(self.lexical_analyser.has_next_token()):
      return self.lexical_analyser.next_token()
  
  def PrintProduction(self, str1, str2):
    print("          {:s} = {:s}".format(str1, str2))

  def checkCategory(self, categories):
    for category in categories:
      if(self.token.token_category == category.name):
        return True
    return False

  def UnexpectedToken(self, expected):
    print("Error: Expected {:s} at [{:>04d}, {:>04d}] but got {:s}".format(expected, self.token.line_number, self.token.column_number, self.token.token_category))
    quit()

  def S (self):
    # self.token = self.GetToken()
  
    if(self.token.token_category == TokensCategories.typeInt.name):
      self.PrintProduction("S", "'typeInt' SR")
      self.token.print_token()
      self.token = self.GetToken()
      self.SR()


  def SR(self):
    # self.token = self.GetToken()
    if(self.token.token_category == TokensCategories.funcDecl.name):
      self.PrintProduction("SR", "'funcDecl' SAux")
      self.token.print_token()
      self.token = self.GetToken()
      self.SAux()
    # elif(token.token_category == TokensCategories.identifier.name):
    #   self.DeclVar()
    #   self.S()
    # elif(token.token_category == TokensCategories.arrayBegin.name):
    #   self.DeclArrOpc()
  
  def SAux(self):
    # self.token = self.GetToken()
    if(self.token.token_category == TokensCategories.main.name):
      self.PrintProduction("SAux", "'main' Main")
      self.token.print_token()
      self.token = self.GetToken()
      self.Main()
    elif(self.token.token_category == TokensCategories.identifier.name):
      self.PrintProduction("SAux", "'identifier' DeclFun S")
      self.token.print_token()
      self.token = self.GetToken()
      self.DeclFun()
      self.S()
  
  # def DeclVar(self):
  #   print("DeclVar")

  def Main(self):
    if(self.token.token_category == TokensCategories.paramBegin.name):
      self.PrintProduction("Main", " '(' ')' Body")
      self.token.print_token()
      self.token = self.GetToken()
      if(self.token.token_category == TokensCategories.paramEnd.name):
        self.token.print_token()
        self.token = self.GetToken()
        self.Body()
      else:
        self.UnexpectedToken("')'")
    else:
      self.UnexpectedToken("'('")
        

  def DeclFun(self):
    self.PrintProduction("DeclFun", " '(' Params ')' Body")
    # self.token = self.GetToken()
    if(self.token.token_category == TokensCategories.paramBegin.name):
      self.token.print_token()
      self.token = self.GetToken()  
      self.Params()
      self.token = self.GetToken()
      if(self.token.token_category == TokensCategories.scopeBegin.name):
        self.Body()
      else:
        self.UnexpectedToken("'{'")
    else:
      self.UnexpectedToken("'('")

  def Params(self):
    # self.token = self.GetToken()
    if(self.checkCategory([TokensCategories.typeInt, TokensCategories.typeFloat, TokensCategories.typeString, TokensCategories.typeChar, TokensCategories.typeBool])):
      self.PrintProduction("Params", "VarType 'identifier' ArrOpc Paramsx")
      # self.token.print_token()
      self.VarType()
      self.token = self.GetToken()
      if(self.token.token_category != TokensCategories.identifier.name):
        self.UnexpectedToken("'identifier'")
      else:
        self.token.print_token()
        self.token = self.GetToken()
        self.ArrOpc()
        self.Paramsx()
    else:
      self.PrintProduction("Params", self.epsilon)
      self.token.print_token()

  def VarType(self):
    if(self.token.token_category == TokensCategories.typeInt.name):
      self.PrintProduction("VarType", "'typeInt'")
      self.token.print_token()
    elif(self.token.token_category == TokensCategories.typeFloat.name):
      self.PrintProduction("VarType", "'typeFloat'")
      self.token.print_token()
    elif(self.token.token_category == TokensCategories.typeString.name):
      self.PrintProduction("VarType", "'typeString'")
      self.token.print_token()
    elif(self.token.token_category == TokensCategories.typeChar.name):
      self.PrintProduction("VarType", "'typeChar'")
      self.token.print_token()
    elif(self.token.token_category == TokensCategories.typeBool.name):
      self.PrintProduction("VarType", "'typeBool'")
      self.token.print_token()

  def ArrOpc(self):
    if(self.token.token_category != TokensCategories.arrayBegin.name):
       self.PrintProduction("ArrOpc", self.epsilon)
       self.token.print_token()
    else:
      self.PrintProduction("ArrOpc", "'[' ArrSizeObg ']'")
      self.token.print_token()
      self.token = self.GetToken()
      self.ArrSizeObg()
      self.token = self.GetToken()
      if(self.token.token_category != TokensCategories.arrayEnd.name):
        self.UnexpectedToken("']'")
      self.token.print_token()
      self.token = self.GetToken()

  def Paramsx(self):
    if(self.token.token_category == TokensCategories.commaSep.name):
      self.PrintProduction("Paramsx", "',' VarType 'identifier' ArrOpc Paramsx")
      self.token = self.GetToken()
      if(self.checkCategory([TokensCategories.typeInt, TokensCategories.typeFloat, TokensCategories.typeChar, TokensCategories.typeString, TokensCategories.typeBool])):
        self.VarType()
        self.token = self.GetToken()
        if(self.token.token_category == TokensCategories.identifier.name):
          self.token.print_token()
          self.token = self.GetToken()
          self.ArrOpc()
          self.Paramsx()
        else:
          self.UnexpectedToken("'identifier'")
      else:
        self.UnexpectedToken("'typeInt', 'typeFloat', 'typeChar', 'typeString' ou 'typeBool'")
    elif(self.token.token_category == TokensCategories.paramEnd.name):
      self.PrintProduction("Paramsx", self.epsilon)
    else:
      self.UnexpectedToken("')'")
          

  def ArrSizeObg(self):
    if(self.token.token_category == TokensCategories.identifier.name):
      self.PrintProduction("ArrSizeObg", "'identifier'")
      self.token.print_token()
    elif(self.token.token_category == TokensCategories.intVal.name):
      self.PrintProduction("ArrSizeObg", "'intVal'")
      self.token.print_token()
    else:
      self.UnexpectedToken("'identifier', 'intVal'")

  def Body(self):
    self.PrintProduction("Body", "'{' Content '}'")
    self.token.print_token()
    self.token = self.GetToken()
    self.Content()
    if(self.token.token_category == TokensCategories.scopeEnd.name):
      self.token.print_token()
    else:
      self.UnexpectedToken("'}'")

  def Content(self):
    if(self.checkCategory([TokensCategories.cmdIf, TokensCategories.cmdWhile, TokensCategories.cmdFor, TokensCategories.funcRead, TokensCategories.funcPrint])):
      self.PrintProduction("Content", "Command Content")
      self.token.print_token()
      self.Command()

  def Command(self):
    if(self.token.token_category == TokensCategories.cmdIf.name):
      self.PrintProduction("Command", "'cmdIf' '(' Eb ')' Body LElif CmdElse")
      self.token = self.GetToken()
      if(self.token.token_category == TokensCategories.paramBegin.name):
        self.token.print_token()
        self.token = self.GetToken()
        self.Eb()
        if(self.token.token_category == TokensCategories.paramEnd.name):
          self.token.print_token()
          self.token = self.GetToken()
          if(self.token.token_category == TokensCategories.scopeBegin.name):
            self.Body()
          else:
            self.UnexpectedToken("'{'")
        else:
          self.UnexpectedToken("')'")
      else:
        self.UnexpectedToken("'('")

  def Ea(self):
    self.PrintProduction("Ea", "Ta Eax")
    self.Ta()
    self.Eax()

  def Eax(self):
    if(self.checkCategory([TokensCategories.opAdd, TokensCategories.opSub])):
      if(self.token.token_category == TokensCategories.opAdd):
        self.PrintProduction("Eax", "'opAdd' Fa Eax")
      elif(self.token.token_category == TokensCategories.opSub):
        self.PrintProduction("Eax", "'opSub' Fa Eax")
      self.token.print_token()
      self.token = self.GetToken()
    else:
      self.PrintProduction("Eax", self.epsilon)
  
  def Ta(self):
    self.PrintProduction("Ta", "Fa Tax")
    self.Fa()
    self.Tax()

  def Tax(self):
    if(self.checkCategory([TokensCategories.opMult, TokensCategories.opDiv, TokensCategories.opMod])):
      if(self.token.token_category == TokensCategories.opMult):
        self.PrintProduction("Tax", "'opMult' Fa Tax")
      elif(self.token.token_category == TokensCategories.opDiv):
        self.PrintProduction("Tax", "'opDiv' Fa Tax")
      elif(self.token.token_category == TokensCategories.opMod):
        self.PrintProduction("Tax", "'opMod' Fa Tax")
      self.token.print_token()
      self.token = self.GetToken()
    else:
      self.PrintProduction("Tax", self.epsilon)

  def Fa(self):
    if(self.token.token_category == TokensCategories.paramBegin.name):
      self.PrintProduction("Fa", "'(' Ec ')'")
      self.token.print_token()
      self.token = self.GetToken()
      self.Ec()
      self.token = self.GetToken()
      if(self.token.token_category == TokensCategories.paramEnd):
        self.token.print_token()
      else:
        self.token.print_token()
        self.UnexpectedToken(")")
    elif(self.token.token_category == TokensCategories.opUnaryNeg.name):
      self.PrintProduction("Fa", "'opUnaryNeg' Fa ")
      self.token.print_token()
      self.token = self.GetToken()
      if(self.token.token_category == TokensCategories.opUnaryNeg.name):
        self.token.print_token()
        self.UnexpectedToken("'(', VarOrFunc, 'intVal', 'floatVal', 'stringVal', 'charVal', 'boolVal'")
      self.Fa()
    elif(self.token.token_category == TokensCategories.identifier.name):
      self.PrintProduction("Fa", "VarOrFunc")
      self.VarOrFunc()

  def VarOrFunc(self):
    self.PrintProduction("VarOrFunc", "'identifier' VarOrFuncx")
    self.token.print_token()
    self.token = self.GetToken()
    if(self.token.token_category == TokensCategories.arrayBegin.name):
      self.PrintProduction("VarOrFuncx","'[' Ea ']'")
      self.token.print_token()
      self.token = self.GetToken()
      self.Ea()
    elif(self.token.token_category == TokensCategories.paramBegin.name):
      self.PrintProduction("VarOfFuncx", "'(' ParamsCall ')'")
      self.token.print_token()
      self.token = self.GetToken()
      self.ParamsCall()
    else:
      self.PrintProduction("VarOrFuncx", self.epsilon)

  def ParamsCall(self):
    if(self.token.token_category == TokensCategories.paramEnd.name):
      self.PrintProduction("ParamsCall", self.epsilon)
    else:
      self.PrintProduction("ParamsCall", "Ec ParamsCallx")
      self.token.print_token()
      self.token = self.GetToken()
      self.Ec()
      # self.ParamsCallx()
    

  def Ec(self):
    self.PrintProduction("Ec", "Eb Ecx")
    self.Eb()
    self.Ecx()
  
  def Ecx(self):
    if(self.token.token_category == TokensCategories.opConcat.name):
      self.PrintProduction("Ecx", "'opConcat' Eb Ecx")
      self.token.print_token()
      self.token = self.GetToken()
      self.Eb()
      self.Ecx()
    else:
      self.PrintProduction("Ecx", self.epsilon)

  def Eb(self):
    self.PrintProduction("Eb", "Tb Ebx")
    self.Tb()
    self.Ebx()

  def Ebx(self):
    if(self.token.token_category == TokensCategories.opOr.name):
      self.PrintProduction("Ebx", "'opOr' Tb Ebx")
      self.token.print_token()
      self.token = self.GetToken()
      self.Tb()
      self.Ebx()
    else:
      self.PrintProduction("Ebx", self.epsilon)
  
  def Tb(self):
    self.PrintProduction("Tb", "Fb Tbx")
    self.Fb()
    self.Tbx()

  def Tbx(self):
    if(self.token.token_category == TokensCategories.opAnd.name):
      self.PrintProduction("Tbx", "'opAnd' Fb Tbx")
      self.token.print_token()
      self.token = self.GetToken()
      self.Fb()
      self.Tbx()
    else:
      self.PrintProduction("Tbx", self.epsilon)

  def Fb(self):
    if(self.token.token_category == TokensCategories.opNot.name):
      self.PrintProduction("Fb", "'opNot' Fb")
      self.token.print_token()
      self.token = self.GetToken()
      self.Fb()
    else:
      self.PrintProduction("Fb", "Ra Fbx")
      self.Ra()
      self.Fbx()

  def Fbx(self):
    if(self.checkCategory([TokensCategories.opGtrThan, TokensCategories.opLessThan, TokensCategories.opGtrEqual, TokensCategories.opLessEq])):
      if(self.token.token_category == TokensCategories.opGtrThan.name):
        self.PrintProduction("Fbx", "'opGtrThan' Ra Fbx")
      elif(self.token.token_category == TokensCategories.opLessThan.name):
        self.PrintProduction("Fbx", "'opLessThan' Ra Fbx")
      elif(self.token.token_category == TokensCategories.opGtrEqual.name):
        self.PrintProduction("Fbx", "'opGtrEqual' Ra Fbx")
      elif(self.token.token_category == TokensCategories.opLessEq.name):
        self.PrintProduction("Fbx", "'opLessEq' Ra Fbx")  
      self.token.print_token()
      self.token = self.GetToken()
      self.Ra()
      self.Fbx()
    else:
      self.PrintProduction("Fbx", self.epsilon)

  def Ra(self):
    self.PrintProduction("Ra", "Ea Rax")
    self.Ea()
    self.Rax()

  def Rax(self):
    if(self.checkCategory([TokensCategories.opEquals, TokensCategories.opDiff])):
      if(self.token.token_category == TokensCategories.opEquals):
        self.PrintProduction("Rax", "'opEquals' Ea Rax")
      elif(self.token.token_category == TokensCategories.opDiff):
        self.PrintProduction("Rax", "'opDiff' Ea Rax")
      self.token.print_token()
      self.token = self.GetToken()
      self.Ea()
      self.Rax()
    else:
      self.PrintProduction("Rax", self.epsilon)