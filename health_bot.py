import random

from yaccdice import goblin_handle

class health_goblin:
    def __init__(self):
        print("Health Goblin Created")
        self.entities = []
        try:
            self.fp = open("player_health.data", "r+")
        except IOError:
            self.fp = open("player_health.data", "w")
            self.fp.close()
            self.fp = open("player_health.data", "r+")
        
        
        #self.fp = open("player_health.data", "r+")
        for line in self.fp:
            words = line.split()
            entity = {}
            entity['name'] = words[0]
            entity['hp'] = int(words[1])
            entity['max_hp'] = int(words[2])
            entity['true_max'] = int(words[3])
            entity['temp_hp'] = int(words[4])
            self.entities.append(entity)
            print("Added:" + entity['name'] + "("
                           + str(entity['hp']) + "/"
                           + str(entity['max_hp']) + ") - temp_hp: "
                           + str(entity['temp_hp']))
        
        
        
    def __del__(self):
        self.fp.seek(0)
        self.fp.truncate(0)
        for entity in self.entities:
            hold_str = ""
            hold_str += entity['name'] + " " 
            hold_str += str(entity['hp']) + " "
            hold_str += str(entity['max_hp']) + " "
            hold_str += str(entity['true_max']) + " "
            hold_str += str(entity['temp_hp']) + "\n"
            self.fp.write(hold_str)
        self.fp.close()
        
        
    def create_output(self, text):
        msg = ''
        
        if text[2] == 'create':
            msg = self.create_entity(text)
        if text[2] == 'delete':
            msg = self.delete_entity(text)
        if text[2] == 'clear':
            msg = self.clear_entities(text)
        if text[2] == 'list':
            msg = self.list_entities(text)
        if text[2] == 'heal':
            msg = self.heal_entity(text)
        if text[2] == 'hurt':
            msg = self.hurt_entity(text)
        if text[2] == 'long' and text[3] == 'rest':
            msg = self.long_rest(text)
        if text[2] == 'temp':
            msg = self.temp_health(text)
        if text[2] == 'reduce':
            msg = self.reduce_max(text)
        if text[2] == 'restore':
            msg = self.restore_max(text)
        if text[2] == 'set' and text[3] == 'max':
            msg = self.set_max_hp(text)
        
        
            
        return msg
    
    def create_entity(self, text):
        #text[3] = name of character
        #text[4] = max HP of character
        name = str(text[3])
        max_hp = int(text[4])
        hp = int(text[4])
        
        entity = {}
        
        entity['name'] = name
        entity['max_hp'] = max_hp
        entity['true_max'] = max_hp
        entity['hp'] = hp
        entity['temp_hp'] = 0
        
        
        #need to add duplicate checking here
        for e in self.entities:
            if entity['name'] == e['name']:
                msg = '```Entity already exists```'
                return msg

        self.entities.append(entity)
        
        msg = ''
        msg += 'Entity created'
        msg += '```'
        msg += entity['name']
        msg += ' HP:('
        msg += str(entity['hp'])
        msg += '/'
        msg += str(entity['max_hp'])
        msg += ')'
        msg += '```'
        
        return msg
    def delete_entity(self, text):
        for entity in self.entities:
            if entity['name'] == text[3]:
                self.entities.remove(entity)

        msg = ''
        msg += '```'
        msg += 'deleted '
        msg += text[3]
        msg += ' from list'
        msg += '```'
        return msg

    def clear_entities(self, text):
        msg = '```Clearing all entities```'
        self.entities.clear()
        return msg

    def list_entities(self, text):
        msg = ''
        msg += '```'

        if not self.entities: 
            msg += 'list is empty'
        else:
            for entity in self.entities:
            	msg += entity['name']
            	msg += ' '
            	msg += 'HP:('
            	msg += str(entity['hp'])
            	msg += '/'
            	msg += str(entity['max_hp'])
            	msg += ')'
            	if entity['temp_hp'] > 0:
            	    msg += ' - Temp HP: '
            	    msg += str(entity['temp_hp'])
            	msg += '\n'
            
        msg += '```'
        return msg

    def heal_entity(self, text):
        #!G health heal dazzak 5
        
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
            
        for entity in self.entities:
            if entity['name'] == text[3]:
                #entity['hp'] += int(text[4])
                entity['hp'] += result
                if entity['hp'] > entity['max_hp']:
                    entity['hp'] = entity['max_hp']
                if entity['hp'] < 0:
                    entity['hp'] = 0
                msg += '```'
                msg += entity['name']
                msg += ' healed for '
                msg += str(result)
                msg += ' health ('
                msg += str(entity['hp'])
                msg += '/'
                msg += str(entity['max_hp'])
                msg += ')'
                
                if entity['temp_hp'] > 0:
                    msg += ' - Temp HP: '
                    msg += str(entity['temp_hp'])
                
                msg += '```'
                
                return msg

        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'

        return msg

    def hurt_entity(self, text):
        input_str = ''.join(text[4:])
        msg, result = goblin_handle(input_str)
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
            
        death_flag = False
        for entity in self.entities:
            if entity['name'] == text[3]:
                #if temp > 0, sub from temp
                #else normal health calculation
                if entity['temp_hp'] > 0:
                    #if damage is greater than temp_hp
                    #subtract temp hp from damage, remove remaining damage
                    #from player hp
                    if int(result) > entity['temp_hp']:
                        remaining_damage = result - entity['temp_hp'] 
                        entity['temp_hp'] = 0
                        entity['hp'] -= remaining_damage
                    #if damage == temp_hp
                    #set temp hp = 0
                    elif int(text[4]) == entity['temp_hp']:
                        entity['temp_hp'] = 0
                    #if damage < temp_hp
                    #subtract only from temp_hp
                    else:
                        entity['temp_hp'] -= result
                        
                    
                else:
                    entity['hp'] -= result
                    
                if entity['hp'] > entity['max_hp']:
                    entity['hp'] = entity['max_hp']
                if entity['hp'] <= 0:
                    entity['hp'] = 0
                    death_flag = True

                msg += '```'
                msg += entity['name']
                msg += ' took '
                msg += str(result)
                msg += ' damage ('
                msg += str(entity['hp'])
                msg += '/'
                msg += str(entity['max_hp'])
                msg += ')'
                if entity['temp_hp'] > 0:
                    msg += ' - Temp HP: '
                    msg += str(entity['temp_hp'])
                
                msg += '```'
                
                if death_flag == True:
                    msg += str(random.choice(['OH SHIT','OH FUCK','HOT DAMN','DANGER']))
                    
                return msg
            
        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'
        
        return msg
        
    #Should reduce max_hp, but leave true_max untouched
    def reduce_max(self, text):
        msg = ''
        for entity in self.entities:
            if entity['name'] == text[3]:
                nervous_flag = False
                entity['max_hp'] -= int(text[4])
                
                #may want to output this to player, but if they
                #reach this point, it's bad news bears
                if entity['max_hp'] < 0:
                    entity['max_hp'] = 0
                    nervous_flag = True
                if entity['hp'] > entity['max_hp']:
                    entity['hp'] = entity['max_hp']
                    
                msg += '```'
                msg += 'Maximum health for '
                msg += entity['name']
                msg += ' reduced by '
                msg += text[4]
                
                msg += ' ('
                msg += str(entity['hp'])
                msg += '/'
                msg += str(entity['max_hp'])
                msg += ')'
                
                msg += '```'
                
                if nervous_flag is True:
                    msg += '*nervous laughter*'
                
                return msg
                
        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'
        
        return msg
        
    #Should restore max_hp, but leave true_max untouched
    def restore_max(self, text):
        msg = ''
        for entity in self.entities:
            if entity['name'] == text[3]:
                amount = int(text[4])
                
                entity['max_hp'] += amount
                
                
                
                #might want to create text output to ensure that this
                #is conveyed to player
                if entity['max_hp'] > entity['true_max']:
                    amount = amount + entity['true_max'] - entity['max_hp'] 
                    entity['max_hp'] = entity['true_max']
                    
                msg += '```'
                msg += 'Maximum health for '
                msg += entity['name']
                msg += ' restored by '
                msg += str(amount)
                
                msg += ' ('
                msg += str(entity['hp'])
                msg += '/'
                msg += str(entity['max_hp'])
                msg += ')'
                
                msg += '```'
                
                return msg
                
        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'
        
        return msg
        
    #this function for adding temp HP
    def temp_health(self, text):
        input_str = ''.join(text[4:])
        msg, result = goblin_handle(input_str)
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
        
        for entity in self.entities:
            
            if entity['name'] == text[3]:
                entity['temp_hp'] = result
                msg += '```'
                msg += 'Temporary HP for '
                msg += entity['name']
                msg += ' set to '
                msg += str(result)
                msg += '```'
            
                return msg
            
        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'
        
        return msg
        
    #This should typically only be invoked during a level up
    def set_max_hp(self, text):
        msg = ''
        for entity in self.entities:
            if entity['name'] == text[4]:
                entity['true_max'] = int(text[5])
                entity['max_hp'] = entity['true_max']
                #entity['hp'] = entity['max_hp']
                msg += '```'
                msg += 'Maximum HP for '
                msg += entity['name']
                msg += ' set to '
                msg += text[5]
                msg += '```'
            
                return msg
        
        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'
        
        return msg
        
    def long_rest(self, text):
        temp_flag = False
        max_flag = False
        msg = ''
        msg += '```'
        for entity in self.entities:
            if entity['temp_hp'] > 0:
                entity['temp_hp'] = 0
                temp_flag = True
            if entity['max_hp'] < entity['true_max']:
                entity['max_hp'] = entity['true_max']
                max_flag = True
            entity['hp'] = entity['max_hp']    
            
        msg += 'All entities healed to full health'
        if temp_flag == True:
            msg += '\nTemporary hit points removed'
        if max_flag == True:
            msg += '\nMaximum hit points restored'
        msg += '```'
        
        return msg