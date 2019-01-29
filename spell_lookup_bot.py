import requests
import json

class spell_lookup_goblin:
    def __init__(self):
        print("Spell Lookup Goblin Created")
        
    def create_output(self, text):
        msg = ""
        
        if text[2] == 'spell':
            msg = self.spell_lookup(text)
        
        return msg
    
    def api_lookup(self, text):
        url = 'http://dnd5eapi.co/api/'
        
        if text[2] == 'spell':
            url += 'spells'
            
            
    def spell_lookup(self, text):
        url = 'http://dnd5eapi.co/api/spells?name='
        prepositions = ['of', 'the', 'with', 'and', 'from', 'without', 'into']
        hold_str = ''
        #print("range is :", len(text))
        spell_name = text[3:-1]
        
        for x in range((len(spell_name))):
            if spell_name[x] in prepositions:
                hold_str += spell_name[x]
            else:
                hold_str += spell_name[x].capitalize()
            hold_str += '+'
            print("hold string", hold_str)
        #remove extra + from end
        hold_str = hold_str[:-1]
        url += hold_str
        print("URL:", url)
        
        response = requests.get(url)
        
        if response.status_code == 200:
            spell_url = json.loads(response.content.decode('utf-8'))['results'][0]['url']
        else:
            return 'Error, api down'
        
        response = requests.get(spell_url)
        
        spell_details = None
        
        if response.status_code == 200:
            spell_details = json.loads(response.content.decode('utf-8'))
        else:
            return 'Error, api down'
        
        msg = ""
        
        msg += hold_str.replace('+', ' ')
        msg += '\n'
        
        
        
        if text[-1] == 'desc':
            msg += '```' 
            msg += spell_details['desc'][0].replace('â€™', '\'')
            msg += '```'
        elif text[-1] == 'range':
            msg += '```'
            msg += spell_details['range']
            msg += '```'
        else:
            msg = 'No specifier provided.'
        return msg
            