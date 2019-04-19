import random
import re

class roll_goblin:
    def __init__(self):
        print("Roll Goblin Created")
        
    def create_output(self, text):
        #To reach this point, the text must have
        #!G roll ... [end]
        #the possible outcomes from this point are
        #stats
        #[num]d[num]
        print("Begin creating output...")
        msg = ""
        
        if text[2] == 'adv':
            msg = self.roll_adv(text)        
        elif text[2] == 'stats':
            msg = self.roll_stats(text)
        elif text[2] != 'stats':
            msg = self.roll_dice(text)
        
        
        return msg
    
    
    def roll_stats(self, text):
        #To reach this point, the text must have
        #!G roll stats [end]
        msg = '```\nSTATS\n'
        for i in range(0,6):
            roll_total = []
            for j in range(4):
                roll_total.append(random.randrange(1,7))
            print("Rolls: ", roll_total)
            roll_total.remove(min(roll_total))
            print("Drop lowest: ", roll_total)
            
            msg += str(sum(roll_total))
            msg += ' '
        msg += '```'
        return msg
    
    def roll_dice(self, text):
        #To reach this point, the text must have
        #!G roll [num]d[num]+/-[bonus] [end]
        
        rolls = []
        #matches both numbers in text[2]
        #i.e. 2d6 would be match[0] = 2 and match[1] = 6
        #match[3] would correspond to the bonus, should it exist
        match = re.findall(r"[0-9]+", text[2])
        for x in range(0, int(match[0])):
            rolls.append(random.randrange(1, int(match[1])+1, 1))
        
        bonus = 0
        bonus_type = None
        if len(match) is 3:
            print("Calculating Bonus...")
            bonus = int(match[2])
            if '+' in text[2]:
                bonus_type = '+'
            if '-' in text[2]:
                bonus_type = '-'
                
        msg = ""
        
        if match[0] == '1':
            msg += '```Roll: '
        else:
            msg += '```Rolls: '
            
        sum_val = 0
        
        for roll in rolls:
            msg += str(roll)
            msg += ' '
            sum_val += roll
        
        if bonus_type != None:
            if bonus_type == '+':
                msg += '\nBONUS: ' + str(bonus)
                sum_val += bonus
            if bonus_type == '-':
                msg += '\nANTI-BONUS: ' + str(bonus)
                sum_val -= bonus
        
        msg += '\nTOTAL: ' + str(sum_val)
        
        if sum_val <= 1:
            msg += ' *oof*'
        
        msg += '```'
        
        return msg
        
    def roll_adv(self, text):
        msg = ''
        msg += '```'
        
        roll_1 = 0
        roll_2 = 0
        
        bonus = 0
        
        print(len(text))
        #!G roll adv +3
        #bonus/antibonus
        if len(text) == 4:
            roll_1 = random.randrange(1, 21)
            roll_2 = random.randrange(1, 21)
            msg += 'roll 1: ' + str(roll_1) + '\n'
            msg += 'roll_2: ' + str(roll_2) + '\n'
            msg += 'bonus: '
            
            if text[3][0] == '-':
                temp = text[3][1:]
                bonus -= int(temp)
                msg += text[3]
            elif text[3][0] == '+':
                temp = text[3][1:]
                bonus += int(temp)
                msg += text[3]
            elif text[3].isdigit():
                #assumes the bonus is positive
                bonus += int(text[3])
                msg += '+'
                msg += text[3]
            
            msg += '\n'
            
            if roll_1 > roll_2:
                msg += 'Result - ' + str(roll_1 + bonus)
            else:
                msg += 'Result - ' + str(roll_2 + bonus)
            
            
            
            
        #no bonus
        elif len(text) < 4:
            roll_1 = random.randrange(1, 21)
            roll_2 = random.randrange(1, 21)
            msg += 'roll 1: ' + str(roll_1) + '\n'
            msg += 'roll_2: ' + str(roll_2) + '\n'
            
            if roll_1 > roll_2:
                msg += 'Result - ' + str(roll_1)
            else:
                msg += 'Result - ' + str(roll_2)
            
        
        msg += '```' 
        return msg