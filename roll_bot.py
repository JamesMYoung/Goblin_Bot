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
        if text[2] != 'stats':
            msg = self.roll_dice(text)
        if text[2] == 'stats':
            msg = self.roll_stats(text)
        
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