from typing import List, Union

NodeType = Union[
    # Main
    "Program",
    
    # Literals
    "Identifier",
    "NumericLiteral",
    #"StringLiteral",
    "NullLiteral",
    
    # Assignment
    #"VariableAssignment",
    
    # Expressions
    "BinaryExpression",
    #"CallExpression",
    #"UnaryExpression",
    
    # Functions
    #"FunctionDeclaration",
    #"FunctionCall"
]

class Statement:
    def __init__(self, type: NodeType):
        self.type = type

class Program(Statement):
    def __init__(self, body: List[Statement]):
        self.type = "Program"
        self.body = body

class Expression(Statement):
    pass

class BinaryExpression(Expression):
    def __init__(self, left: Expression, right: Expression, operator: str):
        self.type = "BinaryExpression"
        self.left = left
        self.right = right
        self.operator = operator

class Identifier(Expression):
    def __init__(self, symbol: str):
        self.type = "Identifier"
        self.symbol = symbol

class NumericLiteral(Expression):
    def __init__(self, value: float):
        self.type = "NumericLiteral"
        self.value = value

class NullLiteral(Expression):
    def __init__(self):
        self.type = "NullLiteral"
        self.value = "null"
