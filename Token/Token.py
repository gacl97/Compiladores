class Token():

  def __init__(self, line_number, column_number, lexeme, token_category, token_category_id):
    self.line_number = line_number
    self.column_number = column_number
    self.lexeme = lexeme
    self.token_category = token_category
    self.token_id = token_category_id

  def print_token(self):
    print("          [{:>04d}, {:>04d}] ({:>04d}, {:>20s}) {{{}}}".format(self.line_number, self.column_number, self.token_id, self.token_category, self.lexeme))
