class misc_goblin:
    def __init__(self):
        self.fp = open("gold.data", "r+")
        self.gold_counter = int(self.fp.read())
        print('Misc Goblin Created')
        
        
    def __del__(self):
        print("Stashing gold into hoard")
        self.fp.seek(0)
        self.fp.truncate(0)
        self.fp.write(str(self.gold_counter))
        self.fp.close()
        
    def create_output(self, text):
        msg = ''
        if text[1] == 'give':
            msg = self.give_goblin(text)
        if text[1] == 'take':
            msg = self.take_goblin(text)
            
        return msg
    
    def give_goblin(self, text):
        msg = ''
        if text[2] == 'gold':
            self.gold_counter += 1
            msg = ":moneybag:The Goblin now has {} gold:moneybag:".format(self.gold_counter)
        if text[2] == 'smooch':
            msg ='*smooch*\n'
        if text[2] == 'hug':
            msg = "```The goblin gives you a biiiiig hug.```"
        return msg
    
    def take_goblin(self, text):
        msg = ''
        if text[2] == 'gold':
            msg = "```The goblin hits you over the head with his bag of gold, and you lose 10 good boy points.```"
        return msg
        