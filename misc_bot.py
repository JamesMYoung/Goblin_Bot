import random

class misc_goblin:
	def __init__(self):
		print('Misc Goblin Created')
		try:
			self.fp = open("data/gold.data", "r+")
			self.gold_counter = int(self.fp.read())
		except IOError:
			self.fp = open("data/gold.data", "w")
			self.fp.close()
			self.fp = open("data/gold.data", "r+")
			self.gold_counter = 0
			
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
		if text[1] == 'uwu':
			msg = self.uwu(text)
		if text[1] == 'fortune':
			msg = self.fortune(text)
		if text[1] == 'starwars':
			msg = self.starwars(text)
		if text[1] == 'cryptography':
			msg = self.cryptography(text)
			
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
		
	def uwu(self, text):
		msg = ''
		msg += str(random.choice(['uwu','owo','OwO']))
		return msg
		
	def fortune(self, text):
		msg = ''
		
		if text[2] == None:
			msg += '```'
			msg += 'The goblin cannot provide a fortune if not asked a question'
			msg += '```'
		else:
			msg += '*'
			for word in text[2:]:
				msg += word + " "
			msg = msg[:-1]
			msg += '*\n'
			
			msg += random.choice([
				"It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you ",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don\'t count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."
				])
				
		return msg
		
	def starwars(self, text):
		msg = ''
		msg = '```'
		file = open("starwars.data", "r+")
		
		quotes = []
		
		for line in file:
			if line[0] == '#':
				pass
			elif line[0] == '-':
				quotes.append(line[1:])
		
		print(quotes)
		output = random.choice(quotes)
		msg += output
		msg += '```'
		
		file.close()
		return msg
		
	def cryptography(self, text):
		msg = 'https://www.youtube.com/watch?v=i_tPnQa-WAE&'
		return msg