import random

from yaccdice import goblin_handle


class enemy_goblin:
    def __init__(self):
        print("Enemy Goblin Created")
        self.enemies = []
        try:
            self.fp = open("data/enemy_list.data", "r+")
        except IOError:
            self.fp = open("data/enemy_list.data", "w")
            self.fp.close()
            self.fp = open("data/enemy_list.data", "r+")
            
    def __del__(self):
        self.fp.seek(0)
        self.fp.truncate(0)
        for enemy in self.enemies:
            hold_str = ""
            hold_str += enemy['name'] + " " 
            hold_str += str(enemy['damage_done']) + " "
            hold_str += str(enemy['temp_hp']) + "\n"
            self.fp.write(hold_str)
        self.fp.close()
        
        
        
    def create_output(self, text):
        msg = ''
        
        if text[2] == 'create':
            msg = self.create_enemy(text)
        if text[2] == 'delete':
            msg = self.delete_enemy(text)
        if text[2] == 'hurt':
            msg = self.hurt_enemy(text)
        if text[2] == 'heal':
            msg = self.heal_enemy(text)
        # temp_hp
        if text[2] == 'clear':
            msg = msg.clear_enemies(text)
        if text[2] == 'list':
            msg = self.list_enemies(text)
        
        return msg
        
    def create_enemy(self, text):
        # !G enemy create [name]
        # Creates an enemy with [name] and 0 damage done
        
        name = str(text[3])
        
        enemy = {}
        enemy['name'] = name
        enemy['damage_done'] = 0
        enemy['temp_hp'] = 0
        
        for e in self.enemies:
            if enemy['name'] == e['name']:
                msg = '```Enemy already exists```'
                return msg
                
        self.enemies.append(enemy)
        
        msg = ''
        msg += 'Enemy created'
        msg += '```'
        msg += enemy['name']
        msg += ' --- Damage Taken:('
        msg += str(enemy['damage_done'])
        msg += ')'
        msg += '```'
        
        
        return msg
        
    def delete_enemy(self, text):
        for enemy in self.enemies:
            if enemy['name'] == text[3]:
                self.enemies.remove(enemy)

        msg = ''
        msg += '```'
        msg += 'deleted '
        msg += text[3]
        msg += ' from list'
        msg += '```'
        return msg    
    
    def clear_enemies(self, text):
        msg = '```Clearing all enemies```'
        self.enemies.clear()
        return msg
    
    def list_enemies(self, text):
        msg = ''
        msg += '```'

        if not self.enemies: 
            msg += 'list is empty'
        else:
            for enemy in self.enemies:
            	msg += enemy['name']
            	msg += ' '
            	msg += '- damage taken:('
            	msg += str(enemy['damage_done'])
            	msg += ')'
            	if enemy['temp_hp'] > 0:
            	    msg += ' - Temp HP: '
            	    msg += str(enemy['temp_hp'])
            	msg += '\n'
            
        msg += '```'
        return msg
        
        
    def heal_enemy(self, text):
        #!G enemy heal goblin 5
        
        input_str = ''.join(text[4:])
        msg, result = goblin_handle(input_str)
        print(msg)
        # Clears the 'empty string' case from the dice roller
        if msg == '``````':
            msg = ''
            
        if isinstance(result, list):
            msg += '```'
            msg += 'Error: result in the form of a list - operation requires single value'
            msg += '```'
            return msg
        elif isinstance(result, float):
            msg += '```'
            msg += 'rounding value ' + str(result) + ' to ' + str(int(result))
            msg += '```'
            result = int(result)
            
        for enemy in self.enemies:
            if enemy['name'] == text[3]:
                #enemy['hp'] += int(text[4])
                enemy['damage_done'] -= result
                if enemy['damage_done'] < 0:
                    enemy['damage_done'] = 0
                msg += '```'
                msg += enemy['name']
                msg += ' healed for '
                msg += str(result)
                msg += ' health ('
                msg += '-'
                msg += str(enemy['damage_done'])
                msg += ')'
                
                if enemy['temp_hp'] > 0:
                    msg += ' - Temp HP: '
                    msg += str(enemy['temp_hp'])
                
                msg += '```'
                
                return msg

        #should only reach this point if no enemy is found
        msg += '```'
        msg += 'enemy not found'
        msg += '```'

        return msg    
        
        
        
        
        
        
        
        
        
        
        
        