#!/usr/bin/env python3.5
import ply.yacc as yacc
import random

from lexdice import tokens

msg = ''
error_flag = False

def p_term_add(p):
    'term : term PLUS term'
    global msg
    
    msg += 'sum: '
    msg += str(p[1]) + ' + ' + str(p[3]) + '\n'
    msg += ' total: ' + str(p[1] + p[3]) + '\n'
    p[0] = p[1] + p[3]
    
def p_term_sub(p):
    'term : term MINUS term'
    global msg
    
    msg += 'sum: '
    msg += str(p[1]) + ' - ' + str(p[3]) + '\n'
    msg += ' total: ' + str(p[1] - p[3]) + '\n'
    p[0] = p[1] - p[3]

#one roll should result in a single value (?)
def p_roll(p):
    'roll : NUMBER D NUMBER'
    
    global msg
    #print("dice-roll: ", end='')
    msg += "dice-roll: "
    #print(str(p[1]) + "d" + str(p[3]))
    msg += str(p[1]) + "d" + str(p[3]) + "\n"
    
    rolls = []
    for i in range(0, p[1]):
        roll = random.randrange(1, p[3]+1)
        rolls.append(roll)
    
    roll_sum = 0
    if p[1] > 1:
        msg += ' rolls: '
    else:
        msg += ' roll: '
        
    for roll in rolls:
        # If roll hits max, do something special
        if roll == p[3]:
            msg += '*' + str(roll) + '*'
        else:
            msg += str(roll) 
        msg += ', '
        roll_sum += roll
    
    #lazily trims off last ', '
    msg = msg[:-2]
    msg += '\n'
    
    msg += ' total: '
    msg += str(roll_sum)
    if roll_sum <= 1:
        msg += ' *oof*'
    msg += '\n'
        
    print(rolls)
    print(roll_sum)
    
    #p[0] = p[1] + p[3]
    p[0] = roll_sum
    
#this converts roll tokens into number tokens
#I have no idea if this should or should not be done
#but it feels future-proofy, so that's good
def p_roll_conv(p):
    'term : roll'
    p[0] = p[1]

#converts num to term, to be used in calculations
def p_num_conv(p):
    'term : NUMBER'
    p[0] = p[1]

#seemingly, there needs to be a handle for a single term



def p_error(p):
    global error_flag
    error_flag = True
    print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()
print("Parser built")


if __name__ == "__main__":
    while True:
        try:
            s = input('input > ')
        except EOFError:
            break
        if not s: continue
        msg = '```'
        result = parser.parse(s)
        msg += '```'
        print('uwu')
        print(msg)
        print(result)
        
def goblin_handle(roll_str):
    global msg
    global error_flag
    error_flag = False
    msg = '```'
    result = parser.parse(roll_str)
    msg += '```'
    
    if error_flag == True:
        msg = '```Error in setting up dice roll.```'
    return msg