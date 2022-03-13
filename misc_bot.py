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
		if text[1] == 'i_fortune':
			msg = self.i_fortune(text)
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
	
	def i_fortune(self, text):
		msg = ''
	
		#msg += '*'
		for word in text[2:]:
			msg += word + " "
		msg = msg[:-1]
		#msg += '*\n'
	
		msg += random.choice([
				"LOOK TO LA LUNA",
				"DON'T LEAVE THE / HOUSE TODAY",
				"WE WILL ALL / DIE ONE DAY",
				"YOU ARE THROWING / YOUR LIFE AWAY",
				"GO OUTSIDE!",
				"GIVE UP!",
				"YOU WILL DIE ALONE",
				"ASK AGAIN LATER",
				"WAKE UP",
				"YOU ARE WORSHIPING / A SUN GOD",
				"STAY ASLEEP",
				"MARRY AND REPRODUCE",
				"QUESTION AUTHORITY",
				"THINK FOR YOURSELF",
				"STEVEN LIVES",
				"BRING HIM THE PHOTO",
				"YOUR SOUL / IS HIDDEN DEEP / WITHIN THE DARKNESS",
				"YOU WERE BORN WRONG",
				"YOU ARE DARK INSIDE",
				"YOU WILL NEVER / BE FORGIVEN",
				"WHEN LIFE / GIVES YOU LEMONS / REROLL!",
				"IT IS DANGEROUS / TO GO ALONE",
				"GO TO THE NEXT ROOM",
				"YOU WILL DIE",
				"WHY SO BLUE?",
				"YOUR PRINCESS / IS IN ANOTHER CASTLE",
				"YOU MAKE MISTAKES / IT IS ONLY / NATURAL",
				"A HANGED MAN / BRINGS YOU / NO LUCK TODAY",
				"THE DEVIL IN DISGUISE",
				"NOBODY KNOWS / THE TROUBLES / YOU HAVE SEEN",
				"DO NOT LOOK SO HURT / OTHERS / HAVE PROBLEMS TOO",
				"ALWAYS YOUR HEAD / IN THE CLOUDS",
				"DO NOT LOSE YOUR HEAD",
				"DO NOT CRY / OVER SPILLED TEARS",
				"WELL THAT / WAS WORTHLESS",
				"SUNRAYS ON YOUR / LITTLE FACE",
				"HAVE YOU SEEN THE EXIT?",
				"ALWAYS LOOK ON / THE BRIGHT SIDE",
				"GET A BABY PET / IT WILL CHEER YOU UP",
				"MEET STRANGERS / WITHOUT PREJUDICE",
				"ONLY A SINNER",
				"SEE WHAT HE SEES / DO WHAT HE DOES",
				"LIES",
				"LUCKY NUMBERS / 16 31 64 70 74",
				"GO DIRECTLY TO JAIL",
				"REBIRTH GOT CANCELLED",
				"FOLLOW THE CAT",
				"YOU LOOK FAT / YOU SHOULD / EXERCISE MORE",
				"TAKE YOUR MEDICINE",
				"COME TO A FORK / IN THE ROAD / TAKE IT",
				"BELIEVE IN YOURSELF",
				"TRUST NO ONE",
				"TRUST GOOD PEOPLE",
				"FOLLOW THE DOG",
				"FOLLOW THE ZEBRA",
				"WHAT DO YOU WANT / TO DO TODAY",
				"USE BOMBS WISELY",
				"LIVE TO DIE",
				"YOU ARE / PLAYING IT WRONG / GIVE ME THE CONTROLLER",
				"CHOOSE YOUR OWN PATH",
				"YOUR OLD LIFE / LIES IN RUIN",
				"I FEEL ASLEEP!!!",
				"MAY YOUR TROUBLES / BE MANY",
				"BLAME NOBODY / BUT YOURSELF"
				])
				
				
		return msg
				
	def starwars(self, text):
		msg = ''
		msg = '```'
		file = open("data/starwars.data", "r+")
		
		quotes = []
		
		for line in file:
			if line[0] == '#':
				pass
			elif line[0] == '-':
				quotes.append(line[1:])
		
		output = random.choice(quotes)
		msg += output
		msg += '```'
		
		file.close()
		return msg
		
	def cryptography(self, text):
		msg = 'https://www.youtube.com/watch?v=i_tPnQa-WAE&'
		return msg