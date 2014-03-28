import pygame
import random

from TDGlobals import *

class RandomMap():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.level1 = []
		self.level2 = []
		self.level3 = []
		self.level4 = []
		self.charsLeft = 2500
		self.topWall = True
		self.sideWalls = 48
		self.bottomWall = True
		self.onLevel = 1
		self.end_rect = None
		self.isTele = False
		self.isEnd = False
		self.isSpace = [[0]*2 for i in range(5)]
		self.isWall = [[0]*2 for i in range(5)]
		self.isMonster = [[0]*3 for i in range(5)]
		self.isEnd = False
		self.spaceCountTop = 0
		self.spaceCountSide = 0
		self.spaceCount = 0
		self.smallmonsterCount = 0
		self.medmonsterCount = 0
		self.largemonsterCount = 0
	def makeMap(self, curr):

		while self.charsLeft > 0:
			self.charsLeft -= 1
			if self.topWall == True:
				self.topWall = False
				curr.append("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
			while self.sideWalls > 0:
				self.sideWalls -= 1
				curr.append("W                                                W")
			if self.bottomWall == True:
				self.bottomWall = False
				curr.append("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")

	
	def testWallPos(self, x, y):
		self.isWall.append([x / 8, y / 8])
		
	
	def declareFreeSpace(self, x, y):
		
		self.isSpace.append([x /8, y / 8])
		self.spaceCount += 1
		self.spaceCountTop += 1
		self.spawnChance = random.randint(0, 2500)	
		if self.smallmonsterCount <= 5:
			if self.onLevel < 3:
				if self.spawnChance >= 0 and self.spawnChance < 5:
					self.isMonster.append([x / 8, y /8, "orc", 0, 0])
					self.smallmonsterCount += 1
				if self.spawnChance >= 6 and self.spawnChance < 10:
					self.isMonster.append([x / 8, y / 8, "rat", 0, 0])
					self.smallmonsterCount += 1
		if self.medmonsterCount <= 4:
			if self.onLevel >= 2 and self.onLevel < 4:
				if self.spawnChance >= 11 and self.spawnChance < 15:
					self.isMonster.append([x / 8, y / 8, "imp", 0, 0])
					self.medmonsterCount += 1
				if self.spawnChance >= 16 and self.spawnChance < 21:
					self.isMonster.append([x / 8, y /8, "spider", 0, 0])
					self.medmonsterCount += 1
		if self.largemonsterCount <= 2:
			if self.onLevel >= 4 and self.onLevel < 14:
				if self.spawnChance >= 22 and self.spawnChance < 28:
					self.isMonster.append([x/ 8, y / 8, "troll", 0, 0])
					self.largemonsterCount += 1
		
		
		
		
		
		
		################################################################
		if self.spaceCountTop >= 1824:
			self.spaceCountSide += 1
			if self.spaceCountSide >= 38:
				if self.isEnd == False:
					if self.spawnChance >=496:
						self.end_rect = pygame.Rect(x, y, 8, 8)
						self.isEnd = True
			if self.spaceCountSide == 48:
				self.spaceCountSide = 0
		if self.spaceCount == 2304:
			if self.isEnd == False:	
				self.end_rect = pygame.Rect(x, y, 8, 8)
				self.isEnd = True
			
				
	def map_update(self, x, y, curr):
		self.x = 0
		self.y = 0
		self.level1 = []
		self.level2 = []
		self.level3 = []
		self.level4 = []
		self.charsLeft = 2500
		self.topWall = True
		self.sideWalls = 48
		self.bottomWall = True
		self.end_rect = None
		self.isTele = False
		self.isEnd = False
		self.isSpace = [[0]*2 for i in range(5)]
		self.isWall = [[0]*2 for i in range(5)]
		self.isMonster = [[0]*3 for i in range(5)]
		self.isEnd = False
		self.spaceCountTop = 0
		self.spaceCountSide = 0
		self.spaceCount = 0
		self.smallmonsterCount = 0
		self.medmonsterCount = 0
		self.largemonsterCount = 0
		print "Generating map!"
		for row in curr:
			for col in row:
				if col == " ":
					self.declareFreeSpace(x, y)

				if col == "W":
					self.testWallPos(x, y)
				if col == "E":
					self.isEnd = True
					self.end_rect = pygame.Rect(x, y, 8, 8)    
				if col == "A":
					self.isTele = True
					self.tele1 = pygame.Rect(x, y, 8, 8)
				if col == "B":
					self.isTele = True
					self.tele2 = pygame.Rect(x, y, 8, 8)
				x += 8
			y += 8
			x = 0




RandomMap = RandomMap()	
	

