import random

class init_goblin:
    def __init__(self):
        print("init_goblin created")
        self.entities = []
        self.fp = open("player_init.data", "r+")
        for line in self.fp:
            #name init
            words = line.split()
            entity = {}
            entity['name'] = words[0]
            entity['init'] = int(words[1])
            self.entities.append(entity)
            print("Added:" + entity['name']
                           + str(entity['init']))

    def __del__(self):
        self.fp.seek(0)
        self.fp.truncate(0)
        for entity in self.entities:
            hold_str = ""
            hold_str += entity['entity']
            hold_str += str(entity['init'])
            self.fp.write(hold_str)
        self.fp.close()
        
    def create_output(self, text):
        msg = ''
        
        #!G init roll [name] (bonus)
        if text[2] == 'roll':
            msg = self.roll_init(text)
        if text[2] == 'list':
            msg = self.list_init(text)
        if text[2] == 'clear':
            msg = self.clear_init(text)

        return msg
        
    def roll_init(self, text):
        msg = ''
        name = str(text[3])
        
        entity = {}
        
        entity['name'] = name
        msg += '```'
        msg += name
        msg += '\'s initiative is '
        #plus/minus applied
        if len(text) == 5:
            roll = random.randrange(1, 21)
            msg += str(roll)
            if text[4][0] == '-':
                roll -= int(text[4][1])
                msg += text[4]
            if text[4][0] == '+':
                roll += int(text[4][1])
                msg += text[4]
            msg += " : "
            msg += roll
            entity['init'] = roll 
        #straight roll
        else:
            roll = random.randrange(1, 21)
            msg += str(roll)
            entity['init'] = roll 
        
        self.entities.append(entity)
        return msg
        
    def list_init(self, text):
        msg = ''
        msg += '```'
        
        if not self.entities:
            msg += 'list is empty'
        else:
            counter = 1
            for entity in self.entities:
                msg += str(counter)
                msg += ': '
                msg += entity['name']
                msg += ' ('
                msg += str(entity['init'])
                msg += ')'
                msg += '\n'
                counter += 1
        msg += '```'
        return msg
        
    def next_init(self, text):
        #pop->push, post new list
        pass
        
    def clear_init(self, text):
        msg = '```Clearing all entities```'
        self.entities.clear()
        return msg