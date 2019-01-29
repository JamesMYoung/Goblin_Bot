class health_goblin:
    def __init__(self):
        self.entities = []
        print("Health Goblin Created")
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
        entity['hp'] = hp
        
        
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
            	msg += ')\n'
            
        msg += '```'
        return msg

    def heal_entity(self, text):
        #!G health heal dazzak 5
        msg = ''
        for entity in self.entities:
            if entity['name'] == text[3]:
                entity['hp'] += int(text[4])
                if entity['hp'] > entity['max_hp']:
                    entity['hp'] = entity['max_hp']
                msg += '```'
                msg += entity['name']
                msg += ' restored '
                msg += text[4]
                msg += ' health ('
                msg += str(entity['hp'])
                msg += '/'
                msg += str(entity['max_hp'])
                msg += ')```'
                
                return msg

        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'

        return msg

    def hurt_entity(self, text):
        msg = ''
        for entity in self.entities:
            if entity['name'] == text[3]:
                entity['hp'] -= int(text[4])
                if entity['hp'] < 0:
                    entity['hp'] = 0

                msg += '```'
                msg += entity['name']
                msg += ' took '
                msg += text[4]
                msg += ' damage ('
                msg += str(entity['hp'])
                msg += '/'
                msg += str(entity['max_hp'])
                msg += ')```'

                return msg
            
        #should only reach this point if no entity is found
        msg += '```'
        msg += 'Entity not found'
        msg += '```'
        
        return msg