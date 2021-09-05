# Open this File with c_ast.sh
# ./c_ast.sh complete_ast.py

from __future__ import division
import sys,os
import ply.lex as lex
import ply.yacc as yacc

graph = open("graph.dot","r+")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
        'NAME','INT','FLOAT',
)

literals = ['=','+','-','*','/','(',')','%','^',',']

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_FLOAT(t):
    r'\d+[eE][-+]?\d+|(\.\d+|\d+\.\d+)([eE][-+]?\d+)?'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'(\d+|0[Xx]\d+)'
    if t.value.startswith(('0x','0X')):
        t.value = int(t.value,16)              
    elif t.value.startswith('0'):
        t.value = int(t.value,8)
    else:
        t.value = int(t.value)
    return t

t_ignore = " \t\n"

def t_error(t): 
    print("Invalid character '%s'" % t.value[0])
    t.lexer.skip(1)


precedence = (
    ('left', '+', '-'),
    ('left', '*', '/','%'),
    ('right', 'UMINUS'),
    ('left', '^'),
)

var = {}


def p_assign(p):
    '''st : NAME '=' exp'''
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[1]))
    node = node + 1
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[2]))
    graph.writelines("n%d -> {n%d; n%d};\n"%(node, node-1, p[3][1]))
    p[0]=p[2],node
    node = node + 1

def p_plus(p):
    "exp : exp '+' exp"
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[2]))
    graph.writelines("n%d -> {n%d; n%d};\n"%(node, p[1][1], p[3][1]))
    p[0]=p[2],node
    node = node + 1 

def p_minus(p):
    "exp : exp '-' exp"
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[2]))
    graph.writelines("n%d -> {n%d; n%d};\n"%(node, p[1][1], p[3][1]))
    p[0] = p[2], node
    node = node + 1

def p_mult(p):
    "exp : exp '*' exp"
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[2]))
    graph.writelines("n%d -> {n%d; n%d};\n"%(node, p[1][1], p[3][1]))
    p[0]=p[2], node
    node = node + 1

def p_div(p):
    "exp : exp '/' exp"
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[2]))
    graph.writelines("n%d -> {n%d; n%d};\n"%(node, p[1][1], p[3][1]))
    p[0] = p[2], node
    node = node + 1

def p_mod(p):
    "exp : exp '%' exp"
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[2]))
    graph.writelines("n%d -> {n%d; n%d};\n"%(node, p[1][1], p[3][1]))
    p[0]=p[2], node
    node = node + 1

def p_pow(p):
    "exp : exp '^' exp"
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[2]))
    graph.writelines("n%d -> {n%d; n%d};\n"%(node, p[1][1], p[3][1]))
    p[0]=p[2], node
    node = node + 1

def p_uminus(p):
    "exp : '-' exp %prec UMINUS"
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[1]))
    graph.writelines("n%d -> n%d;\n"%(node, p[2][1]))
    p[0]=p[1], node
    node = node + 1

def p_group(p):
    "exp : '(' exp ')'"
    p[0]=p[2]

def p_complex(p):
    "exp : '(' exp ',' exp ')'"
    p[0] = complex(p[2],p[4])

def p_num(p):
    '''exp : INT 
           | FLOAT
    '''
    p[0]=p[1]
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[1]))
    p[0]=p[1], node
    node = node + 1

def p_var(p):
    'exp : NAME'
    if p[1] == 'exit':
        sys.exit()
    elif p[1] == 'clear':
        os.system("clear")
        p[0] = ''

    for i in var:
        if i==p[1]:
            p[0]=var[p[1]]
            return
    p[0]=0
    global node
    graph.writelines("n%d [ label =\"%s\"];\n"%(node, p[1]))
    p[0]=p[1], node
    node = node + 1

def p_exp(p):
    'st : exp'

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")   


try:
    data = raw_input('')
except EOFError:
    sys.exit()
except KeyboardInterrupt:
    sys.exit()
            
global node
node = 0
    
graph.writelines("digraph {\n")
    
lex.lex()
yacc.yacc()
yacc.parse(data)
    
graph.writelines("}\n")
