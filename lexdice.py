#!/usr/bin/env python3.5

import ply.lex as lex

# Goals for this project
# 1: Get simple 1d20 rolls working [SEEMINGLY WORKS]
# 2: Add in +/- with simple numbers [SEEMINGLY WORKS AS WELL]
# 3: Get +/- to work with other dice rolls [WORKS]
# 4: Slide in divide and multiply
# 5: See how to start handling paranthesis
# 6: See how to implement advantage maybe?
# 7: At this point, it's just loose requirements



tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'COMMA',
	'COLON',
    'D',
	'ADV',
	'DIS',
	'RR'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r','
t_COLON   = r':'
t_D = r'[dD]'
t_ADV = r'[aA][dD][vV]'
t_DIS = r'[dD][iI][sS]'
t_RR = r'[rR][rR]'



# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

print("Lexer built")

if __name__ == '__main__':
    data = '1d20'
    
    lexer.input(data)
    
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)  