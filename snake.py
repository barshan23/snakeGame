import pygame,random

pygame.init()

# 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)


display_height = 600
display_width = 800
FPS = 20
blockSize = 10

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake")
pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def showMessage(msg,color):
	textScreen = font.render(msg, True, color)
	gameDisplay.blit(textScreen, [display_width/2, display_height/2])

def snake(lead_x,lead_y,blockSize):
	pygame.draw.rect(gameDisplay, BLACK, [lead_x,lead_y,blockSize,blockSize])

def gameLoop():
	gameExit = False
	gameOver = False
	lead_x, lead_y = display_width/2,display_height/2
	lead_x_change = 0
	lead_y_change = 0

	randAppleX = round(random.randrange(0, display_width-blockSize)/10.0)*10.0
	randAppleY = round(random.randrange(0, display_height-blockSize)/10.0)*10.0

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(WHITE)
			showMessage("Game Over! Press C to play again, Q to quit game",RED)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameOver = False
						gameLoop()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -blockSize
					lead_y_change = 0
				if event.key == pygame.K_RIGHT:
					lead_x_change = blockSize
					lead_y_change = 0
				if event.key == pygame.K_UP:
					lead_y_change = -blockSize
					lead_x_change = 0
				if event.key == pygame.K_DOWN:
					lead_y_change = blockSize
					lead_x_change = 0

		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0 :
			gameOver = True

		lead_x += lead_x_change
		lead_y += lead_y_change
		gameDisplay.fill(WHITE)
		pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, blockSize, blockSize])
		snake(lead_x,lead_y,blockSize)
		pygame.display.update()

		if lead_x == randAppleX and lead_y == randAppleY:
			randAppleX = round(random.randrange(0, display_width-blockSize)/10.0)*10.0
			randAppleY = round(random.randrange(0, display_height-blockSize)/10.0)*10.0

		clock.tick(FPS)
	pygame.quit()
	quit()


gameLoop()