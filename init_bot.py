import random

class init_goblin:
    def __init__(self):
        print("init_goblin created")
        self.entities = []
        try:
            self.fp = open("data/player_init.data", "r+")
        except IOError:
            self.fp = open("data/player_init.data", "w")
            self.fp.close()
            self.fp = open("data/player_init.data", "r+")
        
        #self.fp = open("player_init.data", "r+")
        for line in self.fp:
            #name init
            words = line.split()
            entity = {}
            entity['name'] = words[0]
            entity['init'] = int(words[1])
            self.entities.append(entity)
            print("Added:" + entity['name']+"("
                           + str(entity['init']) + ")")

    def __del__(self):
        self.fp.seek(0)
        self.fp.truncate(0)
        for entity in self.entities:
            hold_str = ""
            hold_str += entity['name'] + " "
            hold_str += str(entity['init']) + "\n"
            self.fp.write(hold_str)
        self.fp.close()
        
    def create_output(self, text):
        msg = ''
        
        #!G init roll [name] (bonus)
        if text[2] == 'roll':
            msg = self.roll_init(text)
        if text[2] == 'add':
            msg = self.add_init(text)
        if text[2] == 'delete':
            msg = self.del_init(text)
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
        #if name is in list, return error message
        for e in self.entities:
            if entity['name'] == e['name']:
                msg = '```Entity already exists```'
                return msg
        
        msg += '```'
        msg += name
        msg += '\'s initiative is '
        #plus/minus applied
        if len(text) == 5:
            roll = random.randrange(1, 21)
            msg += str(roll)
            if text[4][0] == '-':
                temp = text[4][1:]
                roll -= int(temp)
                msg += text[4]
            elif text[4][0] == '+':
                temp = text[4][1:]
                roll += int(temp)
                msg += text[4]
            elif text[4].isdigit():
                #assumes the bonus is positive
                roll += int(text[4])
                msg += '+'
                msg += text[4]
            msg += " : "
            msg += str(roll)
            entity['init'] = roll 
        #straight roll
        else:
            roll = random.randrange(1, 21)
            msg += str(roll)
            entity['init'] = roll 
        
        self.entities.append(entity)
        self.entities.sort(key=lambda r: r['init'], reverse = True)
        
        msg += '```'
        return msg
        
    def add_init(self, text):
        msg = ''
        #!G init add Dazzak 3
        entity = {}
        entity['name'] = text[3]
        entity['init'] = int(text[4])

        self.entities.append(entity)
        self.entities.sort(key=lambda r: r['init'], reverse = True)

        msg += '```'
        msg += text[3]
        msg += ' added to table with initiative '
        msg += text[4]
        msg += '```'
        
        return msg
        
    def del_init(self, text):
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
        
    def list_init(self, text):
        msg = ''
        msg += '**__Initiative Order__**'
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