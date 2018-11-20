#-----------------------------------------------------------------
# Using some code from tutorial.py
#-----------------------------------------------------------------
import wrapper
import sys

from pycparser import parse_file
from minic.minic_ast import *
sys.path.extend(['.', '..'])

if len(sys.argv) < 2:
    print "Please specify filename"
    exit()

ast = parse_file('./tests/c_files/inputs/new_' + sys.argv[1] + '.c')

class LHSPrinter(NodeVisitor):
    def __init__(self):
        self.names = []
    
    def visit_Assignment(self, node):
        if node.lvalue.name not in self.names:
            self.names.append(node.lvalue.name)

class VariablesPrinter(NodeVisitor):
    def __init__(self):
        self.names = []
    
    def visit_ID(self, node):
        if node.name not in self.names:
            self.names.append(node.name)
        
# Call ID visitor on the root node to get names of all variables (Variables is of type ID node)
def get_variables(fullc_ast):
    v = VariablesPrinter()
    v.visit(fullc_ast)
    print("Variables: {}".format(v.names))
    
    lhs = LHSPrinter()
    lhs.visit(fullc_ast)
    print("Written Variables: {}".format(lhs.names))

get_variables(ast)
