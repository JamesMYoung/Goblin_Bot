import random
import json

class deck_goblin:
    def __init__(self):
        print("Deck Goblin Created")
        self.deck = []
        self.drawn = []
        
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.ranks = ["Ace", "Two", "Three", "Four", "Five",
                 "Six", "Seven", "Eight", "Nine", "Ten",
                 "Jack", "Queen", "King"]
        
        
        try:
            self.deck_fp = open("data/deck_data.json", "r+")
        except IOError:
            self.deck_fp = open("data/deck_data.json", "w")
            self.deck_fp.close()
            self.deck_fp = open("data/deck_data.json", "r+")
            
        try:
            self.deck = json.load(self.deck_fp)
            print("Valid deck_data file found")
            if len(self.deck) > 0:
                print("- " + str(len(self.deck)) + " cards remain")
                for c in self.deck:
                    print("-- " + c[0] + " of " + c[1])
        except:
            print("No valid deck_data file found, will be created on shutdown")
        
        
        
        try:
            self.draw_fp = open("data/drawn_data.json", "r+")
        except IOError:
            self.draw_fp = open("data/drawn_data.json", "w")
            self.draw_fp.close()
            self.draw_fp = open("data/drawn_data.json", "r+")
            
        try:
            self.drawn = json.load(self.draw_fp)
            print("Valid drawn_data file found")
        except:
            print("No valid drawn_data file found, will be created on shutdown")
        
        
        
    def __del__(self):
        print("Saving current deck...")
        self.deck_fp.seek(0)
        self.deck_fp.truncate(0)
        
        json.dump(self.deck, self.deck_fp)
        
        self.deck_fp.close()
        
        
        self.draw_fp.seek(0)
        self.draw_fp.truncate(0)
        
        json.dump(self.drawn, self.draw_fp)
        
        self.draw_fp.close()
        
    def create_output(self, text):
        msg = ''
    
        if text[2] == 'create' or text[2] == 'new':
            msg = self.new_deck()
        if text[2] == 'shuffle':
            msg = self.suffle()
        if text[2] == 'draw':
            msg = self.draw(text)
        if text[2] == 'size' or text[2] == 'count':
            msg = self.size()
        
        
        return msg
        
        
    # Saves deck to JSON
    def save_deck(self):
        pass
        
    # Loads deck from JSON
    def load_deck(self):
        pass
        
    # Creates new deck
    def new_deck(self):
        msg = ''
        
        self.deck = []
        self.drawn = []
        
        for s in self.suits:
            for r in self.ranks:
                self.deck.append([r, s])
        print(self.deck)
        
        msg += "``` New Deck Created ```"
        msg += self.shuffle()
        
        return "``` New Deck Created ```"
        
    # Draws a card from the current deck
    def draw(self, text):
        msg = ''
        arg = ''
        card = None
        
        if len(self.deck) == 0:
            msg = "``` Deck is empty ```"
            return msg
        
        
        if len(text) > 3:
            arg = str(text[3])
        
        
        if arg == 'club' or arg == 'clubs':
            for c in self.deck:
                if c[1] == "Clubs":
                    card = c
                    self.deck.remove(c)
                    break
            
            if card == None:
                msg = "```No more clubs remain```"
                return msg
        
        elif arg == 'diamond' or arg == 'diamonds':
            for c in self.deck:
                if c[1] == "Diamonds":
                    card = c
                    self.deck.remove(c)
                    break
                    
            if card == None:
                msg = "```No more diamonds remain```"
                return msg
        
        elif arg == 'heart' or arg == 'hearts':
            for c in self.deck:
                if c[1] == "Hearts":
                    card = c
                    self.deck.remove(c)
                    break
                    
            if card == None:
                msg = "```No more hearts remain```"
                return msg
        
        elif arg == 'spade' or arg == 'spades':
            for c in self.deck:
                if c[1] == "Spades":
                    card = c
                    self.deck.remove(c)
                    break
                    
            if card == None:
                msg = "```No more spades remain```"
                return msg

        elif len(text) > 3:
            msg = "```" + arg + " not recognized```"
            return msg
            
        else:
            card = self.deck.pop()
            
            
        msg += "```Drew the "
        msg += card[0]
        msg += " of "
        msg += card[1]
        msg += "```"
        
        self.drawn.append(card)
        
        return msg
        
    # Shuffles deck
    def shuffle(self):
        random.shuffle(self.deck)
        return "``` Deck Shuffled ```"
        
    def size(self):
        size = len(self.deck)
        
        if size > 1:
            msg = "```There are "
        else:
            msg = "```There is "
            
        msg += str(size)
        
        if size > 1:
            msg += " cards left in the deck```"
        else:
            msg += " card left in the deck```"
            
        
        return msg
        
        
        
        
        
        
        
        
        