import json

class macro_goblin:
    def __init__(self):
        self.macro_list = {}
        print('Macro Goblin Created')
        try:
            self.fp = open("data/macro.json", "r+")
        except IOError:
            self.fp = open("data/macro.json", "w")
            self.fp.close()
            self.fp = open("data/macro.json", "r+")
            
        try:
            self.macro_list = json.load(self.fp)
            print("Valid macro file found")
        except:
            print("No valid macro file found, will be created on shutdown")
        
            
    def __del__(self):
        self.fp.seek(0)
        self.fp.truncate(0)
        
        print("Saving macro list...")
        json.dump(self.macro_list, self.fp)
        
        self.fp.close()
        
        
        
    def create_output(self, text):
        msg = ''
        new_text = None
        
        if text[1] == 'create':
            command_name = text[2]
            command = text[3:]
            
            if command_name in self.macro_list.keys():
                msg = '```Command already registered```'
                new_text = None
            else:
                msg = '```Command registered```'
                self.macro_list[command_name] = command
            
        
        elif text[1] == 'delete':
            pass
        else:
            # check macro_list
            # if exist, replace text
            # otherwise print none found
            command_name = text[1]
            
            if command_name in self.macro_list.keys():
                msg = '```Command found```'
                new_text = self.macro_list[command_name]
                new_text.insert(0, '!G')
                print(self.macro_list)
                print(new_text)
            else:
                msg = '```Command not found```'
                new_text = None
            
        
        
        print(msg, new_text)
        return msg, new_text