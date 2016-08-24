import pygame


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

long_bell = pygame.mixer.Sound('sounds/LongBell.wav')
oh_yeah = pygame.mixer.Sound('sounds/OhYeah.wav')
cha_ching = pygame.mixer.Sound('sounds/ChaChing.wav')
hi_ding = pygame.mixer.Sound('sounds/HiDing.wav')
lo_ding = pygame.mixer.Sound('sounds/LoDing.wav')
spin_beep = pygame.mixer.Sound('sounds/SpinBeep.wav')

spin_beep.set_volume(.3)
hi_ding.set_volume(.2)
lo_ding.set_volume(.2)


def play_sound(winningX):

	if 0 < winningX < 5:
		long_bell.play()
		cha_ching.play()
		return
	if winningX > 5:
		cha_ching.play()
		oh_yeah.play()

		return

def play_keyup():

	hi_ding.stop()
	hi_ding.play()

def play_keydown():
	lo_ding.stop()
	lo_ding.play()

def play_spinsound():

	spin_beep.play()