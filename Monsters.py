import pygame
import random
from RandMap import *
from Player import *

class Monsters():
		def __init__(self):
			self.orcHP = 10
			self.orcDef = 5
			self.impHP = 15
			self.impDef = 2
			self.trollHP = 25
			self.trollDef = 10
			self.spiderHP = 6
			self.spiderDef = 5
			self.ratHP = 3
			self.ratDef = 1
			self.monsterR = False
			self.monsterL = False
			self.monsterU = False
			self.monsterD = False	
		def assignStats(self):
			print "Monsters getting buff!"
			
			for monster in RandomMap.isMonster:
				self.smallhpBuffer = random.randint(-2, 7)
				self.smalldefBuffer = random.randint(-1, 3)
				self.medhpBuffer = random.randint(5, 10)
				self.meddefBuffer = random.randint(3, 6)
				self.largehpBuffer = random.randint(10, 16)
				self.largedefBuffer = random.randint(5, 10)
				if monster[2] == "orc":
					monster[3] = self.orcHP + RandomMap.onLevel + self.smallhpBuffer
					monster[4] = self.orcDef + RandomMap.onLevel + self.smalldefBuffer
				if monster[2] == "imp":
					monster[3] = self.impHP + RandomMap.onLevel + self.smallhpBuffer
					monster[4] = self.impDef + RandomMap.onLevel + self.smalldefBuffer
				if monster[2] == "rat":
					monster[3] = self.ratHP + RandomMap.onLevel + self.smallhpBuffer
					monster[4] = self.ratDef + RandomMap.onLevel + self.smalldefBuffer
				if monster[2] == "jackal":
					pass
				if monster[2] == "troll":
					monster[3] = self.trollHP + RandomMap.onLevel + self.medhpBuffer
					monster[4] = self.trollDef + RandomMap.onLevel + self.meddefBuffer
				if monster[2] == "goblin":
					pass
				if monster[2] == "spider":
					monster[3] = self.spiderHP + RandomMap.onLevel + self.medhpBuffer
					monster[4] = self.spiderDef + RandomMap.onLevel + self.meddefBuffer
                def remove0(self):
                        for zeros in RandomMap.isMonster:
                            if RandomMap.isMonster[0] == [0, 0, 0]:
                                del RandomMap.isMonster[0]
                                
		def checkMonsterPos(self):
			self.monsterR = False
			self.monsterL = False
			self.monsterU = False
			self.monsterD = False
			for monster in RandomMap.isMonster:
				for pos in RandomMap.isWall:
					if monster[0] + 1 == pos[0] and monster[1] == pos[1]:
						self.monsterR = True
					if monster[0] - 1 == pos[0] and monster[1] == pos[1]:
						self.monsterL = True
					if monster[1] + 1 == pos[1] and monster[0] == pos[0]:
						self.monsterD = False
					if monster[1] - 1 == pos[1] and monster[0] == pos[0]:
						selfmonsterU = False
			
		def moveMonster(self):
			for monster in RandomMap.isMonster:
				moveRight = (monster[0] + 1) - player.gridpos_x
				moveLeft = (monster[0] - 1) - player.gridpos_x
				moveUp = (monster[1] - 1) - player.gridpos_y
				moveDown = (monster[1] + 1) - player.gridpos_y
				if moveRight < moveLeft and moveRight < moveUp and moveRight < moveDown:
					monster[0] += 1
				elif moveLeft < moveRight and moveLeft < moveUp and moveLeft < moveDown:
					monster[0] -= 1
				elif moveUp < moveRight and moveUp < moveLeft and moveUp < moveDown:
					monster[1] -= 1
				elif moveDown < moveUp and moveDown < moveRight and moveDown < moveLeft:
					monster[1] += 1
					
