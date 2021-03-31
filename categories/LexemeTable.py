from Token.TokensCategories import TokensCategories

class LexemeTable():

  def __init__(self):
    self.token_map = {
      "main": TokensCategories.main.name,
      "int": TokensCategories.typeInt.name,
      "float": TokensCategories.typeFloat.name,
      "char": TokensCategories.typeChar.name,
      "string": TokensCategories.typeString.name,
      "bool": TokensCategories.typeBool.name,
      "for": TokensCategories.cmdFor.name,
      "while": TokensCategories.cmdWhile.name,
      "if": TokensCategories.cmdIf.name,
      "elif": TokensCategories.cmdElif.name,
      "else": TokensCategories.cmdElse.name,
      "function": TokensCategories.funcDecl.name,
      "return": TokensCategories.funcRtn.name,
      ";": TokensCategories.semicolon.name,
      ",": TokensCategories.commaSep.name,
      "!": TokensCategories.opNot.name,
      "&&": TokensCategories.opAnd.name,
      "||": TokensCategories.opOr.name,
      "True": TokensCategories.constTrue.name,
      "False": TokensCategories.constFalse.name,
      "=": TokensCategories.opAtt.name,
      "==": TokensCategories.opEquals.name,
      "!=": TokensCategories.opDiff.name,
      ">": TokensCategories.opGtrThan.name,
      "<": TokensCategories.opLessThan.name,
      ">=": TokensCategories.opGtrEqual.name,
      "<=": TokensCategories.opLessEq.name,
      "+": TokensCategories.opAdd.name,
      "-": TokensCategories.opSub.name,
      "/": TokensCategories.opDiv.name,
      "*": TokensCategories.opMult.name,
      ".": TokensCategories.opConcat.name,
      "input": TokensCategories.funcRead.name,
      "print": TokensCategories.funcPrint.name,
      "(": TokensCategories.paramBegin.name,
      ")": TokensCategories.paramEnd.name,
      "[": TokensCategories.arrayBegin.name,
      "]": TokensCategories.arrayEnd.name,
      "{": TokensCategories.scopeBegin.name,
      "}": TokensCategories.scopeEnd.name,
      "EOF": TokensCategories.EOF.name,
    }