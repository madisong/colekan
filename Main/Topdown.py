import os
import random
import pygame
import sys
from RandMap import *
# from Player import *
from Monsters import *
from TDGlobals import *
# from PlayerInventory import *
""" 

TODO:
	
	Inventory overlay:
		equipping items
		highlighting
	
	Player:
		know whats equipped and what it does

	monster AI:
		as good as it can get while no walls
	
	Level Gen:
		add randomization
	
"""

TDGlobals = TDGlobals()

RandomMap.makeMap(RandomMap.level1)
RandomMap.map_update(0,0,RandomMap.level1)
print "Initializing window..." 
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("Destroy all monsters!")   #Sets up display/screen
TDGlobals.screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()


stonefloorImg = pygame.image.load(os.path.join('Images', 'stonefloor.png'))
wallImg = pygame.image.load(os.path.join('Images', 'wall.png'))
orcImg = pygame.image.load(os.path.join('Images', 'orc.png'))
impImg = pygame.image.load(os.path.join('Images', 'imp.png'))
spiderImg = pygame.image.load(os.path.join('Images', 'spider.png'))
trollImg = pygame.image.load(os.path.join('Images', 'troll.png'))
ratImg = pygame.image.load(os.path.join('Images', 'rat.png'))


def drawWall():
	for walls in RandomMap.isWall:
		wall_x = walls[0] * 8
		wall_y = walls[1] * 8
		TDGlobals.screen.blit(wallImg, (wall_x,wall_y))	
		
		#self.character = pygame.image.load(image)
def drawFloor():
	for floor in RandomMap.isSpace:
		floor_x = floor[0] * 8
		floor_y = floor[1] * 8
		TDGlobals.screen.blit(stonefloorImg, (floor_x,floor_y))

def drawStatBox():
	invbox = pygame.Rect(400, 0, 100, 400)
	pygame.draw.rect(TDGlobals.screen, (0,0,0), invbox)
			
def drawMonsters():
	for monster in RandomMap.isMonster:
		monster_x = monster[0] * 8
		monster_y = monster[1] * 8
		if monster[2] == "orc":    
			TDGlobals.screen.blit(orcImg, (monster_x,monster_y))
		if monster[2] == "imp":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			TDGlobals.screen.blit(impImg, (monster_x,monster_y))                   
		if monster[2] == "spider":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			TDGlobals.screen.blit(spiderImg, (monster_x,monster_y))
		if monster[2] == "troll":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			TDGlobals.screen.blit(trollImg, (monster_x,monster_y))
		if monster[2] == "rat":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			TDGlobals.screen.blit(ratImg, (monster_x,monster_y))	
			

#inventory = PlayerInventory()



Monsters = Monsters()
Monsters.remove0()
Monsters.assignStats()

