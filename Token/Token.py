class Token():

  def __init__(self, line_number, column_number, lexeme, token_category):
    self.line_number = line_number
    self.column_number = column_number
    self.lexeme = lexeme
    self.token_category = token_category
    # self.token_id
