from __future__ import division
import sys,os
import ply.lex as lex
import ply.yacc as yacc

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME', 'NUM',
)

literals = ['=', '+', '-', '*', '/', '(', ')','%','^']

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
    ('left','^'),
    ('left','%'),
)

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t\n"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Invalid character '%s'" % t.value[0])
    t.lexer.skip(1)

var = {}

def p_assign(p):
    'st : NAME "=" exp'
    var[p[1]] = p[3]

def p_oper(p):
    '''exp : exp '+' exp
           | exp '-' exp
           | exp '*' exp
           | exp '/' exp
           | exp '^' exp
           | exp '%' exp
           '''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]


def p_uminus(p):
    "exp : '-' exp %prec UMINUS"
    p[0] = -p[2]

def p_group(p):
    "exp : '(' exp ')'"
    p[0] = p[2]

def p_num(p):
    "exp : NUM"
    p[0] = p[1]

def p_var(p):
    "exp : NAME"
    if p[1] == 'exit':
        sys.exit()
    elif p[1] == 'clear':
        os.system("clear")
        p[0] = ''
    else:
        try:
            p[0] = var[p[1]]
        except LookupError:
            print("No Variable Defined'%s'" % p[1])
            p[0] = 0

def p_expr(p):
    'st : exp'
    print(p[1])

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

while 1:
    try:
        data = raw_input('')
    except EOFError:
        break
    except KeyboardInterrupt:
        sys.exit()
    if not data:
        continue
    lex.lex()
    yacc.yacc()
    yacc.parse(data)


    
