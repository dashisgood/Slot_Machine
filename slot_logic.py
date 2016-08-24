import random

class Game:

	denomination = .25
	player_money = 200 * denomination
	bet_multiplier = 0 * denomination

	odds_table = [
		5	,
		15	,
		80	,
		167	,
		287	,
		430	,
		630	,
		880	,
		1213	,
		1713	,
		1808	,
		10000
	]

	t = odds_table		

	def make_bet(self,bet=1):
		self.player_money -= bet * self.denomination
		self.bet_multiplier = self.get_bet_multiplier()
		return self.bet_multiplier

	def get_bet_multiplier(self):


		rand_num = random.randrange(0,10000)
		
		if rand_num <   self.t[0]:
			return 100
		elif rand_num < self.t[1]:
			return 50
		elif rand_num < self.t[2]:
			return 25
		elif rand_num < self.t[3]:
			return 15
		elif rand_num < self.t[4]:
			return 10
		elif rand_num < self.t[5]:
			return 7
		elif rand_num < self.t[6]:
			return 5
		elif rand_num < self.t[7]:
			return 4
		elif rand_num < self.t[8]:
			return 3
		elif rand_num < self.t[9]:
			return 2
		elif rand_num < self.t[10]:
			return 1
		elif rand_num < self.t[11]:
			return 0

	def update_account(self):

		self.player_money += self.bet_multiplier * self.denomination