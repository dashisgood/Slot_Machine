import pygame
import sys
import random
import slot_logic
import slot_sounds

class AppUI:

	def __init__(self):	
		
		pygame.init()
		#print pygame.display.Info()
		self.screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
		pygame.display.set_caption("Slot Machine")
		self.clock = pygame.time.Clock()
		self.screen.fill((0,100,0))
		self.font0 = pygame.font.SysFont("Gothic", 100, (0,0,0))
		self.font1 = pygame.font.SysFont("Gothic", 50)
		pygame.display.update()

		self.s0 = pygame.image.load("images/Bananas.png")
		self.s1 = pygame.image.load("images/Watermelon.png")
		self.s2 = pygame.image.load("images/Plum.png")
		self.s3 = pygame.image.load("images/Lemon.png")
		self.s4 = pygame.image.load("images/Seven.png")
		self.s5 = pygame.image.load("images/Cherries.png")
		self.s6 = pygame.image.load("images/Orange.png")
		self.s7 = pygame.image.load("images/Bar.png")
		self.s8 = pygame.image.load("images/Bigwin.png")

		self.s0.convert()
		self.s1.convert()
		self.s2.convert()
		self.s3.convert()
		self.s4.convert()
		self.s5.convert()
		self.s6.convert()
		self.s7.convert()
		self.s8.convert()

		self.winnings_to_display = 0.0

		self.main()

	def main(self):

		self.set_wheels()
		main_loop = True
		count = 0
		while main_loop == True:
			
			self.clock.tick(5)			
			self.screen.fill((0,0,0))
			self.display_symbols()
			self.display_panel()
			
			pygame.display.update()

			
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q :
						pygame.quit()
						sys.exit()
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == pygame.K_s:
							self.winnings_to_display = 0.0
							self.bet()

					if event.key == pygame.K_UP:
						self.raise_bet()

					if event.key == pygame.K_DOWN:
						self.lower_bet()

					if event.key == pygame.K_t:
						slot_sounds.play_sound()

	def set_wheels(self):
		y=0
		 
		self.wheel0 = [[self.s0, y], [self.s1, y], [self.s2, y], [self.s3, y], [self.s4, y], [self.s5, y], [self.s6, y], [self.s7, y], [self.s8, y]]
		
		self.wheel1 = [[self.s6, y], [self.s0, y], [self.s2, y], [self.s4, y], [self.s8, y], [self.s1, y], [self.s3, y], [self.s5, y], [self.s7, y], ]
		 
		self.wheel2 = [[self.s4, y], [self.s7, y], [self.s3, y], [self.s1, y], [self.s0, y], [self.s8, y], [self.s5, y], [self.s2, y], [self.s6, y], ]

		for i in (self.wheel2, self.wheel1, self.wheel0):
			
			i[0][1] = 576
			i[1][1] = 384
			i[2][1] = 192
			i[3][1] = 0
			i[4][1] = -192
			i[5][1] = -384
			i[6][1] = -576
			i[7][1] = -768
			i[8][1] = -960

	def shift_wheels(self, sym):

		for i in range(sym[0]):
			self.wheel0.append(self.wheel0.pop(0))
		for i in range(sym[1]):
			self.wheel1.append(self.wheel1.pop(0))
		for i in range(sym[2]):
			self.wheel2.append(self.wheel2.pop(0))

		for i in (self.wheel2, self.wheel1, self.wheel0):
			
			i[0][1] = 576
			i[1][1] = 384
			i[2][1] = 192
			i[3][1] = 0
			i[4][1] = -192
			i[5][1] = -384
			i[6][1] = -576
			i[7][1] = -768
			i[8][1] = -960				

	def display_symbols(self):

		for i in self.wheel0:
			if 576 > i[1] > -192:
				self.screen.blit(i[0], (345, i[1]))
		for i in self.wheel1:
			if 576 > i[1] > -192:
				self.screen.blit(i[0], (567, i[1]))
		for i in self.wheel2:
			if 576 > i[1] > -192:
				self.screen.blit(i[0], (789, i[1]))

	def display_panel(self):

		bottom_rect = pygame.draw.rect(self.screen, (0,0,0), [0,576,1366,768])

		credit_label = self.font1.render("Credit: $%.2f" % game.player_money,1, (255,255,255))
		self.screen.blit(credit_label, (50,630))

		bet_label = self.font1.render("Bet: $%.2f" % game.denomination,1, (255,255,255))
		self.screen.blit(bet_label, (580,630))

		winningX_label = self.font1.render("Win: $%.2f" % (self.winnings_to_display),1, (255,255,255))
		self.screen.blit(winningX_label, (1040,630))

	def wheel_animation_frame(self,t0,t1, w0_speed, w1_speed, w2_speed):
		
		while t0 <= self.t < t1:

			self.clock.tick(90)
			self.screen.fill((0,0,0))
			for i in self.wheel0:
				if i[1] < 576:
					i[1] += w0_speed
				else:
					i[1] = -960 + w0_speed
			for i in self.wheel1:
				if i[1] < 576:
					i[1] += w1_speed
				else:
					i[1] = -960  + w1_speed
			for i in self.wheel2:
				if i[1] < 576:
					i[1] += w2_speed
				else:
					i[1] = -960  + w2_speed


			self.display_symbols()
			self.display_panel()
			pygame.display.update()
			self.t += 1														

	def spin_wheels(self):	
		
		self.t = -50
		
		self.wheel_animation_frame(-64,   12, 96, 96, 96)
		self.wheel_animation_frame( 12,   24, 48, 96, 96)
		self.wheel_animation_frame( 24,   40, 24, 96, 96)
		self.wheel_animation_frame( 40,   52, 16, 96, 96)
		self.wheel_animation_frame( 52,   64,  8, 96, 96)
		self.wheel_animation_frame( 64,   82,  4, 48, 48)
		self.wheel_animation_frame( 82,   94,  2, 24, 48)

		self.wheel_animation_frame( 94,  106,  0, 16, 24)
		self.wheel_animation_frame(106,  122,  0,  8, 24)
		self.wheel_animation_frame(122,  134,  0,  4, 12)
		self.wheel_animation_frame(134,  142,  0,  2,  8)
		
		self.wheel_animation_frame(142,  162,  0,  0,  8)
		self.wheel_animation_frame(162,  200,  0,  0,  4)
		self.wheel_animation_frame(200,  228,  0,  0,  2)
		

		pygame.event.get()

	def win_message(self, winningX):
		# t = 0
		# #self.screen.fill((0,0,0))
		# while t < 120:
		# 	self.clock.tick(90)
		# 	if winningX > -1:

				
		# 		label = self.font.render("$%.2f" % (winningX * game.denomination),1, (255,255,255))
		# 		self.screen.blit(label, (1000,100))
		# 		pygame.display.update()
		# 	t += 1
		# 	for event in pygame.event.get():
		# 		if event.type == pygame.KEYDOWN:
		# 			if event.key == pygame.K_s:
		# 				#self.bet()
		# 				return

		pass
						
	def raise_bet(self):
		
		if game.denomination < 5.0:
			game.denomination += .25
			slot_sounds.play_keyup()

	def lower_bet(self):
		
		if game.denomination > .25:
			game.denomination -= .25
			slot_sounds.play_keydown()

	def bet(self):
		
		if game.denomination > game.player_money:
			return

		slot_sounds.play_spinsound()
		winningX = game.make_bet()

		shiftcode = self.get_shiftcode(winningX)


		self.set_wheels()
		self.shift_wheels(shiftcode)
		self.spin_wheels()
		slot_sounds.play_sound(winningX)
		self.winnings_to_display = winningX * game.denomination
		game.update_account()
		self.win_message(winningX)
		self.display_panel()
		pygame.display.update()
		pygame.event.get()

	def get_shiftcode(self, winningX):

		symbol_codes = {
			'Bigwin':    (0,1,4),
			'Banana':    (1,7,3),
			'Watermelon':(2,2,2),
			'Plum':      (3,8,6),
			'Lemon':     (4,3,1),
			'Seven': 	 (5,0,8),
			'Cherries':  (6,4,5),
			'Orange':	 (7,6,7),
			'Bar':		 (8,5,0)

		}
		if winningX == 100:
			return symbol_codes['Bigwin']
		if winningX == 50:
			return symbol_codes['Bigwin']
		if winningX == 25:
			return symbol_codes['Plum']
		if winningX == 15:
			return symbol_codes['Banana']
		if winningX == 10:
			return symbol_codes['Watermelon']
		if winningX == 7:
			return symbol_codes['Seven']
		if winningX == 5:
			return symbol_codes['Plum']
		if winningX == 4:
			return symbol_codes['Bar']
		if winningX == 3:
			return symbol_codes['Cherries']
		if winningX == 2:
			return symbol_codes['Orange']
		if winningX == 1:
			return symbol_codes['Lemon']
		if winningX == 0:
			while True:
				code = (random.randrange(9), random.randrange(9),random.randrange(9),)
				if code not in symbol_codes.values():
					return code


if __name__ == '__main__':

	game = slot_logic.Game()
	app = AppUI()






