from frontend.language_ast import (
    Program,
    Statement,
    Expression,
    BinaryExpression,
    Identifier,
    NumericLiteral,
    NullLiteral
)

from frontend.lexer import (
    tokenize,
    Token,
    TokenType
)

class Parser:
    def __init__(self):
        self.tokens = []

    def not_eof(self) -> bool:
        return self.tokens[0].type != TokenType.EOF

    def at(self) -> Token:
        return self.tokens[0]

    def eat(self) -> Token:
        return self.tokens.pop(0)

    def expect(self, token_type: TokenType, message: str) -> Token:
        prev = self.eat()
        
        if not prev or prev.type != token_type:
            raise ValueError(message)
        
        return prev

    def produce_ast(self, source_code: str) -> Program:
        self.tokens = tokenize(source_code)
        program = Program(type= "Program", body=[ ])
        
        while self.not_eof():
            program.body.append(self.parse_statement())
        
        return program

    def parse_statement(self) -> Statement:
        return self.parse_expression()

    def parse_expression(self) -> Expression:
        return self.parse_additive_expression()

    def parse_additive_expression(self) -> Expression:
        left = self.parse_multiplicative_expression()
        
        while self.at().value in ["+", "-"]:
            operator = self.eat().value
            right = self.parse_multiplicative_expression()
            left = BinaryExpression(type="BinaryExpression", left=left, right=right, operator=operator)
        
        return left

    def parse_multiplicative_expression(self) -> Expression:
        left = self.parse_primary_expression()
        
        while self.at().value in ["*", "/", "%"]:
            operator = self.eat().value
            right = self.parse_primary_expression()
            left = BinaryExpression(type="BinaryExpression", left=left, right=right, operator=operator)
        
        return left

    def parse_primary_expression(self) -> Expression:
        token_type = self.at().type
        
        if token_type == TokenType.Identifier:
            return Identifier(type="Identifier", symbol=self.eat().value)
        
        elif token_type == TokenType.Null:
            self.eat()
            return NullLiteral(type="NullLiteral", value="null")
        
        elif token_type == TokenType.Number:
            return NumericLiteral(type="NumericLiteral", value=float(self.eat().value))
        
        elif token_type == TokenType.OpenParenthesis:
            self.eat()
            value = self.parse_expression()
            self.expect(TokenType.CloseParenthesis, "Unexpected token found inside parenthesized expression. Expected ')'.")
            
            return value
        else:
            raise ValueError(f"Unexpected token {self.at().value} of type {TokenType[self.at().type]}")
