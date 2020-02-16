import random
import json

from yaccdice import goblin_handle

# The JSON structure should look like something below
# Dictionary of Characters (name = keys)
# characters['Joevellious']
# - Player Name
# - Player Discord Username (useful for automating some aspects?)
# - Core 6 Stats (use another dictionary?)
# Strength
# 
#     Athletics
# 
# Dexterity
# 
#     Acrobatics
#     Sleight of Hand
#     Stealth
# 
# Intelligence
# 
#     Arcana
#     History
#     Investigation
#     Nature
#     Religion
# 
# Wisdom
# 
#     Animal Handling
#     Insight
#     Medicine
#     Perception
#     Survival
# 
# Charisma
# 
#     Deception
#     Intimidation
#     Performance
#     Persuasion


#     Athletics
#     Acrobatics
#     Sleight of Hand
#     Stealth
#     Arcana
#     History
#     Investigation
#     Nature
#     Religion
#     Animal Handling
#     Insight
#     Medicine
#     Perception
#     Survival
#     Deception
#     Intimidation
#     Performance
#     Persuasion




class char_goblin:
    def __init__(self):
        print("Char Goblin Created")
        
        self.characters = []
        
        try:
            self.fp = open("data/character_data.json", "r+")
        except IOError:
            self.fp = open("data/character_data.json", "w")
            self.fp.close()
            self.fp = open("data/character_data.json", "r+")
            
        try:
            self.characters = json.load(self.fp)
            print("Valid character_data file found")
            if len(self.characters) > 0:
                for character in self.characters:
                    print("-Added: " + character['name'])
                    print("Characters loaded from JSON")
        except:
            print("No valid character_data file found, will be created on shutdown")
        
        
        
    def __del__(self):
        self.fp.seek(0)
        self.fp.truncate(0)
        
        json.dump(self.characters, self.fp)
        
        self.fp.close()
        
    def create_output(self, text):
        msg = ''
        
        if text[2] == 'create':
            msg = self.create_char(text)
        if text[2] == 'delete':
            msg = self.delete_char(text)
        if text[2] == 'set':
            msg = self.set_value(text)
            
        return msg
            
    def create_char(self, text):
        # !G char create Joevellious
        msg = ''
        
        for character in self.characters:
            if character['name'] == str(text[3]):
                msg = '```Character already exists```'
                return msg
        

        character = {}
        character['name'] = str(text[3])
        character['player_name'] = "n/a"
        character['level'] = 1
        character['str'] = -1
        character['dex'] = -1
        character['con'] = -1
        character['int'] = -1
        character['wis'] = -1
        character['cha'] = -1
        character['profs'] = {}
        character['profs']['athletics']        = False
        character['profs']['acrobatics']       = False
        character['profs']['sleight_of_hand']  = False
        character['profs']['stealth']          = False
        character['profs']['arcana']           = False
        character['profs']['history']          = False
        character['profs']['investigation']    = False
        character['profs']['nature']           = False
        character['profs']['religion']         = False
        character['profs']['animal_handling']  = False
        character['profs']['insight']          = False
        character['profs']['medicine']         = False
        character['profs']['perception']       = False
        character['profs']['survival']         = False
        character['profs']['deception']        = False
        character['profs']['intimidation']     = False
        character['profs']['performance']      = False
        character['profs']['persuasion']       = False

        character['expert'] = {}
        character['expert']['athletics']       = False
        character['expert']['acrobatics']      = False
        character['expert']['sleight_of_hand'] = False
        character['expert']['stealth']         = False
        character['expert']['arcana']          = False
        character['expert']['history']         = False
        character['expert']['investigation']   = False
        character['expert']['nature']          = False
        character['expert']['religion']        = False
        character['expert']['animal_handling'] = False
        character['expert']['insight']         = False
        character['expert']['medicine']        = False
        character['expert']['perception']      = False
        character['expert']['survival']        = False
        character['expert']['deception']       = False
        character['expert']['intimidation']    = False
        character['expert']['performance']     = False
        character['expert']['persuasion']      = False
        
        self.characters.append(character)
        
        msg += 'Character succesfully created\n'
        msg += '```'
        msg += 'Name: ' + character['name'] + '\n'
        msg += 'Player Name: ' + character['player_name'] + '\n'
        msg += 'Strength: ' + str(character['str']) + '\n'
        msg += 'Dexterity: ' + str(character['dex']) + '\n'
        msg += 'Constitution: ' + str(character['con']) + '\n'
        msg += 'Intelligence: ' + str(character['int']) + '\n'
        msg += 'Wisdom: ' + str(character['wis']) + '\n'
        msg += 'Charisma: ' + str(character['cha']) + '\n'
        msg += '```'
        
        return msg
        
    def delete_char(self, text):        
        for character in self.characters:
            if character['name'] == text[3]:
                self.characters.remove(character)
                
        msg = ''
        msg += '```'
        msg += 'deleted '
        msg += text[3]
        msg += ' from list'
        msg += '```'
        
        
        return msg
        
    def set_value(self, text):
        # !G char set Joevellious int 20
        # This set function can be used to set values for:
        # Player Name
        # Core Stats
        
        name = text[3]
        parameter = text[4]
        value = text[5]
        msg = ''
        
        for character in self.characters:
            if character['name'] == name:
                msg += '```'
                
                if character['name'][-1] == 's':
                    msg += character['name'] + '\' '
                else:
                    msg += character['name'] + '\'s '
                
                
                if parameter == 'str':
                    character['str'] = int(value)
                    msg += 'strength set to ' + str(character['str'])
                if parameter == 'dex':
                    character['dex'] = int(value)
                    msg += 'dexterity set to ' + str(character['dex'])
                if parameter == 'con':
                    character['con'] = int(value)
                    msg += 'constitution set to ' + str(character['con'])
                if parameter == 'int':
                    character['int'] = int(value)
                    msg += 'intelligence set to ' + str(character['int'])
                if parameter == 'wis':
                    character['wis'] = int(value)
                    msg += 'wisdom set to ' + str(character['wis'])
                if parameter == 'cha':
                    character['cha'] = int(value)
                    msg += 'charisma set to ' + str(character['cha'])
                if parameter == 'player_name':
                    character['player_name'] = str(value)
                    msg += 'player name set to ' + str(character['player_name'])

                msg += '```'
                
                return msg
                
        #should only reach this point if no character is found
        msg += '```'
        msg += 'Character not found'
        msg += '```'

        return msg
        
        
        
        
        
        
        
        
        
    
        