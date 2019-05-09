import pygame
pygame.init()

size = (600, 600)

screen = pygame.display.set_mode(size)

image_file = pygame.image.load("saved.jpg")

image = pygame.transform.scale(image_file, (600, 600))

print("Hello")

def brighten():


		for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))
				r = color[0] + 15
				g = color[1] + 15
				b = color[2] + 15

				if r > 255:
					r = 255
				if g > 255:
					g = 255
				if b > 255:
					b = 255

				screen.set_at((x, y), (r, g, b))

def darken():

		for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x,y))
				r = color[0] - 15
				g = color[1] - 15
				b = color[2] - 15

				if r < 0:
					r = 0
				if g < 0:
					g = 0
				if b < 0:
					b = 0
				screen.set_at((x, y), (r, g, b))

def rmGreen():

	for x in range(0, 600):
		for y in range(0,600):
			color = screen.get_at((x, y))

			r = color[0]
			g = 0
			b = color[2]

			screen.set_at((x, y), (r, g, b))




def rmRed():

		for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				r = 0
				g = color[1]
				b = color[2]

				screen.set_at((x, y), (r, g, b))



def rmBlue():

	for x in range(0, 600):
		for y in range(0, 600):
			color = screen.get_at((x, y))

			r = color[0]
			g = color[1]
			b = 0

			screen.set_at((x, y), (r, g, b))

def negate():

	for x in range(0, 600):
		for y in range(0, 600):
			color = screen.get_at((x, y))

			r = 255 - color[0]
			g = 255 - color[1]
			b = 255 - color[2]

			screen.set_at((x, y), (r, g, b))


def intensify():
	for x in range(0, 600):
		for y in range(0, 600):
			color = screen.get_at((x, y))

			r = color[0]
			g = color[1]
			b = color[2]

			if r > 255 / 2:
				r = 255
			else:
				r = 0

			if g > 255 / 2:
				g = 255
			else:
				g = 0
			if b > 255 / 2:
				b = 255
			else:
				b = 0

			screen.set_at((x, y), (r, g, b))


def greyscale():


	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			r = color[0]
			g = color[1]
			b = color[2]

			average = (r+g+b) / 3
			screen.set_at((x, y), (average, average, average))

def two_tone():

	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			r = color[0]
			g = color[1]
			b = color[2]

			brightness = r + g +b

			if brightness > (255 * 3)/2.0:
				screen.set_at((x, y), (255, 255, 255))

			else:
				screen.set_at((x,y), (0, 0, 0))

def four_tone():

	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			max = 255 * 3

			r = color[0]
			g = color[1]
			b = color[2]

		brightness = r + g + b

		if brightness > (3/4) * max:
			screen.set_at((x, y), (240, 240, 120))

		elif brightness > (2/4) * max:
			screen.set_at((x,y), (240, 30, 30))

		elif brightness > (1/4) * max:
			screen.set_at((x,y), (15, 150, 15))

		else:
			screen.set_at((x, y), (15, 15, 80))





running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_l:
				screen.blit(image, image.get_rect())
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				screen.fill([100,50,100])

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				pygame.draw.circle(screen, [255, 0, 0], (300, 300), 10)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_b:
				brighten()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				darken()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				rmRed()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_2:
				rmGreen()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_3:
				rmBlue()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				pygame.image.save(screen, "c2f.png")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_5:
				negate()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_i:
				intensify()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_g:
				greyscale()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_t:
				two_tone()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				four_tone()



	pygame.display.flip()

