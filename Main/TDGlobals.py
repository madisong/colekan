import pygame
from Player import *
class TDGlobals():
	
	def __init__(self):
		self.screen = None
		self.player = Player(2, 2, "character.png")