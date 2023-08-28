from runtime.values import (
    ValueType, 
    RuntimeValue, 
    NumberValue, 
    NullValue
)

from frontend.language_ast import (
    BinaryExpression, 
    NumericLiteral, 
    Statement, 
    Program
)

def evaluate(ast_node: Statement) -> RuntimeValue:
    match ast_node.type:
        case "NumericLiteral":
            return NumberValue(value=ast_node.value)
        
        case "NullLiteral":
            return NullValue()
        
        case "BinaryExpression":
            return evaluate_binary_expression(ast_node)

        case "Program":
            return evaluate_program(ast_node)
        
        case _:
            raise ValueError(f'Unknown AST node of type {ast_node.type}')

def evaluate_program(program: Program) -> RuntimeValue:
    last_evaluated = NullValue()
    
    for statement in program.body:
        last_evaluated = evaluate(statement)
    
    return last_evaluated

def evaluate_binary_expression(binary_operation: BinaryExpression) -> RuntimeValue:
    left_hand = evaluate(binary_operation.left)
    right_hand = evaluate(binary_operation.right)
    
    if isinstance(left_hand, NumberValue) and isinstance(right_hand, NumberValue):
        return evaluate_numeric_binary_expression(left_hand, right_hand, binary_operation.operator)
    else:
        return NullValue()

def evaluate_numeric_binary_expression(left: NumberValue, right: NumberValue, operator: str) -> RuntimeValue:
    result = 0
    match operator:
        case "+":
            result = left.value + right.value
        case "-":
            result = left.value - right.value
        case "*":
            result = left.value * right.value
        case "/":
            result = left.value / right.value
        case "%":
            result = left.value % right.value
    return NumberValue(result)
