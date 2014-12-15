import pygame
from copy import copy, deepcopy
from pygame.locals import *
from gamelib import SimpleGame
from objects import *
from state import *

BLOCK_SIZE = (WINDOW_SIZE[0]/32,WINDOW_SIZE[1]/20)
BLACK = pygame.Color('black')
WHITE = pygame.Color('White')
CYAN = pygame.Color('cyan')
YELLOW = pygame.Color('yellow')

######################################################################################################################### 

class MazeGame(SimpleGame):
	
	def __init__(self , player = Player() , state = State() , block = [Block()] , block2 = [Block()] ):
		super(MazeGame, self).__init__('Maze', BLACK)
		self.player = player
		self.state = state
		self.numofMap = len(self.state.Map)
		self.current_block = block
		self.next_block = block2
		self.isCollide = False
		self.helpCollide = block[0]
		self.check_repeat_block = False
		self.saveplayer = self.player.pos
		self.changestate = 0
		self.changestate2 = 1
		self.can_use_next_map = True
		self.Initial_block()
		self.Next_map_block()

	#def Test(self):
	#	for b in self.block :
	#		print b.pos
	
	def CollideCondition(self,b):
		if self.player.pos[0] >= b.pos[0]+40 and self.player.pos[1] >= b.pos[1]+48 :
			return False
		elif self.player.pos[0] >= b.pos[0]+40 and self.player.pos[1] <= b.pos[1]+48 and self.player.pos[1] <= b.pos[1] :
			return False
		elif self.player.pos[0] <= b.pos[0]+40 and self.player.pos[1] >= b.pos[1]+48 and self.player.pos[0] <= b.pos[0] :
			return False
		else :
			return b.pos[0] <= self.player.pos[0]+10 and self.player.pos[0]-10 <= b.pos[0]+40 and b.pos[1] <= self.player.pos[1]+10 and self.player.pos[1]-10 <= b.pos[1]+48

	def CheckCollide(self):  ## Check Collide
		if self.isCollide == False :
			for b in self.current_block:
				if self.CollideCondition(b):
					self.isCollide = True
					self.helpCollide = b
					#print b
					break
		if  self.CollideCondition(self.helpCollide)== False :
			self.isCollide = False


	def Collide(self):  ## Condition Movement for Collide
		if self.isCollide == True :
			if self.player.pos[0] >= self.helpCollide.pos[0] and self.player.pos[0] >= self.helpCollide.pos[0]+40 and self.player.pos[1] >= self.helpCollide.pos[1] and self.player.pos[1] <= self.helpCollide.pos[1]+48: ## Collide Left 
				self.player.canmoveleft = False
				self.player.canmoveup = False
				self.player.canmovedown = False
			if self.player.pos[0] <= self.helpCollide.pos[0] and self.player.pos[0] <= self.helpCollide.pos[0]+40 and self.player.pos[1] >= self.helpCollide.pos[1] and self.player.pos[1] <= self.helpCollide.pos[1]+48: ## Colllide Right
				self.player.canmoveright = False
				self.player.canmoveup = False
				self.player.canmovedown = False
			if self.player.pos[0] >= self.helpCollide.pos[0] and self.player.pos[0] <= self.helpCollide.pos[0]+40 and self.player.pos[1] >= self.helpCollide.pos[1] and self.player.pos[1] >= self.helpCollide.pos[1]+48: ## Collide Up
				self.player.canmoveup = False
				self.player.canmoveleft = False
				self.player.canmoveright = False
			if self.player.pos[0] >= self.helpCollide.pos[0] and self.player.pos[0] <= self.helpCollide.pos[0]+40 and self.player.pos[1] <= self.helpCollide.pos[1] and self.player.pos[1] <= self.helpCollide.pos[1]+48: ## Collide Down
				self.player.canmovedown = False
				self.player.canmoveleft = False
				self.player.canmoveright = False
		else :
			self.player.canmoveright = True
			self.player.canmoveleft = True
			self.player.canmovedown = True
			self.player.canmoveup = True

	def Visible(self):
		pass
	
	def isGameOver(self):
		if ( self.player.pos[0] <= 0 or self.player.pos[0]>= WINDOW_SIZE[0] or self.player.pos[1] <=0 or self.player.pos[1] >= WINDOW_SIZE[1] ) :
			self.terminate()
			print 60000-pygame.time.get_ticks()

	def update(self):
		self.player.move(1./self.fps)
		self.isGameOver()
		self.player.pos = ( self.player.x , self.player.y )
		self.CheckCollide()
		self.Collide()
		if pygame.time.get_ticks()%1000 < 25 :
			#print pygame.time.get_ticks()%5000
			self.Change_state()
			#self.player.canmoveright = True     ## Can Walk After Change State
                        #self.player.canmoveleft = True
                        #self.player.canmovedown = True
                        #self.player.canmoveup = True
			#print (self.player.canmoveleft , self.player.canmoveright , self.player.canmoveup , self.player.canmovedown )
			#print self.helpCollide.pos
			#print ( self.player.pos[0] >= self.helpCollide.pos[0] and self.player.pos[0] >= self.helpCollide.pos[0]+40 and self.player.pos[1] >= self.helpCollide.pos[1] and self.player.pos[1] <= self.helpCollide.pos[1]+48,self.player.pos[0] <= self.helpCollide.pos[0] and self.player.pos[0] <= self.helpCollide.pos[0]+40 and self.player.pos[1] >= self.helpCollide.pos[1] and self.player.pos[1] <= self.helpCollide.pos[1]+48,self.player.pos[0] >= self.helpCollide.pos[0] and self.player.pos[0] <= self.helpCollide.pos[0]+40 and self.player.pos[1] >= self.helpCollide.pos[1] and self.player.pos[1] >= self.helpCollide.pos[1]+48,self.player.pos[0] >= self.helpCollide.pos[0] and self.player.pos[0] <= self.helpCollide.pos[0]+40 and self.player.pos[1] <= self.helpCollide.pos[1] and self.player.pos[1] <= self.helpCollide.pos[1]+48 )
		#print self.player.pos
		#print self.helpCollide.pos

	def Change_state(self): ## use to change state
		for i in range(self.numofMap) :
			self.Next_map_block()  ## Check_block2
			for b in self.next_block : 
				if b.pos[0] <= self.player.pos[0]+9 and self.player.pos[0]-9 <= b.pos[0]+36 and b.pos[1] <= self.player.pos[1]+9 and self.player.pos[1]-9 <= b.pos[1]+43 :
					self.can_use_next_map = False
					break
			if self.can_use_next_map == True :
				del self.current_block[:]
				self.current_block = deepcopy(self.next_block) ## next block to current
				self.changestate = self.changestate2            ## for render
				if ( self.changestate >= self.numofMap ):	## for render
					self.changestate = 0			## for render
				self.changestate2 += 1  
				if ( self.changestate2 >= self.numofMap ):
					self.changestate2 = 0
				del self.next_block[:]				## delete next_block
				break
			del self.next_block[:]
			self.can_use_next_map = True
			self.changestate2 += 1
			if ( self.changestate2 >= self.numofMap ) :
				self.changestate2 = 0 
	
	def Initial_block(self): ## Make_intitial_block
		for i in range(self.state.get_row()):
			for j in range(self.state.get_colum()):
				if self.state.Map[self.changestate][j+i*32] == "#" :
					for b in self.current_block:
						if b.pos == ( BLOCK_SIZE[0]*j , BLOCK_SIZE[1]*i ):	## check_repeat_block
							self.check_repeat_block = True
					if self.check_repeat_block == False :
						self.current_block.append(Block(pos = (BLOCK_SIZE[0]*j,BLOCK_SIZE[1]*i))) ## Make_new_block
					self.check_repeat_block = False

	def Next_map_block(self) : ## Make_Next_block
		for i in range(self.state.get_row()):
			for j in range(self.state.get_colum()):
				if self.state.Map[self.changestate2][j+i*32] == "#" :
					for b in self.next_block :
						if b.pos == ( BLOCK_SIZE[0]*j , BLOCK_SIZE[1]*i ):	## check_repeat_block
                                                        self.check_repeat_block = True
                                        if self.check_repeat_block == False :
                                                self.next_block.append(Block(pos = (BLOCK_SIZE[0]*j,BLOCK_SIZE[1]*i))) ## Make_new_block
                                        self.check_repeat_block = False

	def render_state(self): ## for render state in current block
		for i in range(self.state.get_row()):
			for j in range(self.state.get_colum()):
				if self.state.Map[self.changestate][j+i*32] == "#" :
					#try :
						self.current_block[0].draw(self.surface,i,j)	
					#except :						
						#pass					

	def render(self):
		self.player.draw(self.surface)
		self.render_state()

#############################################################################################################################

def main():
	game = MazeGame()
	game.run()

if __name__ == '__main__' :
	main()
