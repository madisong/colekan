import os
import random
import pygame
import sys
from RandMap import *
from Player import *
from Monsters import *
from TDGlobals import *


viewingInv = False
RandomMap.makeMap(RandomMap.level1)
RandomMap.map_update(0,0,RandomMap.level1)
print "Initializing window..." 
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("Destroy all monsters!")   #Sets up display/screen
TDGlobals.screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
h_x = 0
h_y = 0
drewinv = False
stonefloorImg = pygame.image.load("stonefloor.png")
wallImg = pygame.image.load("wall.png")
orcImg = pygame.image.load("orc.png")
impImg = pygame.image.load("imp.png")
spiderImg = pygame.image.load("spider.png")
trollImg = pygame.image.load("troll.png")
ratImg = pygame.image.load("rat.png")
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
			


Monsters = Monsters()
Monsters.remove0()
Monsters.assignStats()

while player.playing: #main playing loop
	clock.tick(60)
	if player.hp <= 0:
		player.playing = False
	
	key = pygame.key.get_pressed()
	for e in pygame.event.get(): 
		if e.type == pygame.QUIT:
			player.playing = False
		if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
			player.playing = False	
		if e.type == pygame.KEYDOWN:		# if keydown
			
			if e.key == pygame.K_i:
				if viewingInv == True:
					viewingInv = False
				
				elif viewingInv == False:
					viewingInv = True
					
			player.checkNextPos()
			
			if viewingInv == True:
				if  e.key == pygame.K_DOWN:
					h_y += 20
				if e.key == pygame.K_UP:
					h_y -= 20
			
			if viewingInv == False:	
				player.Combat()
				if player.moved == False:						
					if player.checkedPos == True:
						if e.key == pygame.K_LEFT: 				
							if player.beingBlockedLeft == False:						
								player.updatePos()												
								player.checkedPos = False									
								player.movingL = True										
								player.moved = True											
								player.rect.x -= 8
						if  e.key == pygame.K_RIGHT:
							if player.beingBlockedRight == False:		
								player.updatePos()
								player.movingR = True
								player.moved = True	
								player.rect.x += 8
								player.checkedPos = False					
						if  e.key == pygame.K_DOWN:
							if player.beingBlockedDown == False:
								player.updatePos()
								player.movingD = True
								player.moved = True
								player.rect.y += 8
								player.checkedPos = False
						if  e.key == pygame.K_UP:
							if player.beingBlockedUp == False:					
								player.updatePos()
								player.checkedPos = False
								player.movingU = True
								player.moved = True
								player.rect.y -= 8
			player.updatePos()
			Monsters.checkMonsterPos()
			Monsters.moveMonster()
		if e.type == pygame.KEYUP:
			if  e.key == pygame.K_LEFT:
				player.movingL = False
			if  e.key == pygame.K_RIGHT:
				player.movingR = False
			if  e.key == pygame.K_UP:
				player.movingU = False
			if  e.key == pygame.K_DOWN:
				player.movingD = False
			if player.moved == True:	
				if not player.movingL and not player.movingR and not player.movingU \
				and not player.movingD:	
					player.moved = False
	
	if RandomMap.isTele == True:
		if player.rect.colliderect(RandomMap.tele1):
			player.rect = pygame.Rect(RandomMap.tele2)
	
	if RandomMap.isEnd == True:
		if player.rect.colliderect(RandomMap.end_rect):
			RandomMap.onLevel += 1
			player.rect = pygame.Rect(16, 16, 8,8)
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
			Monsters.assignStats()
	
	playScreen = pygame.Rect(0, 0, 400, 400)
	pygame.draw.rect(TDGlobals.screen, (50,50,50), playScreen)
	myfont = pygame.font.SysFont("monospace", 15)
	healthText = myfont.render("Health:" + str(player.hp) , 1, (255,60,60))
	defenseText = myfont.render("Defense:" + str(player.defense) , 1, (0,255,255))
	experienceText = myfont.render("Level:" + str(player.exp), 1, (34,139,34))
	
	drawStatBox()	
	
	
	TDGlobals.screen.blit(healthText, (405, 10))
	TDGlobals.screen.blit(defenseText, (405, 25))
	TDGlobals.screen.blit(experienceText, (405, 40))
	drawFloor()
	player.render()
	drawMonsters()
	drawWall()
	

	
	
	
	
	
	
	if viewingInv == True:  
		x = 0
		y = 0

		highlight = pygame.Surface((110, 15))
		highlight.set_alpha(8)
		highlight.fill((255,255,0))
		if drewinv == False:
			drewinv == True
			for item in player.inv:
				displayitem = myfont.render(item , 1, (0,0,0))
				backText = pygame.Rect(x, y, 110, 15)
				pygame.draw.rect(TDGlobals.screen, (0,0,255), backText)
				TDGlobals.screen.blit(highlight, (h_x, h_y))
				TDGlobals.screen.blit(displayitem, (x, y))
				y += 20


					
	
	if RandomMap.isTele == True:
		pygame.draw.rect(TDGlobals.screen, (255, 255, 0), RandomMap.tele1)
		pygame.draw.rect(TDGlobals.screen, (255, 255, 0), RandomMap.tele2)
	
	if RandomMap.isEnd == True:
		pygame.draw.rect(TDGlobals.screen, (255, 0, 0), RandomMap.end_rect)
	

	
	pygame.display.flip()