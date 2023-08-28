from enum import Enum

class TokenType(Enum):
    Identifier = 1
    Null = 2
    Number = 3
    String = 4
    Var = 5
    Assignment = 6
    Operator = 7
    OpenParenthesis = 8
    CloseParenthesis = 9
    EOF = 10

keywords = {
    "let": TokenType.Var,
    "null": TokenType.Null,
}

class Token:
    def __init__(self, value: str, type: TokenType):
        self.value = value
        self.type = type

def tokenize(input_str: str):
    tokens = []
    src = list(input_str)
    
    def token(value, token_type):
        return Token(value, token_type)
    
    def is_alphabetic(src_char):
        return src_char.isalpha()
    
    def is_int(src_char):
        return src_char.isdigit()
    
    def is_skippable(src_char):
        return src_char in ['', ' ', '\n', '\t']
    
    while src:
        if src[0] == "(":
            tokens.append(token(src.pop(0), TokenType.OpenParenthesis))
            
        elif src[0] == ")":
            tokens.append(token(src.pop(0), TokenType.CloseParenthesis))
            
        elif src[0] in ['+', '-', '*', '/', '%']:
            tokens.append(token(src.pop(0), TokenType.Operator))
            
        elif src[0] == "=":
            tokens.append(token(src.pop(0), TokenType.Assignment))
            
        else:
            if is_int(src[0]):
                num = ""
                while src and is_int(src[0]):
                    num += src.pop(0)
                
                tokens.append(token(num, TokenType.Number))
                
            elif is_alphabetic(src[0]):
                identifier = ""
                while src and is_alphabetic(src[0]):
                    identifier += src.pop(0)
                
                keyword = keywords.get(identifier)
                
                if keyword is not None:
                    tokens.append(token(identifier, keyword))
                else:
                    tokens.append(token(identifier, TokenType.Identifier))
                    
            elif is_skippable(src[0]):
                src.pop(0)
            else:
                raise ValueError(f"Unexpected token {src[0]}")
    
    tokens.append(token("EndOfFile", TokenType.EOF))
    return tokens