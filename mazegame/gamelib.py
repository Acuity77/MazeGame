import pygame
from pygame.locals import *

class SimpleGame(object):

	def __init__(self, title, background_color, window_size=(1280,960), fps =60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.is_terminated = False
		self.background_color = background_color

	def terminate(self):
		self.is_terminated = True 

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20 )
	        music = pygame.mixer.music.load("music.mp3")
	        pygame.mixer.music.play(-1)


	def run(self):
		self.init()
		while not self.is_terminated :
			self.__handle_events()
			#self.render()
			self.update()
			self.clock.tick(self.fps)
			self.surface.fill(self.background_color)
			self.render()
			pygame.display.update()
	
	def init(self):
		self.__game_init()

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()
	
	def on_key_up(self, key):
		pass

	def on_key_down(self, key):
		pass
	
	def update(self):
		pass

	def render(self):
		pass
