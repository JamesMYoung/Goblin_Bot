import random
import json
from Levenshtein import jaro_winkler

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
        self.skill_keywords = [
            "athletics", "acrobatics", "sleight of hand",
            "stealth", "arcana", "history", "investigation",
            "nature", "religion", "animal handling",
            "insight", "medicine", "perception", "survival",
            "deception", "intimidation", "performance",
            "persuasion"
            ]
        self.core_keywords = [
            "strength", "dexterity", "constitution",
            "intelligence", "wisdom", "charisma"        
            ]
        self.bool_keywords = [
            "proficiency", "expertise"
        ]
        self.misc_keywords = [
            "player name"
            ]
        
        
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
        character['player name'] = "n/a"
        character['level'] = 1
        for c in self.core_keywords:
            character[c] = -1
        character['proficiency'] = {}
        character['expertise'] = {}
        for s in self.skill_keywords:
            character['proficiency'][s] = False
            character['expertise'][s] = False
        
        self.characters.append(character)
        
        msg += 'Character succesfully created\n'
        msg += '```'
        msg += 'Name: ' + character['name'] + '\n'
        msg += 'Player Name: ' + character['player name'] + '\n'
        msg += 'Strength: ' + str(character['strength']) + '\n'
        msg += 'Dexterity: ' + str(character['dexterity']) + '\n'
        msg += 'Constitution: ' + str(character['constitution']) + '\n'
        msg += 'Intelligence: ' + str(character['intelligence']) + '\n'
        msg += 'Wisdom: ' + str(character['wisdom']) + '\n'
        msg += 'Charisma: ' + str(character['charisma']) + '\n'
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
        # Proficiencies and Expertise
        # !G char set Joevellious athletics expertise
        
        msg = ''
        name = text[3]
        parameter = None
        guessed_word = ''
        best_match = 0
        
        for keyword in self.core_keywords + self.misc_keywords + self.bool_keywords:
            
            word_dist = jaro_winkler(keyword, str(text[4]))
            if best_match < word_dist:
                guessed_word = keyword
                best_match = word_dist
            
            if keyword == text[4]:
                parameter = text[4]
        
        if parameter == None:
            msg += 'Could not find parameter \"' + str(text[4]) + '\"\n'
            msg += 'Goblin Bot will assume you meant ' + guessed_word + '\n'
            parameter = guessed_word
        
        value = text[5]
        
        if parameter == 'proficiency' or parameter == 'expertise':
            value = None
            guessed_word = ''
            best_match = 0
            
            for keyword in self.skill_keywords:
                word_dist = jaro_winkler(keyword, str(text[5]))
                if best_match < word_dist:
                    guessed_word = keyword
                    best_match = word_dist
                if keyword == text[5]:
                    value = text[5]
            
            if value == None:
                msg += 'Could not find parameter \"' + str(text[5]) + '\"\n'
                msg += 'Goblin Bot will assume you meant ' + guessed_word + '\n'
                value = guessed_word
            
        
        #value = None
        #bool_dist_check = 0
        #best_match = ''
        #for b in self.bool_keywords:
        #    word_dist = jaro_winkler(b, str(text[5]))
        #    print("prof, exp word_dist val: " + str(word_dist))
        #    if word_dist > 0.5 and word_dist > bool_dist_check:
        #        bool_dist_check = word_dist
        #        best_match = b
        #
        #if value == None:
        #    value = text[5]
        #else:
        #    msg += 'Could not find parameter \"' + str(text[5]) + '\"'
        #    msg += 'Goblin Bot will assume you meant ' + best_match + '\n'
        #    skill = best_match
        
        
        
        for character in self.characters:
            if character['name'] == name:
                msg += '```'
                
                if character['name'][-1] == 's':
                    msg += character['name'] + '\' '
                else:
                    msg += character['name'] + '\'s '
                
                
                
                if parameter in self.bool_keywords:
                    # Could potentially add expertise error checking
                    # aka you need proficiency for expertise
                    if character[parameter][value] == False:
                        character[parameter][value] = True
                        msg += parameter + ' in ' + value + ' changed from False to True\n'
                    else:
                        character[parameter][value] = False
                        msg += parameter + ' in ' + value + ' changed from True to False\n'
                        
                elif parameter in self.core_keywords:
                    # Add some error checking here for integer values
                    character[parameter] = int(value)
                    msg += parameter + ' set to ' + str(character[parameter])
                elif parameter in self.misc_keywords:
                    character[parameter] = str(value)
                    msg += parameter + ' set to ' + str(character[parameter])
                
                
                
                
                
                #if parameter == 'str':
                #    character['str'] = int(value)
                #    msg += 'strength set to ' + str(character['str'])
                #if parameter == 'dex':
                #    character['dex'] = int(value)
                #    msg += 'dexterity set to ' + str(character['dex'])
                #if parameter == 'con':
                #    character['con'] = int(value)
                #    msg += 'constitution set to ' + str(character['con'])
                #if parameter == 'int':
                #    character['int'] = int(value)
                #    msg += 'intelligence set to ' + str(character['int'])
                #if parameter == 'wis':
                #    character['wis'] = int(value)
                #    msg += 'wisdom set to ' + str(character['wis'])
                #if parameter == 'cha':
                #    character['cha'] = int(value)
                #    msg += 'charisma set to ' + str(character['cha'])
                #if parameter == 'player_name':
                #    character['player_name'] = str(value)
                #    msg += 'player name set to ' + str(character['player_name'])

                msg += '```'
                
                return msg
                
        #should only reach this point if no character is found
        msg += '```'
        msg += 'Character not found'
        msg += '```'

        return msg
        
        
        
        
        
        
        
        
        
    
        