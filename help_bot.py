class help_goblin:
    def __init__(self):
        print("Help Goblin Created")
        
    def create_output(self, text):
        msg = ""
        
        if text[1] == "help":
            msg = self.all_help()
        
        return msg
    
    def all_help(self):
        msg = ""
        
        #Rolling, either !G4 or !G roll amount d dice + bonus
        #Can also !Gflip which will flip a coin
        #Spell lookup, !G lookup [spell] desc for description
        #[spell] range for range
        #give gold
        #give smooch
        #give hug
        #take gold
        
        msg += "__**Rolling**__\n"
        msg += "```"
        msg += "Rolling can be done in two ways:\n"
        msg += "!G[number]\n"
        msg += "   -rolls any of the standard D&D dice [2, 4, 6, 8, 10, 20, 100]\n"
        #msg += "ex: !G20 will roll a 1d20.\n"
        msg += "!Gflip\n"
        msg += "   -flips a coin, and will give either a heads or a tails.\n"
        msg += "!G roll [amount]d[dice size]\n"
        msg += "   -rolls multiple dice and total the rolls.\n"
        #msg += "ex: !G roll 4d6 will roll 4 d6 dice.\n"
        msg += "!G roll [amount]d[dice size]+[bonus]\n"
        msg += "   -rolls multiple dice, and then adds a bonus.\n"
        msg += "!G roll [amount]d[dice size]-[bonus]\n"
        msg += "   -rolls multiple dice, and then adds a anti-bonus.\n"
        #msg += "ex: !G roll 1d20+5 will roll a d20 and add 5 to that roll.\n"
        msg += "```"
        msg += "\n"
        
        msg += "__**Health**__\n"
        msg += "```"
        msg += "!G health create [entity name] [max hp]\n"
        msg += "   -creates a new entity on the health table and sets their max health\n"
        msg += "!G health delete [entity name]\n"
        msg += "   -deletes the sepcified entity from the health table\n"
        msg += "!G health clear\n"
        msg += "   -deletes all entities from the health table\n"
        msg += "!G health list\n"
        msg += "   -lists the current entities and their health\n"
        msg += "!G health heal [entity name] [heal amount]\n"
        msg += "   -heals the specified entity by the specified amount\n"
        msg += "!G health hurt [entity name] [damage amount]\n"
        msg += "   -damages the specified entity by the specified amount\n"
        msg += "```"
        msg += "\n"
        
        msg += "__**Spell Lookup**__\n"
        msg += "```"
        msg += "!G lookup spell [spell name] desc will return a description of the specified spell.\n"
        msg += "!G lookup spell [spell name] range will return the range of the specified spell.\n"
        msg += "!G lookup spell [spell name] duration will return the duration of the specified spell\n"
        msg += "!G lookup spell [spell name] cast_time will return the casting time of the specified spell\n"
        msg += "!G lookup spell [spell name] components will return the required components of the specified spell\n"
        msg += "```"
        msg += "\n"
        
        msg += "__**Other Stuff**__\n"
        msg += "```"
        msg += "!G give gold - give the goblin his rightful gold.\n"
        msg += "!G give smooch - uwu\n"
        msg += "!G give hug - get that good hug\n"
        msg += "!G take gold - evil, don't do this\n"
        msg += "```"
        msg += "\n"
        
        
        return msg
        
        