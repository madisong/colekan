import os
import random
import pygame
import sys
#from TDGlobals import *
import TDGlobals as tdg
# TDGlobals.player = Player.Player(2, 2, "character.png")
from RandMap import *
from Player import *
from Monsters import *
from PlayerInventory import *
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



RandomMap.makeMap(RandomMap.level1)
RandomMap.map_update(0,0,RandomMap.level1)

print "Initializing window..." 
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("Destroy all monsters!")   #Sets up display/screen

tdg.screen = pygame.display.set_mode((500, 400))
tdg.player = Player(2, 2, "character.png")

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
		tdg.screen.blit(wallImg, (wall_x,wall_y))	
		
		#self.character = pygame.image.load(image)
def drawFloor():
	for floor in RandomMap.isSpace:
		floor_x = floor[0] * 8
		floor_y = floor[1] * 8
		tdg.screen.blit(stonefloorImg, (floor_x,floor_y))

def drawStatBox():
	invbox = pygame.Rect(400, 0, 100, 400)
	pygame.draw.rect(tdg.screen, (0,0,0), invbox)
			
def drawMonsters():
	for monster in RandomMap.isMonster:
		monster_x = monster[0] * 8
		monster_y = monster[1] * 8
		if monster[2] == "orc":    
			tdg.screen.blit(orcImg, (monster_x,monster_y))
		if monster[2] == "imp":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			tdg.screen.blit(impImg, (monster_x,monster_y))                   
		if monster[2] == "spider":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			tdg.screen.blit(spiderImg, (monster_x,monster_y))
		if monster[2] == "troll":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			tdg.screen.blit(trollImg, (monster_x,monster_y))
		if monster[2] == "rat":
			monster = pygame.Rect(monster_x, monster_y, 8, 8)
			tdg.screen.blit(ratImg, (monster_x,monster_y))	
			

#inventory = PlayerInventory()



Monsters = Monsters()
Monsters.remove0()
Monsters.assignStats()

inventory = PlayerInventory()

while tdg.player.playing: #main playing loop
	clock.tick(60)
	if tdg.player.hp <= 0:
		tdg.player.playing = False
	
	key = pygame.key.get_pressed()
	for e in pygame.event.get(): 
		if e.type == pygame.QUIT:
			tdg.player.playing = False
		if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
			tdg.player.playing = False	
		if e.type == pygame.KEYDOWN:		
			
			if e.key == pygame.K_i:
				if inventory.viewingInv == True:
					inventory.viewingInv = False
				
				elif inventory.viewingInv == False:
					inventory.viewingInv = True
					
			tdg.player.checkNextPos()
			
			#inventory.moveHighlight()

			
			if inventory.viewingInv == False:	
				tdg.player.Combat()
				if tdg.player.moved == False:						
					if tdg.player.checkedPos == True:
						if e.key == pygame.K_LEFT: 				
							if tdg.player.beingBlockedLeft == False:						
								tdg.player.updatePos()												
								tdg.player.checkedPos = False									
								tdg.player.movingL = True										
								tdg.player.moved = True											
								tdg.player.rect.x -= 8
						if  e.key == pygame.K_RIGHT:
							if tdg.player.beingBlockedRight == False:		
								tdg.player.updatePos()
								tdg.player.movingR = True
								tdg.player.moved = True	
								tdg.player.rect.x += 8
								tdg.player.checkedPos = False					
						if  e.key == pygame.K_DOWN:
							if tdg.player.beingBlockedDown == False:
								tdg.player.updatePos()
								tdg.player.movingD = True
								tdg.player.moved = True
								tdg.player.rect.y += 8
								tdg.player.checkedPos = False
						if  e.key == pygame.K_UP:
							if tdg.player.beingBlockedUp == False:					
								tdg.player.updatePos()
								tdg.player.checkedPos = False
								tdg.player.movingU = True
								tdg.player.moved = True
								tdg.player.rect.y -= 8
						if tdg.player.moved == True:
							tdg.player.updatePos()
							Monsters.moveMonster()
						if e.key == pygame.K_p:
							tdg.player.hp += 10
						if e.key == pygame.K_o:
							tdg.player.defense += 10		
		
		if e.type == pygame.KEYUP:
			if  e.key == pygame.K_LEFT:
				tdg.player.movingL = False
			if  e.key == pygame.K_RIGHT:
				tdg.player.movingR = False
			if  e.key == pygame.K_UP:
				tdg.player.movingU = False
			if  e.key == pygame.K_DOWN:
				tdg.player.movingD = False
			if tdg.player.moved == True:	
				if not tdg.player.movingL and not tdg.player.movingR and not tdg.player.movingU \
				and not tdg.player.movingD:	
					tdg.player.moved = False
	
	if RandomMap.isTele == True:
		if tdg.player.rect.colliderect(RandomMap.tele1):
			tdg.player.rect = pygame.Rect(RandomMap.tele2)
	
	if RandomMap.isEnd == True:
		if tdg.player.rect.colliderect(RandomMap.end_rect):
			RandomMap.onLevel += 1
			tdg.player.rect = pygame.Rect(16, 16, 8,8)
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
	pygame.draw.rect(tdg.screen, (50,50,50), playScreen)
	myfont = pygame.font.SysFont("monospace", 15)
	healthText = myfont.render("Health:" + str(tdg.player.hp) , 1, (255,60,60))
	defenseText = myfont.render("Defense:" + str(tdg.player.defense) , 1, (0,255,255))
	experienceText = myfont.render("Level:" + str(tdg.player.exp), 1, (34,139,34))
	
	drawStatBox()	
	
	
	tdg.screen.blit(healthText, (405, 10))
	tdg.screen.blit(defenseText, (405, 25))
	tdg.screen.blit(experienceText, (405, 40))
	drawFloor()
	# tdg.player.render(tdg.screen)
	tdg.player.render()
	drawMonsters()
	drawWall()
	inventory.makePlayerInv() # If drewinv = False, it will update the player inv. Set drewinv to false to re-draw
	
		#for rect in rectsInInv:
		#	pygame.draw.rect(tdg.screen, (0, 0, 100), rect)
		#	tdg.screen.blit(highlight, (h_x, h_y))
		#	tdg.screen.blit(rect, (x, y))
		#for text in textInInv:		
		
		
	if RandomMap.isTele == True:
		pygame.draw.rect(tdg.screen, (255, 255, 0), RandomMap.tele1)
		pygame.draw.rect(tdg.screen, (255, 255, 0), RandomMap.tele2)
	
	if RandomMap.isEnd == True:
		pygame.draw.rect(tdg.screen, (255, 0, 0), RandomMap.end_rect)
	

	
	pygame.display.flip()