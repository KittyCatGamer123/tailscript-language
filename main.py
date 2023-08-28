from frontend.parser import Parser
from runtime.interpreter import evaluate
import pprint

def tailscript():
    parser = Parser()
    print("TailScript | WIP-2023.08.28 Edition")
    
    while True:
        code = input()
        if not code or code == "exit": break
        
        program = parser.produce_ast(code)
        result = evaluate(program)
        
        pp = pprint.PrettyPrinter(depth=None)
        pp.pprint(result)

tailscript()