while TDGlobals.player.playing: #main playing loop
	clock.tick(60)
	if TDGlobals.player.hp <= 0:
		TDGlobals.player.playing = False
	
	key = pygame.key.get_pressed()
	for e in pygame.event.get(): 
		if e.type == pygame.QUIT:
			TDGlobals.player.playing = False
		if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
			TDGlobals.player.playing = False	
		if e.type == pygame.KEYDOWN:		
			
			if e.key == pygame.K_i:
				if inventory.viewingInv == True:
					inventory.viewingInv = False
				
				elif inventory.viewingInv == False:
					inventory.viewingInv = True
					
			TDGlobals.player.checkNextPos()
			
			#inventory.moveHighlight()

			
			if inventory.viewingInv == False:	
				TDGlobals.player.Combat()
				if TDGlobals.player.moved == False:						
					if TDGlobals.player.checkedPos == True:
						if e.key == pygame.K_LEFT: 				
							if TDGlobals.player.beingBlockedLeft == False:						
								TDGlobals.player.updatePos()												
								TDGlobals.player.checkedPos = False									
								TDGlobals.player.movingL = True										
								TDGlobals.player.moved = True											
								TDGlobals.player.rect.x -= 8
						if  e.key == pygame.K_RIGHT:
							if TDGlobals.player.beingBlockedRight == False:		
								TDGlobals.player.updatePos()
								TDGlobals.player.movingR = True
								TDGlobals.player.moved = True	
								TDGlobals.player.rect.x += 8
								TDGlobals.player.checkedPos = False					
						if  e.key == pygame.K_DOWN:
							if TDGlobals.player.beingBlockedDown == False:
								TDGlobals.player.updatePos()
								TDGlobals.player.movingD = True
								TDGlobals.player.moved = True
								TDGlobals.player.rect.y += 8
								TDGlobals.player.checkedPos = False
						if  e.key == pygame.K_UP:
							if TDGlobals.player.beingBlockedUp == False:					
								TDGlobals.player.updatePos()
								TDGlobals.player.checkedPos = False
								TDGlobals.player.movingU = True
								TDGlobals.player.moved = True
								TDGlobals.player.rect.y -= 8
						if TDGlobals.player.moved == True:
							TDGlobals.player.updatePos()
							Monsters.moveMonster()
						if e.key == pygame.K_p:
							TDGlobals.player.hp += 10
						if e.key == pygame.K_o:
							TDGlobals.player.defense += 10		
		
		if e.type == pygame.KEYUP:
			if  e.key == pygame.K_LEFT:
				TDGlobals.player.movingL = False
			if  e.key == pygame.K_RIGHT:
				TDGlobals.player.movingR = False
			if  e.key == pygame.K_UP:
				TDGlobals.player.movingU = False
			if  e.key == pygame.K_DOWN:
				TDGlobals.player.movingD = False
			if TDGlobals.player.moved == True:	
				if not TDGlobals.player.movingL and not TDGlobals.player.movingR and not TDGlobals.player.movingU \
				and not TDGlobals.player.movingD:	
					TDGlobals.player.moved = False
	
	if RandomMap.isTele == True:
		if TDGlobals.player.rect.colliderect(RandomMap.tele1):
			TDGlobals.player.rect = pygame.Rect(RandomMap.tele2)
	
	if RandomMap.isEnd == True:
		if TDGlobals.player.rect.colliderect(RandomMap.end_rect):
			RandomMap.onLevel += 1
			TDGlobals.player.rect = pygame.Rect(16, 16, 8,8)
			if RandomMap.onLevel == 2: 
				RandomMap.makeMap(RandomMap.level2)
				RandomMap.map_update(0, 0, RandomMap.level2)
			if RandomMap.onLevel == 3:
				RandomMap.makeMap(RandomMap.level3)
				RandomMap.map_update(0, 0, RandomMap.level3)
			if RandomMap.onLevel == 4:
				RandomMap.makeMap(RandomMap.level4)
				RandomMap.map_update(0, 0, RandomMap.level4)
			if RandomMap.onLevel == 5:
				RandomMap.makeMap(RandomMap.level5)
				RandomMap.map_update(0, 0, RandomMap.level5)
			if RandomMap.onLevel == 6:
				RandomMap.makeMap(RandomMap.level6)
				RandomMap.map_update(0, 0, RandomMap.level6)
			if RandomMap.onLevel == 7:
				RandomMap.makeMap(RandomMap.level7)
				RandomMap.map_update(0, 0, RandomMap.level7)
			if RandomMap.onLevel == 8:
				RandomMap.makeMap(RandomMap.level8)
				RandomMap.map_update(0, 0, RandomMap.level8)
			if RandomMap.onLevel == 9:
				RandomMap.makeMap(RandomMap.level9)
				RandomMap.map_update(0, 0, RandomMap.level9)
			if RandomMap.onLevel == 10:
				RandomMap.makeMap(RandomMap.level10)
				RandomMap.map_update(0, 0, RandomMap.level10)

	playScreen = pygame.Rect(0, 0, 400, 400)
	pygame.draw.rect(TDGlobals.screen, (50,50,50), playScreen)
	myfont = pygame.font.SysFont("monospace", 15)
	healthText = myfont.render("Health:" + str(TDGlobals.player.hp) , 1, (255,60,60))
	defenseText = myfont.render("Defense:" + str(TDGlobals.player.defense) , 1, (0,255,255))
	experienceText = myfont.render("Level:" + str(TDGlobals.player.exp), 1, (34,139,34))
	
	drawStatBox()	
	
	
	TDGlobals.screen.blit(healthText, (405, 10))
	TDGlobals.screen.blit(defenseText, (405, 25))
	TDGlobals.screen.blit(experienceText, (405, 40))
	drawFloor()
	TDGlobals.player.render()
	drawMonsters()
	drawWall()
	inventory.makePlayerInv() # If drewinv = False, it will update the player inv. Set drewinv to false to re-draw
	
		#for rect in rectsInInv:
		#	pygame.draw.rect(TDGlobals.screen, (0, 0, 100), rect)
		#	TDGlobals.screen.blit(highlight, (h_x, h_y))
		#	TDGlobals.screen.blit(rect, (x, y))
		#for text in textInInv:		
		
		
	if RandomMap.isTele == True:
		pygame.draw.rect(TDGlobals.screen, (255, 255, 0), RandomMap.tele1)
		pygame.draw.rect(TDGlobals.screen, (255, 255, 0), RandomMap.tele2)
	
	if RandomMap.isEnd == True:
		pygame.draw.rect(TDGlobals.screen, (255, 0, 0), RandomMap.end_rect)
	

	
	pygame.display.flip()