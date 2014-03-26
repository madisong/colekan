from __future__ import division 
import pygame
from RandMap import *
from TDGlobals import *

class Player(object):
	def __init__(self, x, y, image):
	# MOVEMENT AND PLAYER LOCATION#
		self.character = pygame.image.load(image)
		self.rect = self.character.get_rect()
		self.rect.x = x * 8
		self.rect.y = y * 8
		self.playing = True
		self.moved = False
		self.movingL = None
		self.movingR = None
		self.movingU = None
		self.movingD = None
		self.current_x =  16 
		self.current_y =  16 
		self.gridpos_x = 2
		self.gridpos_y = 2
		self.beingBlockedRight = False
		self.beingBlockedLeft = False
		self.beingBlockedUp = False
		self.beingBlockedDown = False
		self.checkedPos = True
		self.fighting = False
	#PLAYER INVENTORY/ HEALTH/ ETC#
		self.hp  = 45
		self.exp = 1
		self.inv = ["dagger", "leather garb", "item!", "item!", "item!", "item!", "item!", "item!", "item!", "item!", ]
		self.equipped = {"hands": "dagger", "chest":"leather garb", "ring1": "none", "ring2": "none"}
		self.defense = 1
		self.power = 8
	
	def updatePos(self):
		self.gridpos_x = int(self.rect.x / 8)
		self.gridpos_y = int(self.rect.y / 8)
		
		
		
	def checkNextPos(self):
		self.beingBlockedUp = False
		self.beingBlockedDown = False
		self.beingBlockedRight = False
		self.beingBlockedLeft = False
		self.checkedPos = True
		self.fighting = True
		self.fightingR = False
		self.fightingL = False
		self.fightingU = False
		self.fightingD = False
		for pos in RandomMap.isWall:
			if self.gridpos_x + 1 == pos[0] and self.gridpos_y == pos[1]:
				self.beingBlockedRight = True
			if self.gridpos_x - 1 == pos[0] and self.gridpos_y == pos[1]:
				self.beingBlockedLeft = True
			if self.gridpos_y + 1 == pos[1] and self.gridpos_x == pos[0]:
				self.beingBlockedDown = True
			if self.gridpos_y - 1 == pos[1] and self.gridpos_x == pos[0]:
				self.beingBlockedUp = True
		
		for stat in RandomMap.isMonster:
			if self.gridpos_x + 1 == stat[0] and self.gridpos_y == stat[1]:
				self.beingBlockedRight = True
				self.fightingR = True
				self.fighting = True
			if self.gridpos_x - 1 == stat[0] and self.gridpos_y == stat[1]:
				self.beingBlockedLeft = True
				self.fightingL = True
				self.fighting = True
			if self.gridpos_y + 1 == stat[1] and self.gridpos_x == stat[0]:
				self.beingBlockedDown = True
				self.fightingD = True
				self.fighting = True
			if self.gridpos_y - 1 == stat[1] and self.gridpos_x == stat[0]:
				self.beingBlockedUp = True
				self.fightingU = True
				self.fighting = True
	


	def Combat(self):
		x = 0
		y = 0
		if self.fighting == True:
			for stat in RandomMap.isMonster:
				if self.fightingR == True:
					if self.gridpos_x + 1 == stat[0] and self.gridpos_y == stat[1]:
						x = stat[0]
						y = stat[1]
						self.damageCalc(x, y)
				if self.fightingL == True:
					if self.gridpos_x - 1 == stat[0] and self.gridpos_y == stat[1]:
						x = stat[0]
						y = stat[1]
						self.damageCalc(x, y)				
				if self.fightingD == True:
					if self.gridpos_y + 1 == stat[1] and self.gridpos_x == stat[0]:
						x = stat[0]
						y = stat[1]
						self.damageCalc(x, y)
				if self.fightingU == True:
					if self.gridpos_y - 1 == stat[1] and self.gridpos_x == stat[0]:
						x = stat[0]
						y = stat[1]
						self.damageCalc(x, y)
	
	def calcPlayerDamage(self, defense):
		self.baseDamage = self.exp * 1.5 + self.power
		self.playerDamage = self.baseDamage / 1 - defense / 1.3

	
	def damageCalc(self, x, y):
		for stat in RandomMap.isMonster:
			if stat[0] == x and stat[1] == y:
				self.calcPlayerDamage(stat[4])
				if self.playerDamage <= 0:
					print "You can't penetrate the " + str(stat[2]) + "'s armor!"
				elif self.playerDamage >= 0:
					stat[3] -= int(self.playerDamage)
					print "You deal " + str(int(self.playerDamage)) + " damage to the " + str(stat[2])
				
				if stat[3] >= 0:
					if stat[2] == "orc":
						orcDamage = random.randint(1, 4) / 1 - self.defense / 1.3
						if orcDamage <= 0:
							print "The " + str(stat[2]) + " can't penetrate your armor!"
						elif orcDamage >= 1:
							self.hp -= int(orcDamage) 
							print "The orc did " + str(int(orcDamage)) + " damage"
					
					if stat[2] == "imp":
						impDamage = random.randint(3, 7) / 1 - self.defense / 1.3
						if impDamage <= 0:
							print "The " + str(stat[2]) + " can't penetrate your armor!"
						
						elif impDamage >= 1:
							self.hp -= int(impDamage)
							print "The imp did " + str(int(impDamage)) + " damage"
				
					if stat[2] == "rat":
						ratDamage = random.randint(0, 2) / 1 - self.defense / 1.3
						if ratDamage <= 0:
							print "The " + str(stat[2]) + " can't penetrate your armor!"
						elif ratDamage >= 1:
							self.hp -= int(ratDamage)
							print "The rat did " + str(int(ratDamage)) + " damage"
				
					if stat[2] == "troll":
						trollDamage = random.randint(8, 11) / 1 - self.defense / 1.3
						if trollDamage <= 0:
							print "The " + str(stat[2]) + " can't penetrate your armor!"
						elif trollDamage >= 1:
							self.hp -= int(trollDamage)
							print "The troll did " + str(int(trollDamage)) + " damage"
					
					if stat[2] == "spider":
						spiderDamage = random.randint(3, 8) / 1 - self.defense / 1.3
						if spiderDamage <= 0:
							print "The " + str(stat[2]) + " can't penetrate your armor!"
						elif spiderDamage >= 1:
							self.hp -= int(spiderDamage)
							print "The spider did " + str(int(spiderDamage)) + " damage"				
				
				if stat[3] <= 0:
					RandomMap.isMonster.remove(stat)
					self.exp += 1
	def render(self):
		TDGlobals.screen.blit(self.character, (self.gridpos_x * 8, self.gridpos_y * 8))
player = Player(2, 2, "character.png")