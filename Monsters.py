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
                                
					
		def moveMonster(self):
			for monster in RandomMap.isMonster:
				self.blockedUp = False
				self.blockedLeft = False
				self.blockedRight = False
				self.blockedDown = False
				self.movedX = False
				if monster[0] + 1 == player.gridpos_x and monster[1] == player.gridpos_y:
					self.blockedRight = True
				if monster[0] - 1 == player.gridpos_x and monster[1] == player.gridpos_y:
					self.blockedLeft = True
				if monster[1] + 1 == player.gridpos_y and monster[0] == player.gridpos_x:
					self.blockedDown = True
				if monster[1] - 1 == player.gridpos_y and monster[0] == player.gridpos_x:
					self.blockedUp = True
				
				for wall in RandomMap.isWall:
					if monster[0] + 1 == wall[0]  and monster[1] == wall[1]:
						self.blockedRight = True
					if monster[0] - 1 == wall[0]  and monster[1] == wall[1]:
						self.blockedLeft = True
					if monster[1] + 1 == wall[1] and monster[0] == wall[0]:
						self.blockedDown = True
					if monster[1] - 1 == wall[1] and monster[0] == wall[0]:
						self.blockedUp = True		
				

				if self.blockedLeft == False:
					if monster[0] > player.gridpos_x:
						monster[0] -= 1
						self.movedX = True
				if self.blockedRight == False:	
					if monster[0] < player.gridpos_x:
						monster[0] += 1				
						self.movedX = True
				
				if self.movedX == False:
					if self.blockedUp == False:	
						if monster[1] > player.gridpos_y:
							monster[1] -= 1
					if self.blockedDown == False:	
						if monster[1] < player.gridpos_y:
							monster[1] += 1
							

					
