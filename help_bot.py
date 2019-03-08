class help_goblin:
    def __init__(self):
        print("Help Goblin Created")
        
    def create_output(self, text):
        msg = ""
        
        if len(text) == 2:
            msg = self.help_prompt()
        elif text[2] == "roll":
            msg = self.roll_help()
        elif text[2] == "health":
            msg = self.health_help()
        elif text[2] == "spell" and text[3] == "lookup":
            msg = self.spell_lookup_help()
        elif text[2] == "misc":
            msg = self.misc_help()

        return msg
    
    def roll_help(self):
        msg = ""
        
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
        
        return msg
    
    def health_help(self):
        msg = ""
        
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
        msg += "!G health temp [entity name] [temp hp amount]\n"
        msg += "   -sets the specified entity's temporary hit points to specified amount\n"
        msg += "!G health reduce [entity name] [max hp reduction amount]\n"
        msg += "   -reduces the specified entity's maximum hit points by the specified amount\n"
        msg += "!G health restore [entity name] [max hp restoration amount]\n"
        msg += "   -restores the specified entity's maximum hit points by the specified amount\n"
        msg += "!G health set max [entity name] [max hp amount]\n"
        msg += "   -set the specified entity's maximum hit points to the specified amount\n"
        msg += "   -*note, this is typically used for level ups, as it restores current hp as well\n"
        msg += "```"
        msg += "\n"
        
        return msg
    
    def spell_lookup_help(self):
        msg = ""
        
        msg += "__**Spell Lookup**__\n"
        msg += "```"
        msg += "!G lookup spell [spell name] desc will return a description of the specified spell.\n"
        msg += "!G lookup spell [spell name] range will return the range of the specified spell.\n"
        msg += "!G lookup spell [spell name] duration will return the duration of the specified spell\n"
        msg += "!G lookup spell [spell name] cast_time will return the casting time of the specified spell\n"
        msg += "!G lookup spell [spell name] components will return the required components of the specified spell\n"
        msg += "```"
        msg += "\n"
        
        return msg
    
    def misc_help(self):
        msg = ""
        
        msg += "__**Other Stuff**__\n"
        msg += "```"
        msg += "!G give gold - give the goblin his rightful gold.\n"
        msg += "!G give smooch - uwu\n"
        msg += "!G give hug - get that good hug\n"
        msg += "!G take gold - evil, don't do this\n"
        msg += "```"
        msg += "\n"
        
        return msg
    
    def help_prompt(self):
        msg = ""

        msg += "Possible help topics include:"
        msg += "roll help: Help for roll functionality"
        msg += "health help: Help for health functionality"
        msg += "spell lookup help: Help for spell lookup functionality"
        msg += "misc help: Fun things :)"
        
        return msg
    
    #This function is now decpreciated as it is too large of an output
    #for discord to handle it
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
        msg += "!G health temp [entity name] [temp hp amount]\n"
        msg += "   -sets the specified entity's temporary hit points to specified amount\n"
        msg += "!G health reduce [entity name] [max hp reduction amount]\n"
        msg += "   -reduces the specified entity's maximum hit points by the specified amount\n"
        msg += "!G health restore [entity name] [max hp restoration amount]\n"
        msg += "   -restores the specified entity's maximum hit points by the specified amount\n"
        msg += "!G health set max [entity name] [max hp amount]\n"
        msg += "   -set the specified entity's maximum hit points to the specified amount\n"
        msg += "   -*note, this is typically used for level ups, as it restores current hp as well\n"
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
        
        