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
            "intelligence", "wisdom", "charisma",
            "level", "speed"           
            ]
        self.bool_keywords = [
            "proficiency", "expertise"
        ]
        self.misc_keywords = [
            "player name"
            ]
        
        self.skill_to_core = {
            "athletics" : "strength",
            "acrobatics" : "dexterity",
            "sleight of hand" : "dexterity",
            "stealth" : "dexterity",
            "arcana" : "intelligence",
            "history" : "intelligence",
            "investigation" : "intelligence",
            "nature" : "intelligence",
            "religion" : "intelligence",
            "animal handling" : "wisdom",
            "insight" : "wisdom",
            "medicine" : "wisdom",
            "perception" : "wisdom",
            "survival" : "wisdom",
            "deception" : "charisma",
            "intimidation" : "charisma",
            "performance" : "charisma",
            "persuasion" : "charisma"
        }
        
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
        if text[2] == 'roll':
            msg = self.char_roll(text)
        if text[2] == 'print':
            msg = self.print_sheet(text)
            
            
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
        
        #if parameter == 'proficiency' or parameter == 'expertise':
        if parameter in self.bool_keywords:
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
                

                msg += '```'
                
                return msg
                
        #should only reach this point if no character is found
        msg += '```'
        msg += 'Character not found'
        msg += '```'

        return msg
        
    def char_roll(self, text):
        # !G char roll Joevellious int
        # !G char roll Joevellious arcana
        msg = ''
        name = text[3]
        
        for character in self.characters:
            if character['name'] == name:
                
                roll_type = None
                guessed_word = ''
                best_match = 0
                
                for keyword in self.core_keywords + self.skill_keywords:
                    word_dist = jaro_winkler(keyword, str(text[4]))
                    
                    if best_match < word_dist:
                        guessed_word = keyword
                        best_match = word_dist
                    # (may) Need to change: if word_dist == 1.0, it's a perfect match
                    if keyword == text[4]:
                        roll_type = text[4]
        
                if roll_type == None:
                    msg += 'Could not find parameter \"' + str(text[4]) + '\"\n'
                    msg += 'Goblin Bot will assume you meant ' + guessed_word + '\n'
                    roll_type = guessed_word
                
                # Should add error message if the stat has not been set yet
                # i.e. if stat == -1, return error message
                if roll_type in self.core_keywords:
                    
                    roll_mod = int((int(character[roll_type]) - 10) / 2)
                    
                    roll_str = '1d20 + ' + str(roll_mod)
                    
                    msg, result = goblin_handle(roll_str)
                    
                elif roll_type in self.skill_keywords:
                    roll_mod = 0
                    prof_bonus = 0
                
                    roll_mod += int((int(character[self.skill_to_core[roll_type]]) - 10) / 2)
                
                    level = int(character['level'])
                    if level >= 1 and level <= 4:
                        prof_bonus = 2
                    elif level >= 5 and level <= 8:
                        prof_bonus = 3
                    elif level >= 9 and level <= 12:
                        prof_bonus = 4
                    elif level >= 13 and level <= 16:
                        prof_bonus = 5
                    else:
                        prof_bonus = 6
                    
                    
                    if (character['proficiency'][roll_type] == True and
                        character['expertise'][roll_type] == False):
                        
                        roll_mod += prof_bonus
                        
                    elif (character['proficiency'][roll_type] == True and
                          character['expertise'][roll_type] == True):

                        roll_mod += prof_bonus * 2
                    else:
                        # This catches both the default case of no bonuses,
                        # as well as the case in which the player sets expertise
                        # without proficiency
                        #roll_mod += int(character[self.skill_to_core[roll_type]])
                        
                        # Do nothing?
                        
                        pass
                        
                    roll_str = '1d20 + ' + str(roll_mod)
                    roll_msg, result = goblin_handle(roll_str)
                    msg += roll_msg
                
                return msg
        
        #should only reach this point if no character is found
        msg += '```'
        msg += 'Character not found'
        msg += '```'

        return msg
        
        
        
    def print_sheet(self, text):
        # !G char print Joevellious sheet
        msg = ''
        name = text[3]
        
        for character in self.characters:
            if character['name'] == name:
                msg += '```\n'
                str_mod = int((character['strength'] - 10) / 2)
                dex_mod = int((character['dexterity'] - 10) / 2)
                con_mod = int((character['constitution'] - 10) / 2)
                int_mod = int((character['intelligence'] - 10) / 2)
                wid_mod = int((character['wisdom'] - 10) / 2)
                cha_mod = int((character['charisma'] - 10) / 2)
                
                
                
                
                msg += '+-----------------------------------------+\n'
                msg += '| {0:39} |'.format(character['name']) + '\n'
                msg += '|{0:41}|'.format('') + '\n'
                msg += '| +---------+{0:29}|'.format('') + '\n'
                msg += '| | STR:{0:3d} |      Saving Throws          |'.format(character['strength']) + '\n'
                msg += '| | mod:{0:+3d} |    [ ] {1:+3d} Strength         |'.format(str_mod, str_mod) + '\n'
                
                msg += '```'
                return msg
        
        
        #should only reach this point if no character is found
        msg += '```'
        msg += 'Character not found'
        msg += '```'

        return msg
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        